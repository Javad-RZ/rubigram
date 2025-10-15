import rubigram

class GetBytes:
    async def get_bytes(
        self: "rubigram.Client",
        url: str
    ) -> bytes:
        """Fetch raw bytes from a given URL.

        Performs an HTTP GET request and returns the response content as bytes.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            url (str): The URL to fetch.

        Returns:
            bytes: The raw content of the response.

        Example:
            >>> data = await client.get_bytes("https://rubigram.com/file.png")
            >>> print(len(data))
        """
        async with self.http.session.get(url) as response:
            response.raise_for_status()
            return await response.read()