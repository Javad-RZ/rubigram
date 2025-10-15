import rubigram


class EditChatKeypad:
    async def edit_chat_keypad(
        self: "rubigram.Client",
        chat_id: str,
        chat_keypad: "rubigram.types.Keypad"
    ):
        """
        Edit the keypad (custom button layout) of a chat.

        This method updates or replaces the current chat keypad
        (custom buttons) with a new layout.

        Args:
            chat_id (str): The unique identifier of the chat where the keypad should be updated.
            chat_keypad (rubigram.bot.types.Keypad): A `Keypad` object defining the new button layout.

        Returns:
            Any: The API response returned by the server.

        Example:
            >>> from rubigram.bot.types import Keypad, Button
            >>> keypad = Keypad(rows=[[Button(text="Menu"), Button(text="Help")]])
            >>> await client.edit_chat_keypad("chat123", keypad)
        """
        data = {
            "chat_id": chat_id,
            "chat_keypad_type": "New",
            "chat_keypad": chat_keypad.asdict()
        }

        return await self.request("editChatKeypad", data)