from typing import Callable
import rubigram


class OnStop:
    def on_stop(
        self: "rubigram.Client",
        func: Callable[["rubigram.Client"], None]
    ):
        """Register a shutdown handler.

        This decorator registers a function that will be called when the
        client stops. It is typically used for cleaning up resources,
        saving data, or closing database connections before shutdown.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            func (Callable[[rubigram.Client], None]): The async function to be executed on shutdown.

        Returns:
            Callable: The function itself, after being registered.

        Example:
            >>> @app.on_stop
            >>> async def on_stop(client):
            >>>     print("Bot stopped gracefully.")
        """
        self.on_stop_app.append(func)
        return func