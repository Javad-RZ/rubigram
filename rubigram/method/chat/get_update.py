from typing import Optional
import rubigram


class GetUpdates:
    async def get_updates(
        self: "rubigram.Client",
        limit: Optional[int] = 1,
        offset_id: Optional[str] = None
    ) -> "rubigram.types.Updates":
        """Get new updates for the bot (messages, events, etc.).

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            limit (Optional[int], optional): Maximum number of updates to retrieve. Defaults to 1.
            offset_id (Optional[str], optional): Identifier of the last processed update to skip older ones. Defaults to None.

        Returns:
            rubigram.types.Updates: A parsed object containing a list of updates received from the server.

        Example:
            >>> updates = await client.get_updates(limit=5)
            >>> for update in updates.updates:
            >>>     print(update.new_message.text)
        """
        data = {
            "limit": limit,
            "offset_id": offset_id
        }

        response = await self.request("getUpdates", data)
        return rubigram.types.Updates.parse(response)