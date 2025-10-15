from typing import Optional
import rubigram


class EditMessage:
    async def edit_message(
        self: "rubigram.Client",
        chat_id: str,
        message_id: Optional[str] = None,
        text: Optional[str] = None,
        chat_keypad: Optional["rubigram.types.Keypad"] = None,
        inline_keypad: Optional["rubigram.types.Keypad"] = None
    ):
        """Edit various properties of a message.

        This method allows updating a message's text, chat keypad, or inline keypad.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): The unique identifier of the chat containing the message.
            message_id (Optional[str], optional): The unique identifier of the message to edit.
            text (Optional[str], optional): The new message text.
            chat_keypad (Optional[rubigram.types.Keypad], optional): A new chat keypad layout.
            inline_keypad (Optional[rubigram.types.Keypad], optional): A new inline keypad layout.

        Returns:
            None: This method does not return a response directly.

        Example:
            >>> from rubigram.types import Keypad, KeypadRow, Button
            >>> button = Button(id="101", button_text="rubigram")
            >>> row = KeypadRow(buttons=[button])
            >>> keypad = Keypad(rows=[row])
            >>> await client.edit_message("chat123", "msg456", text="Updated!", inline_keypad=keypad)
        """
        if text:
            await self.edit_message_text(chat_id, message_id, text)
        if chat_keypad:
            await self.edit_chat_keypad(chat_id, chat_keypad)
        if inline_keypad:
            await self.edit_message_keypad(chat_id, message_id, inline_keypad)