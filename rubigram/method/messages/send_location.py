from typing import Optional
import rubigram


class SendLocation:
    async def send_location(
        self: "rubigram.Client",
        chat_id: str,
        latitude: str,
        longitude: str,
        chat_keypad: Optional["rubigram.types.Keypad"] = None,
        inline_keypad: Optional["rubigram.types.Keypad"] = None,
        chat_keypad_type: Optional["rubigram.enums.ChatKeypadType"] = None,
        disable_notification: Optional[bool] = False,
        reply_to_message_id: Optional[str] = None
    ) -> "rubigram.types.UMessage":
        """Send a location to a chat.

        This method sends geographic coordinates to a specific chat,
        with optional chat or inline keypads and notification settings.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): The unique identifier of the target chat.
            latitude (str): Latitude of the location.
            longitude (str): Longitude of the location.
            chat_keypad (Optional[rubigram.types.Keypad], optional): Custom chat keypad. Defaults to None.
            inline_keypad (Optional[rubigram.types.Keypad], optional): Inline keypad. Defaults to None.
            chat_keypad_type (Optional[rubigram.enums.ChatKeypadType], optional): Type of chat keypad. Defaults to None.
            disable_notification (Optional[bool], optional): Whether to disable notifications. Defaults to False.
            reply_to_message_id (Optional[str], optional): Reply to a specific message ID. Defaults to None.

        Returns:
            rubigram.types.UMessage: The sent message object.

        Example:
            >>> from rubigram.types import Keypad, KeypadRow, Button
            >>> button = Button(id="101", button_text="rubigram")
            >>> row = KeypadRow(buttons=[button])
            >>> keypad = Keypad(rows=[row])
            >>> message = await client.send_location(
            ...     "chat_id",
            ...     "35.6895",
            ...     "139.6917",
            ...     inline_keypad=keypad
            ... )
            >>> print(message.message_id)
        """
        data = {
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude
        }

        if chat_keypad:
            data["chat_keypad"] = chat_keypad.asdict()
        if inline_keypad:
            data["inline_keypad"] = inline_keypad.asdict()
        if chat_keypad_type:
            data["chat_keypad_type"] = chat_keypad_type
        if disable_notification:
            data["disable_notification"] = disable_notification
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id

        response = await self.request("sendLocation", data)
        message = rubigram.types.UMessage.parse(response)
        message.chat_id = chat_id
        message.client = self
        return message