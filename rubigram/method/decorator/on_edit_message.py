from typing import Optional
from rubigram.filters import Filter
import rubigram


class OnEditMessage:
    def on_edit_message(
        self: "rubigram.Client",
        filters: Optional["Filter"] = None,
        group: int = 0
    ):
        """Register a handler for edited messages.

        This decorator allows you to handle updates where an existing message
        in a chat has been edited. The handler function will be triggered whenever
        an `UpdatedMessage` event is received.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            filters (Optional[Filter], optional): A filter or combination of filters to limit
                which edited messages should trigger the handler. Defaults to None.
            group (int, optional): Execution priority for this handler. Handlers with
                smaller group values run first. Defaults to 0.

        Returns:
            Callable: A decorator that registers the function as an edit-message handler.

        Example:
            >>> @app.on_edit_message()
            >>> async def on_edit(client, update):
            >>>     await client.send_message(update.chat_id, "A message was edited!")
        """
        return self.register_handler(
            self.handlers["edit"],
            filters,
            group
        )