from typing import Union
import asyncio
import rubigram


class DeleteMessage:
    async def delete_message(
        self: "rubigram.Client",
        chat_id: str,
        message_id: Union[str, list[str]]
    ):
        """Delete one or more messages from a chat.

        This method deletes a single message or multiple messages
        from a specific chat.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): The unique identifier of the chat.
            message_id (Union[str, list[str]]): A message ID or list of message IDs to delete.

        Returns:
            Any: API response for a single message, or the number of deletions for multiple messages.

        Example:
            >>> await client.delete_message("chat_id", "msg_id")
            >>> await client.delete_message("chat_id", ["msg1", "msg2"])
        """
        if isinstance(message_id, str):
            return await self.request(
                "deleteMessage",
                {
                    "chat_id": chat_id,
                    "message_id": message_id
                }
            )

        tasks = [
            self.request(
                "deleteMessage",
                {
                    "chat_id": chat_id,
                    "message_id": i
                }
            )
            for i in message_id
        ]

        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return len(responses)