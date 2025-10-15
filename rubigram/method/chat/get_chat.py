import rubigram


class GetChat:
    async def get_chat(
        self: "rubigram.Client",
        chat_id: str
    ) -> "rubigram.types.Chat":
        """Get information about a chat.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            chat_id (str): Unique identifier of the chat to get information about.

        Returns:
            rubigram.types.Chat: An object containing chat information.

        Example:
            >>> chat = await client.get_chat("u0f1a2b3c4d5e6")
            >>> print(chat.chat_id, chat.title)
        """
        data = {
            "chat_id": chat_id
        }
        response = await self.request("getChat", data)
        return rubigram.types.Chat.parse(response["chat"])