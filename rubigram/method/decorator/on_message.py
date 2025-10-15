from typing import Optional
from rubigram.filters import Filter
import rubigram


class OnMessage:
    def on_message(
        self: "rubigram.Client",
        filters: Optional["Filter"] = None,
        group: int = 0
    ):
        """Register a handler for new incoming messages.

        This decorator allows you to listen for new message updates that match
        the provided filters. Handlers are executed in order based on their group priority.

        Args:
            self (rubigram.Client): The Rubigram client instance.
            filters (Optional[Filter], optional): A filter or combination of filters
                that determine which messages trigger this handler. Defaults to None.
            group (int, optional): The handler execution priority.
                Lower values run first. Defaults to 0.

        Returns:
            Callable: A decorator used to register the function as a message handler.

        Example:
            >>> from rubigram import filters
            >>>
            >>> @app.on_message(filters.text)
            >>> async def handle_text(client, update):
            >>>     await client.send_message(update.chat_id, "Received a text message!")
        """
        return self.register_handler(
            self.handlers["message"],
            filters,
            group
        )