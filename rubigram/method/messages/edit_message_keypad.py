import rubigram


class EditMessageKeypad:
    async def edit_message_keypad(
        self: "rubigram.Client",
        chat_id: str,
        message_id: str,
        inline_keypad: "rubigram.types.Keypad"
    ):
        """Edit the inline keypad (buttons) of a message.

        This method updates the inline keypad of a specific message
        in a chat with a new button layout.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): The unique identifier of the chat containing the message.
            message_id (str): The unique identifier of the message to update.
            inline_keypad (rubigram.types.Keypad): A `Keypad` object defining the new inline buttons.

        Returns:
            dict: The response returned by the server.

        Example:
            >>> from rubigram.types import Keypad, KeypadRow, Button
            >>> button = Button(id="101", button_text="rubigram")
            >>> row = KeypadRow(buttons=[button])
            >>> keypad = Keypad(rows=[row])
            >>> response = await client.edit_message_keypad("chat_id", "message_id", keypad)
            >>> print(response)
        """
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_keypad": inline_keypad.asdict()
        }
        return await self.request("editMessageKeypad", data)