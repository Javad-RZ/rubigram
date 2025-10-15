import rubigram


class GetFile:
    async def get_file(
        self: "rubigram.Client",
        file_id: str
    ) -> str:
        """Get the download URL of a file.

        This method retrieves the direct download URL of a file
        previously uploaded or sent via Rubigram.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            file_id (str): The unique identifier of the file.

        Returns:
            str: The download URL of the file.

        Example:
            >>> download_url = await client.get_file("file_id")
            >>> print(download_url)
        """
        data = {"file_id": file_id}
        response = await self.request("getFile", data)
        return response["download_url"]