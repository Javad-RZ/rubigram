from typing import Callable
import rubigram


class OnStart:
    def on_start(
        self: "rubigram.Client",
        func: Callable[["rubigram.Client"], None]
    ):
        """Register a startup handler.

        This decorator registers a function that will be called when the
        client starts. It is typically used for initializing resources,
        database connections, or performing setup tasks before the bot begins
        processing updates.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            func (Callable[[rubigram.Client], None]): The async function to be executed on startup.

        Returns:
            Callable: The function itself, after being registered.

        Example:
            >>> @app.on_start
            >>> async def on_start(client):
            >>>     print("Bot started and ready!")
        """
        self.on_start_app.append(func)
        return func