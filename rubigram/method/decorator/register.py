from typing import Optional, Callable
from rubigram.filters import Filter
from ...handler import Handler
import rubigram


class Register:
    def register_handler(
        self: "rubigram.Client",
        handlers: list["Handler"],
        filters: Optional["Filter"] = None,
        group: int = 0
    ) -> Callable:
        """Register an event handler with optional filters and group priority.

        This method is used internally by decorators such as
        `on_message`, `on_inline`, and similar ones to attach a function
        as an event handler. It wraps the given function inside a `Handler`
        object and stores it in the appropriate handler list.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            handlers (List[Handler]): The list where the handler should be registered.
            filters (Optional[Filter], optional): A filter or filter group to
                restrict which updates trigger the handler. Defaults to None.
            group (int, optional): The handler's execution priority.
                Lower values are executed first. Defaults to 0.

        Returns:
            Callable: A decorator that registers the provided function as a handler.

        Example:
            >>> @app.on_message(filters.text)
            >>> async def handle_text(client, update):
            >>>     await client.send_message(update.chat_id, "Received text!")
        """
        def decorator(func: Callable):
            handler = Handler(func, filters, group)
            handlers.append(handler)
            handlers.sort(key=lambda x: x.group)
            return func

        return decorator