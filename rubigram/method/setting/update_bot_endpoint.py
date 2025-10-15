from typing import Optional, Union
import rubigram


class UpdateBotEndpoints:
    async def update_bot_endpoints(
        self: "rubigram.Client",
        url: str,
        type: Optional[Union[str, "rubigram.enums.UpdateEndpointType"]] = "ReceiveUpdate"
    ) -> dict:
        """ Set the endpoint URL for receiving updates.

        Args:
            self (rubigram.Client): ...
            url (str): your endpoint url
            type (Optional[Union[str, rubigram.enums.UpdateEndpointType]], optional):
            type of endpoint Defaults to "ReceiveUpdate".

        Returns:
            dict: response server

        Example:
            >>> response = await client.update_bot_endpoints("https://rubigram.bot.com")
            >>> print(response)
        """
        data = {
            "url": url,
            "type": type
        }
        response = await self.client.request("updateBotEndpoints", data)
        return response