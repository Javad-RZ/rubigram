from typing import Optional
from rubigram.filters import Filter
import rubigram


class OnInlineMessage:
    def on_inline_message(
        self: "rubigram.Client",
        filters: Optional["Filter"] = None,
        group: int = 0
    ):
        """Register a handler for inline message updates.

        This decorator registers a callback function that will be called
        whenever an inline message update is received by the client.

        Args:
            self (rubigram.Client): The Rubigram client instance.
            filters (Optional[Filter], optional): Filter(s) to restrict which updates
                should trigger the callback. Defaults to None.
            group (int, optional): Determines the order in which multiple handlers
                are executed. Lower numbers are executed first. Defaults to 0.

        Returns:
            Callable: A decorator that registers the provided function as a handler.

        Example:
            >>> from rubigram import Client, filters
            >>>
            >>> app = Client("TOKEN")
            >>>
            >>> @app.on_inline_message(filters.button("click_me"))
            >>> async def handle_inline(client, inline):
            >>>     await client.send_message(inline.chat_id, "Button clicked!")
        """
        return self.register_handler(
            self.handlers["inline"],
            filters,
            group
        )