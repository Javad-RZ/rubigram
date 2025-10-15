from typing import Optional
from dataclasses import dataclass
from .object import Object
from .types import *
import rubigram


@dataclass
class Message(Object):
    message_id: Optional[str] = None
    text: Optional[str] = None
    time: Optional[str] = None
    is_edited: Optional[bool] = None
    sender_type: Optional[enums.MessageSender] = None
    sender_id: Optional[str] = None
    aux_data: Optional[AuxData] = None
    file: Optional[File] = None
    reply_to_message_id: Optional[str] = None
    forwarded_from: Optional[ForwardedFrom] = None
    forwarded_no_link: Optional[str] = None
    location: Optional[Location] = None
    sticker: Optional[Sticker] = None
    contact_message: Optional[ContactMessage] = None
    poll: Optional[Poll] = None
    live_location: Optional[LiveLocation] = None
    client: Optional["rubigram.Client"] = None


@dataclass
class InlineMessage(Object):
    sender_id: Optional[str] = None
    text: Optional[str] = None
    message_id: Optional[str] = None
    chat_id: Optional[str] = None
    file: Optional[File] = None
    location: Optional[Location] = None
    aux_data: Optional[AuxData] = None
    client: Optional["rubigram.Client"] = None


@dataclass
class UMessage(Object):
    message_id: Optional[str] = None
    file_id: Optional[str] = None
    chat_id: Optional[str] = None
    client: Optional["rubigram.Client"] = None

    async def delete(self):
        """Delete this message from the chat.

        Sends a request to Rubigram to remove the message identified
        by this object's `message_id` from its chat.

        Args:
            self (UMessage): The message instance to be deleted.

        Returns:
            bool: True if the message was successfully deleted, False otherwise.

        Example:
            >>> message = await client.send_message(chat_id="b0X123", text="Hello!")
            >>> await message.delete()
        """
        return await self.client.delete_message(
            self.chat_id, self.message_id
        )

    async def edit(
        self,
        text: Optional[str] = None,
        inline: Optional[Keypad] = None,
        keypad: Optional[Keypad] = None
    ):
        """Edit this message's content, inline keyboard, or chat keypad.

        This method allows modifying the text, inline keyboard, or chat keypad
        of the current message. You can use any combination of parameters to
        update different parts of the message.

        Args:
            self (UMessage): The message instance to edit.
            text (Optional[str], optional): New text content for the message. Defaults to None.
            inline (Optional[Keypad], optional): Inline keyboard to attach to the message. Defaults to None.
            keypad (Optional[Keypad], optional): Chat keypad to attach to the message. Defaults to None.

        Returns:
            None

        Example:
            >>> message = await client.send_message(chat_id="b0X123", text="Hello!")
            >>> await message.edit(text="Updated text")
            >>> await message.edit(inline=my_inline_keypad)
            >>> await message.edit(keypad=my_chat_keypad)
        """
        if text:
            await self.edit_text(text)
        if inline:
            await self.edit_inline(inline)
        if keypad:
            await self.edit_keypad(keypad)

    async def edit_text(self, text: str):
        """Edit the text content of this message.

        Args:
            self (UMessage): The message instance to edit.
            text (str): New text to replace the current message content.

        Returns:
            UMessage: The updated message object returned by the client.

        Example:
            >>> await message.edit_text("Updated text content")
        """
        return await self.client.edit_message_text(
            self.chat_id,
            self.message_id,
            text
        )

    async def edit_inline(self, inline: Keypad):
        """Edit the inline keyboard of this message.

        Args:
            self (UMessage): The message instance to edit.
            inline (Keypad): New inline keyboard to attach to the message.

        Returns:
            UMessage: The updated message object returned by the client.

        Example:
            >>> await message.edit_inline(my_inline_keypad)
        """
        return await self.client.edit_message_keypad(
            self.chat_id,
            self.message_id,
            inline
        )

    async def edit_keypad(self, keypad: Keypad):
        """Edit the chat keypad for this message's chat.

        Args:
            self (UMessage): The message instance whose chat keypad will be edited.
            keypad (Keypad): New chat keypad to attach.

        Returns:
            UMessage: The updated message object returned by the client.

        Example:
            >>> await message.edit_keypad(my_chat_keypad)
        """
        return await self.client.edit_chat_keypad(
            self.chat_id,
            keypad
        )

    async def forward(self, chat_id: str):
        """Forward this message to another chat.

        Args:
            self (UMessage): The message instance to forward.
            chat_id (str): ID of the chat to forward the message to.

        Returns:
            UMessage: The forwarded message object returned by the client.

        Example:
            >>> await message.forward("b0AnotherChat")
        """
        return await self.client.forward_message(
            self.chat_id,
            self.message_id,
            chat_id
        )