from typing import Optional, Union
import rubigram


class SendGif:
    async def send_gif(
        self: "rubigram.Client",
        chat_id: str,
        document: Union[str, bytes],
        caption: Optional[str] = None,
        filename: Optional[str] = None,
        chat_keypad: Optional["rubigram.types.Keypad"] = None,
        inline_keypad: Optional["rubigram.types.Keypad"] = None,
        chat_keypad_type: Optional["rubigram.enums.ChatKeypadType"] = None,
        disable_notification: Optional[bool] = False,
        reply_to_message_id: Optional[str] = None
    ) -> "rubigram.types.UMessage":
        """Send a GIF file to a chat.

        This is a wrapper around `send_file` to specifically send GIFs.
        Supports local files, URLs, or raw bytes.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): The ID of the chat to send the GIF to.
            document (Union[str, bytes]): Local path, URL, or raw bytes of the GIF.
            caption (Optional[str], optional): Text caption for the GIF. Defaults to None.
            filename (Optional[str], optional): Filename to use for raw bytes. Defaults to None.
            chat_keypad (Optional[rubigram.types.Keypad], optional): Chat keypad to include. Defaults to None.
            inline_keypad (Optional[rubigram.types.Keypad], optional): Inline keypad to include. Defaults to None.
            chat_keypad_type (Optional[rubigram.enums.ChatKeypadType], optional): Chat keypad type. Defaults to None.
            disable_notification (Optional[bool], optional): Whether to disable notifications. Defaults to False.
            reply_to_message_id (Optional[str], optional): ID of message to reply to. Defaults to None.

        Returns:
            rubigram.types.UMessage: The sent message object containing message ID, file ID, and chat ID.

        Example:
            >>> message = await client.send_gif(
            >>>     chat_id="chat_id",
            >>>     document="path/to/animation.gif",
            >>>     caption="Funny GIF"
            >>> )
            >>> print(message.message_id)
            >>> print(message.file_id)
        """
        return await self.send_file(
            chat_id=chat_id,
            file=document,
            caption=caption,
            filename=filename,
            type="Gif",
            chat_keypad=chat_keypad,
            inline_keypad=inline_keypad,
            chat_keypad_type=chat_keypad_type,
            disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id
        )