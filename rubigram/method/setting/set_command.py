import rubigram


class SetCommands:
    async def set_commands(
        self: "rubigram.Client",
        commands: list["rubigram.types.BotCommand"]
    ) -> dict:
        """Set the command for bot.

        Args:
            self (rubigram.Client): ...
            commands (list[rubigram.types.BotCommand]): ...

        Returns:
            dict: response server

        Example:
            >>> commands = [
            >>>     rubigram.types.BotCommand(command="start", description="Start the bot"),
            >>>     rubigram.types.BotCommand(command="help", description="Show help")
            >>> ]
            >>> response = await client.set_commands(commands)
            >>> print(response)
        """

        data = {
            "bot_commands": [command.asdict() for command in commands]
        }

        response = await self.request("setCommands", data)
        return response