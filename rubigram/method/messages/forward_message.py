from typing import Optional
import rubigram


class ForwardMessage:
    async def forward_message(
        self: "rubigram.Client",
        from_chat_id: str,
        message_id: str,
        to_chat_id: str,
        disable_notification: Optional[bool] = False
    ) -> "rubigram.types.UMessage":
        """Forward a message from one chat to another.

        This method forwards a specific message from a source chat
        to a target chat, optionally disabling notifications.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            from_chat_id (str): The unique identifier of the chat to forward the message from.
            message_id (str): The unique identifier of the message to forward.
            to_chat_id (str): The unique identifier of the chat to forward the message to.
            disable_notification (Optional[bool], optional): Whether to disable notifications for the forwarded message. Defaults to False.

        Returns:
            rubigram.types.UMessage: The forwarded message object.

        Example:
            >>> message = await client.forward_message("from_chat_id", "message_id", "to_chat_id")
            >>> print(message.message_id)
        """
        data = {
            "from_chat_id": from_chat_id,
            "message_id": message_id,
            "to_chat_id": to_chat_id,
            "disable_notification": disable_notification
        }
        
        response = await self.request("forwardMessage", data)
        message = rubigram.types.UMessage.parse(response)
        message.chat_id = to_chat_id
        message.client = self
        return message