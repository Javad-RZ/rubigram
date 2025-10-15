import rubigram


class RemoveChatKeypad:
    async def remove_chat_keypad(
        self: "rubigram.Client",
        chat_id: str
    ) -> dict:
        """Remove the chat keypad from a chat.

        This method removes the custom chat keypad from a specific chat.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): The unique identifier of the chat.

        Returns:
            dict: The response returned by the server.

        Example:
            >>> response = await client.remove_chat_keypad("chat_id")
            >>> print(response)
        """
        data = {
            "chat_id": chat_id,
            "chat_keypad_type": "Remove"
        }
        return await self.request("editChatKeypad", data)