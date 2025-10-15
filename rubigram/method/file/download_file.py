from typing import Optional
import rubigram


class DownloadFile:
    async def download_file(
        self: "rubigram.Client",
        file_id: str,
        save_as: Optional[str] = None
    ) -> str:
        """Download a file by its file ID.

        Retrieves the file download URL from the server using the file ID,
        downloads the file, and saves it locally.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            file_id (str): The unique identifier of the file to download.
            save_as (Optional[str], optional): Custom filename or path to save the file as.
                If not provided, the original filename will be used. Defaults to None.

        Returns:
            str: The local path where the file was saved.

        Example:
            >>> path = await client.download_file(
            >>>     file_id="1234567890abcdef",
            >>>     save_as="downloads/photo.png"
            >>> )
            >>> print(f"File saved at: {path}")
        """
        download_url = await self.get_file(file_id)
        response = await self.request_download_file(download_url, save_as)
        return response