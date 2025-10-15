from typing import Optional, Union
import rubigram


class SendFile:
    async def send_file(
        self: "rubigram.Client",
        chat_id: str,
        file: Union[str, bytes],
        caption: Optional[str] = None,
        filename: Optional[str] = None,
        type: Optional[Union[str, "rubigram.enums.FileType"]] = "File",
        chat_keypad: Optional["rubigram.types.Keypad"] = None,
        inline_keypad: Optional["rubigram.types.Keypad"] = None,
        chat_keypad_type: Optional["rubigram.enums.ChatKeypadType"] = None,
        disable_notification: Optional[bool] = False,
        reply_to_message_id: Optional[str] = None
    ) -> "rubigram.types.UMessage":
        """Send a file to a chat.

        Uploads a file (local path, URL, or raw bytes) and sends it to the specified chat,
        optionally with caption, keypads, or as a reply.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): The ID of the chat to send the file to.
            file (Union[str, bytes]): File path, URL, or raw bytes to send.
            caption (Optional[str], optional): Text caption for the file. Defaults to None.
            filename (Optional[str], optional): Filename to use for raw bytes. Defaults to None.
            type (Optional[Union[str, rubigram.enums.FileType]], optional): Type of file. Defaults to "File".
            chat_keypad (Optional[rubigram.types.Keypad], optional): Chat keypad to include. Defaults to None.
            inline_keypad (Optional[rubigram.types.Keypad], optional): Inline keypad to include. Defaults to None.
            chat_keypad_type (Optional[rubigram.enums.ChatKeypadType], optional): Chat keypad type. Defaults to None.
            disable_notification (Optional[bool], optional): Whether to disable notifications. Defaults to False.
            reply_to_message_id (Optional[str], optional): ID of message to reply to. Defaults to None.

        Returns:
            rubigram.types.UMessage: The sent message object containing message ID, file ID, and chat ID.

        Example:
            >>> message = await client.send_file(
            >>>     chat_id="chat_id",
            >>>     file="path/to/file.png",
            >>>     caption="Hello!",
            >>> )
            >>> print(message.message_id)
            >>> print(message.file_id)
        """
        upload_url = await self.request_send_file(type)
        file_id = await self.request_upload_file(upload_url, file, filename)

        data = {
            "chat_id": chat_id,
            "file_id": file_id,
            "text": caption
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

        response = await self.request("sendFile", data)
        message = rubigram.types.UMessage.parse(response)
        message.chat_id = chat_id
        message.file_id = file_id
        message.client = self
        return message