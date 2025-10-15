import rubigram


class EditMessageText:
    async def edit_message_text(
        self: "rubigram.Client",
        chat_id: str,
        message_id: str,
        text: str
    ):
        """Edit the text content of a message.

        This method changes the text of an existing message
        in a specific chat.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): The unique identifier of the chat containing the message.
            message_id (str): The unique identifier of the message to edit.
            text (str): The new text to replace the current message content.

        Returns:
            dict: The response returned by the server.

        Example:
            >>> response = await client.edit_message_text("chat_id", "message_id", "New message text")
            >>> print(response)
        """
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text
        }
        return await self.request("editMessageText", data)