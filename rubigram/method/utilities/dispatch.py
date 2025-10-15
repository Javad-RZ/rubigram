from typing import Union
import rubigram


class Dispatch:
    async def dispatch(
        self: "rubigram.Client",
        update: Union[
            "rubigram.types.Update",
            "rubigram.types.InlineMessage"
        ]
    ):
        if isinstance(update, rubigram.types.InlineMessage):
            event_type = "inline"
        else:
            match update.type:
                case "NewMessage": event_type = "message"
                case "UpdatedMessage": event_type = "edit"
                case "RemovedMessage": event_type = "delete"
                case other:
                    return

        for handler in self.handlers[event_type]:
            if handler.filters is None or await handler.filters(update):
                await handler.func(self, update)