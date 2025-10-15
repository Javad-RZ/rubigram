from typing import Optional
from dataclasses import dataclass
from .object import Object
from .types import *
import rubigram


@dataclass
class Update(Object):
    type: Optional[enums.UpdateType] = None
    chat_id: Optional[str] = None
    removed_message_id: Optional[str] = None
    new_message: Optional["rubigram.types.Message"] = None
    updated_message: Optional["rubigram.types.Message"] = None
    updated_payment: Optional["rubigram.types.PaymentStatus"] = None
    client: Optional["rubigram.Client"] = None

    async def reply(
        self,
        text: str,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: Optional[bool] = None,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with text and optional keypads.

        Args:
            text (str): The text of the reply message.
            chat_keypad (Optional[Keypad], optional): Keypad to show in the chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Inline keypad to show. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad. Defaults to None.
            disable_notification (Optional[bool], optional): If True, disables notification for the message. Defaults to None.

        Returns:
            rubigram.types.UMessage: The sent reply message object.

        Example:
            >>> reply_msg = await update.reply("Hello!", chat_keypad=my_keypad)
        """
        return await self.client.send_message(
            self.chat_id,
            text,
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification,
            self.new_message.message_id if self.new_message else None,
        )

    async def reply_poll(
        self,
        question: str,
        options: list[str],
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a poll.

        Args:
            question (str): The poll question text.
            options (list[str]): A list of options for the poll.
            chat_keypad (Optional[Keypad], optional): Keypad to show in the chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Inline keypad to show. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad. Defaults to None.
            disable_notification (bool, optional): If True, disables notification for the message. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent poll message object.

        Example:
            >>> poll_msg = await update.reply_poll(
            >>>     "What's your favorite color?",
            >>>     ["Red", "Blue", "Green"]
            >>> )
        """
        return await self.client.send_poll(
            self.chat_id,
            question,
            options,
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification,
            self.new_message.message_id if self.new_message else None,
        )

    async def reply_location(
        self,
        latitude: str,
        longitude: str,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a location.

        Args:
            latitude (str): Latitude of the location.
            longitude (str): Longitude of the location.
            chat_keypad (Optional[Keypad], optional): Keypad to show in chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Inline keypad to show. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad. Defaults to None.
            disable_notification (bool, optional): If True, disables notification. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent location message.

        Example:
            >>> await update.reply_location("35.6895", "139.6917")
        """
        return await self.client.send_location(
            self.chat_id,
            latitude,
            longitude,
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification,
            self.new_message.message_id if self.new_message else None,
        )

    async def reply_contact(
        self,
        first_name: str,
        last_name: str,
        phone_number: str,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a contact.

        Args:
            first_name (str): Contact's first name.
            last_name (str): Contact's last name.
            phone_number (str): Contact's phone number.
            chat_keypad (Optional[Keypad], optional): Keypad to show in chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Inline keypad to show. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad. Defaults to None.
            disable_notification (bool, optional): If True, disables notification. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent contact message.

        Example:
            >>> await update.reply_contact("John", "Doe", "+123456789")
        """
        return await self.client.send_contact(
            self.chat_id,
            first_name,
            last_name,
            phone_number,
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification,
            self.new_message.message_id if self.new_message else None,
        )

    async def reply_sticker(
        self,
        sticker_id: str,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a sticker.

        Args:
            sticker_id (str): The ID of the sticker to send.
            chat_keypad (Optional[Keypad], optional): Keypad to show in chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Inline keypad to show. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad. Defaults to None.
            disable_notification (bool, optional): If True, disables notification. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent sticker message.

        Example:
            >>> await update.reply_sticker("CAADAgADQAADyIsGAAE7MpzFPFQXkQI")
        """
        return await self.client.send_message(
            self.chat_id,
            sticker_id,
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification,
            self.new_message.message_id if self.new_message else None,
        )

    async def reply_file(
        self,
        file: Union[str, bytes],
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        type: Optional[Union[str, enums.FileType]] = enums.FileType.File,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a file.

        Args:
            file (Union[str, bytes]): The file path or binary data to send.
            caption (Optional[str], optional): Caption for the file. Defaults to None.
            file_name (Optional[str], optional): Custom filename for the file. Defaults to None.
            type (enums.FileType, optional): Type of the file (File, Document, etc.). Defaults to File.
            chat_keypad (Optional[Keypad], optional): Keypad to show in chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Inline keypad to show. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad. Defaults to None.
            disable_notification (bool, optional): If True, disables notification. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent file message.

        Example:
            >>> await update.reply_file("example.pdf", caption="Here is your file")
        """
        return await self.client.send_file(
            self.chat_id,
            file,
            caption,
            file_name,
            type,
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification,
            self.new_message.message_id if self.new_message else None,
        )

    async def reply_document(
        self,
        document: Union[str, bytes],
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a document file.

        This method sends a document as a reply to the current message, optionally with a caption,
        custom file name, chat or inline keypads, chat keypad type, and notification control.

        Args:
            document (Union[str, bytes]): The path or bytes of the document to send.
            caption (Optional[str], optional): Text caption for the document. Defaults to None.
            file_name (Optional[str], optional): Custom name for the file. Defaults to None.
            type (Optional[Union[str, enums.FileType]], optional): The type of the file. Defaults to enums.FileType.Document.
            chat_keypad (Optional[Keypad], optional): Keypad to attach to the chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Keypad to attach inline. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad if applicable. Defaults to None.
            disable_notification (bool, optional): If True, disables notification for this message. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent reply message object.

        Example:
            >>> await update.reply_document(
            >>>     document="example.pdf",
            >>>     caption="Here is the file",
            >>>     chat_keypad=keypad
            >>> )
        """
        return await self.reply_file(
            document,
            caption,
            file_name,
            "File",
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification
        )

    async def reply_photo(
        self,
        photo: Union[str, bytes],
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a photo.

        This method sends a photo as a reply to the current message, optionally with a caption,
        custom file name, chat or inline keypads, chat keypad type, and notification control.

        Args:
            photo (Union[str, bytes]): The path or bytes of the photo to send.
            caption (Optional[str], optional): Text caption for the photo. Defaults to None.
            file_name (Optional[str], optional): Custom name for the file. Defaults to None.
            chat_keypad (Optional[Keypad], optional): Keypad to attach to the chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Keypad to attach inline. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad if applicable. Defaults to None.
            disable_notification (bool, optional): If True, disables notification for this message. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent reply message object.

        Example:
            >>> await update.reply_photo(
            >>>     photo="example.jpg",
            >>>     caption="Here is the photo",
            >>>     chat_keypad=keypad
            >>> )
        """
        return await self.reply_file(
            photo,
            caption,
            file_name,
            "Image",
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification
        )

    async def reply_video(
        self,
        video: Union[str, bytes],
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a video file.

        This method sends a video as a reply to the current message, optionally with a caption,
        custom file name, chat or inline keypads, chat keypad type, and notification control.

        Args:
            video (Union[str, bytes]): The path or bytes of the video to send.
            caption (Optional[str], optional): Text caption for the video. Defaults to None.
            file_name (Optional[str], optional): Custom name for the file. Defaults to None.
            chat_keypad (Optional[Keypad], optional): Keypad to attach to the chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Keypad to attach inline. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad if applicable. Defaults to None.
            disable_notification (bool, optional): If True, disables notification for this message. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent reply message object.

        Example:
            >>> await update.reply_video(
            >>>     video="example.mp4",
            >>>     caption="Here is the video",
            >>>     chat_keypad=keypad
            >>> )
        """
        return await self.reply_file(
            video,
            caption,
            file_name,
            "Video",
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification
        )

    async def reply_gif(
        self,
        gif: Union[str, bytes],
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a GIF file.

        This method sends a GIF as a reply to the current message, optionally with a caption,
        custom file name, chat or inline keypads, chat keypad type, and notification control.

        Args:
            gif (Union[str, bytes]): The path or bytes of the GIF to send.
            caption (Optional[str], optional): Text caption for the GIF. Defaults to None.
            file_name (Optional[str], optional): Custom name for the file. Defaults to None.
            chat_keypad (Optional[Keypad], optional): Keypad to attach to the chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Keypad to attach inline. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad if applicable. Defaults to None.
            disable_notification (bool, optional): If True, disables notification for this message. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent reply message object.

        Example:
            >>> await update.reply_gif(
            >>>     gif="funny.gif",
            >>>     caption="Check out this GIF!",
            >>>     chat_keypad=keypad
            >>> )
        """
        return await self.reply_file(
            gif,
            caption,
            file_name,
            "Gif",
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification
        )

    async def reply_music(
        self,
        music: Union[str, bytes],
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a music/audio file.

        This method sends a music/audio file as a reply to the current message, optionally with a caption,
        custom file name, chat or inline keypads, chat keypad type, and notification control.

        Args:
            music (Union[str, bytes]): The path or bytes of the music file to send.
            caption (Optional[str], optional): Text caption for the music. Defaults to None.
            file_name (Optional[str], optional): Custom name for the file. Defaults to None.
            chat_keypad (Optional[Keypad], optional): Keypad to attach to the chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Keypad to attach inline. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad if applicable. Defaults to None.
            disable_notification (bool, optional): If True, disables notification for this message. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent reply message object.

        Example:
            >>> await update.reply_music(
            >>>     music="song.mp3",
            >>>     caption="Listen to this!",
            >>>     chat_keypad=keypad
            >>> )
        """
        return await self.reply_file(
            music,
            caption,
            file_name,
            "Music",
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification
        )

    async def reply_voice(
        self,
        voice: Union[str, bytes],
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        chat_keypad_type: Optional[enums.ChatKeypadType] = None,
        disable_notification: bool = False,
    ) -> "rubigram.types.UMessage":
        """Reply to the current message with a voice note.

        This method sends a voice message as a reply to the current message, optionally with a caption,
        custom file name, chat or inline keypads, chat keypad type, and notification control.

        Args:
            voice (Union[str, bytes]): The path or bytes of the voice file to send.
            caption (Optional[str], optional): Text caption for the voice message. Defaults to None.
            file_name (Optional[str], optional): Custom name for the file. Defaults to None.
            chat_keypad (Optional[Keypad], optional): Keypad to attach to the chat. Defaults to None.
            inline_keypad (Optional[Keypad], optional): Keypad to attach inline. Defaults to None.
            chat_keypad_type (Optional[enums.ChatKeypadType], optional): Type of chat keypad if applicable. Defaults to None.
            disable_notification (bool, optional): If True, disables notification for this message. Defaults to False.

        Returns:
            rubigram.types.UMessage: The sent reply message object.

        Example:
            >>> await update.reply_voice(
            >>>     voice="voice.ogg",
            >>>     caption="Listen to this voice note!",
            >>>     chat_keypad=keypad
            >>> )
        """
        return await self.reply_file(
            voice,
            caption,
            file_name,
            "Voice",
            chat_keypad,
            inline_keypad,
            chat_keypad_type,
            disable_notification
        )

    async def download(
        self,
        save_as: str
    ) -> str:
        """Download the file attached to the current message.

        This method downloads the file associated with the message (if any) 
        and saves it locally with the specified file name.

        Args:
            file_name (str): The name (including path if needed) to save the downloaded file as.

        Returns:
            str: The path to the downloaded file.

        Example:
            >>> await update.download("my_file.pdf")
        """
        return await self.client.download_file(
            self.new_message.file.file_id,
            save_as
        )

    async def forward(
        self,
        chat_id: str
    ) -> "rubigram.types.UMessage":
        """Forward the current message to another chat.

        This method forwards the message represented by this update to the specified chat ID.

        Args:
            chat_id (str): The target chat ID to forward the message to.

        Returns:
            rubigram.types.UMessage: The forwarded message object in the target chat.

        Example:
            >>> await update.forward("g0123456789")
        """
        return await self.client.forward_message(
            self.chat_id,
            self.new_message.message_id,
            chat_id
        )


@dataclass
class Updates(Object):
    updates: Optional[list["rubigram.types.Update"]] = None
    next_offset_id: Optional[str] = None

    @classmethod
    def parse(cls, data: dict):
        data = data or {}
        updates = [
            rubigram.types.Update.parse(update) if isinstance(update, dict) else update for update in data.get("updates", []) or []
        ]
        return cls(
            updates=updates,
            next_offset_id=data.get("next_offset_id")
        )