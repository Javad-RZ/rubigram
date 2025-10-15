from .method import Method
from .http import Http
from .handler import Handler
from aiohttp.web import Application, Request, json_response, run_app
from datetime import datetime
from typing import Optional, Callable
from .logger import logger
import asyncio


class Client(Method):
    def __init__(
        self,
        token: str,
        endpoint: Optional[str] = None,
        host: Optional[str] = "0.0.0.0",
        port: Optional[int] = 8000,
        timeout: Optional[float] = 30
    ):
        self.token = token
        self.endpoint = endpoint
        self.host = host
        self.port = port
        self.timeout = timeout
        self.offset_id = None
        self.http: Http = Http(timeout)
        self.set_endpoint = True
        self.handlers: dict[str, list[Handler]] = {
            "message": [],
            "inline": [],
            "delete": [],
            "edit": [],
        }
        self.on_start_app: list[Callable] = []
        self.on_stop_app: list[Callable] = []
        self.routes = []
        super().__init__(self)

    async def start(self):
        await self.http.connect()

    async def stop(self):
        await self.http.disconnect()

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, *args):
        await self.stop()

    async def run_start_app(self):
        for func in self.on_start_app:
            try:
                await func(self)
            except Exception as error:
                logger.error("[!] On Start App Error : {}".format(error))

    async def run_stop_app(self):
        for func in self.on_stop_app:
            try:
                await func(self)
            except Exception as error:
                logger.error("[!] On Stop App Error : {}".format(error))

    async def startup(self, app):
        await self.run_start_app()
        if self.set_endpoint:
            await self.setup_endpoints()
        await self.start()

    async def cleanup(self, app):
        await self.run_stop_app()
        await self.stop()

    def request_handler(self):
        async def wrapper(request: Request):
            data = await request.json()
            await self.updater(data)
            return json_response({"status": "OK"})
        return wrapper

    async def run_polling(self):
        try:
            await self.run_start_app()
            await self.start()
            while True:
                response = await self.get_updates(100, self.offset_id)
                updates = response.updates

                if updates:
                    for update in updates:
                        message_time = (
                            update.new_message.time
                            if update.type == "NewMessage"
                            else update.updated_message.time
                            if update.type == "UpdatedMessage"
                            else None
                        )

                        if message_time:
                            now = int(datetime.now().timestamp())
                            if int(message_time) + 2 >= now:
                                update.client = self
                                await self.dispatch(update)

                    self.offset_id = response.next_offset_id

        except Exception as error:
            logger.error("[!] {} : {}".format(__class__.__name__, error))

        finally:
            await self.run_stop_app()
            await self.stop()

    def run(
        self,
        set_endpoint: Optional[bool] = True
    ):
        self.set_endpoint = set_endpoint
        if self.endpoint:
            app = Application()
            app.on_startup.append(self.startup)
            app.on_cleanup.append(self.cleanup)

            app.router.add_post("/ReceiveUpdate", self.request_handler())
            app.router.add_post("/ReceiveInlineMessage", self.request_handler())

            for path, func, method in self.routes:
                app.router.add_route(method, path, func)

            logger.info("[<] Start bot on {}:{}".format(self.host, self.port))
            run_app(app, host=self.host, port=self.port)

        else:
            try:
                logger.info("[<] Start bot ...")
                asyncio.run(self.run_polling())

            except KeyboardInterrupt:
                logger.info("[<] Stop bot")

            except Exception as error:
                logger.error("[!] Unexpected error : {}".format(error))