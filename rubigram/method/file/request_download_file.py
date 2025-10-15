from typing import Optional
import aiofiles
import rubigram

class RequestDownloadFile:
    async def request_download_file(
        self: "rubigram.Client",
        url: str,
        filename: Optional[str] = None
    ) -> str:
        """Download a file from a URL and save it locally.

        If `filename` is not provided, the name is extracted from the URL.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            url (str): The URL of the file to download.
            filename (Optional[str], optional): Local file name to save as.

        Returns:
            str: The path of the saved file.

        Example:
            >>> saved_file = await client.request_download(
            >>>     "https://example.com/file.png"
            >>> )
            >>> print(saved_file)
        """
        file_bytes = await self.get_bytes(url)
        file_name = filename or await self.get_file_name(url)

        async with aiofiles.open(file_name, "wb") as f:
            await f.write(file_bytes)

        return file_name