from typing import Optional
from rubigram.filters import Filter
import rubigram


class OnDeleteMessage:
    def on_delete_message(
        self: "rubigram.Client",
        filters: Optional["Filter"] = None,
        group: int = 0
    ):
        """Register a handler for deleted messages.

        This decorator allows you to handle events where a message has been removed
        from a chat (either by the sender, admin, or system). The handler function
        will be called whenever a `RemovedMessage` update is received.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            filters (Optional[Filter], optional): A filter or combined filters to restrict
                which deleted messages trigger the handler. Defaults to None.
            group (int, optional): Execution priority for this handler. Handlers with
                lower group values are executed first. Defaults to 0.

        Returns:
            Callable: A decorator that registers the function as a delete-message handler.

        Example:
            >>> @app.on_delete_message()
            >>> async def on_delete(client, update):
            >>>     print(f"Message deleted in chat: {update.chat_id}")
        """
        return self.register_handler(
            self.handlers["delete"],
            filters,
            group
        )