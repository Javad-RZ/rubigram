import rubigram


class GetMe:
    async def get_me(self: "rubigram.Client") -> "rubigram.types.Bot":
        """Get information about the current bot.

        Sends a `getMe` request to the Rubigram API and retrieves
        detailed information about the bot associated with the current token.

        Returns:
            rubigram.types.Bot: The bot information object containing attributes
            such as bot ID, name, username, and creation date.

        Example:
            >>> bot = await client.get_me()
            >>> print(bot.id)
            >>> print(bot.name)
            >>> print(bot.username)
        """
        response = await self.request("getMe")
        return rubigram.types.Bot(response["bot"])