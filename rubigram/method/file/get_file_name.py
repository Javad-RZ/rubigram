import os
from urllib.parse import urlparse
import rubigram


class GetFileName:
    async def get_file_name(
        self: "rubigram.Client",
        url: str
    ) -> str:
        """Extract the file name from a given URL.

        This method parses the URL and returns the last path component,
        which usually corresponds to the file name.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            url (str): The URL to parse.

        Returns:
            str: The file name extracted from the URL.

        Example:
            >>> file_name = await client.get_file_name("https://example.com/path/to/file.png")
            >>> print(file_name)
            file.png
        """
        parser = urlparse(url)
        return os.path.basename(parser.path)