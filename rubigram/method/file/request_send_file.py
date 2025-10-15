from typing import Optional
import rubigram


class RequestSendFile:
    async def request_send_file(
        self: "rubigram.Client",
        type: Optional[str] = "File"
    ) -> str:
        """Request a file upload URL from the server.

        This method asks the server to generate an upload URL for sending
        a file. The type of file can be specified.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            type (Optional[str], optional): Type of file. Defaults to "File".

        Returns:
            str: The upload URL to send the file.

        Example:
            >>> upload_url = await client.request_send_file()
            >>> print(upload_url)
        """
        data = {"type": type}
        response = await self.request("requestSendFile", data)
        return response["upload_url"]