from typing import Callable, Optional
import rubigram


class Handler:
    def __init__(
        self,
        func: Callable,
        filters: Optional[str] = None,  # Filter Class
        group: Optional[int] = 1
    ):
        self.func = func
        self.filters = filters
        self.group = group

    async def runner(
        self,
        client,
        update: "rubigram.types.Update"
    ):
        if self.filters is None or await self.filters(update):
            await self.func(client, update)
            return True
        return False