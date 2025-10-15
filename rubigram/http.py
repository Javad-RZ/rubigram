from aiohttp import ClientSession, TCPConnector, ClientTimeout
from typing import Optional
import logging


logger = logging.getLogger(__name__)


class Http:
    def __init__(self, timeout: Optional[float] = 30):
        self.timeout = timeout
        self.session: Optional[ClientSession] = None

    async def connect(self):
        connector = TCPConnector(limit=100)
        timeout = ClientTimeout(total=self.timeout)
        if self.session is None:
            self.session = ClientSession(connector=connector, timeout=timeout)
            logger.info("[<] Open HTTP session")

    async def disconnect(self):
        if self.session:
            await self.session.close()
            self.session = None
            logger.info("[<] Close HTTP session")

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.disconnect()