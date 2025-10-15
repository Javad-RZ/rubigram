import rubigram


class Updater:
    async def updater(
        self: "rubigram.Client",
        data: dict
    ):
        if "inline_message" in data:
            event = rubigram.types.InlineMessage.parse(data["inline_message"])
        elif "update" in data:
            event = rubigram.types.Update.parse(data["update"])
        else:
            return

        event.client = self
        await self.dispatch(event)