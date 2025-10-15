from typing import Union, Optional
from pathlib import Path
from aiohttp import FormData
import rubigram


class RequestUploadFile:
    async def request_upload_file(
        self: "rubigram.Client",
        upload_url: str,
        file: Union[str, bytes],
        name: Optional[str] = None
    ) -> str:
        """Upload a file and return its file ID.

        Supports local file paths, URLs, or raw bytes. If sending raw bytes,
        the `name` argument must be provided.

        Args:
            self (rubigram.Client): The active Rubigram client instance.
            upload_url (str): The URL to upload the file to (from `request_send_file`).
            file (Union[str, bytes]): File path, URL, or raw bytes.
            name (Optional[str], optional): File name for raw bytes or to override the default.

        Returns:
            str: The uploaded file's ID.

        Example:
            >>> file_id = await client.request_upload(
            >>>     upload_url="https://upload.rubigram.com",
            >>>     file="path/to/file.png"
            >>> )
            >>> print(file_id)
        """
        if isinstance(file, str):
            path = Path(file)
            if path.is_file():
                data, filename = path.read_bytes(), name or path.name
            elif file.startswith("http"):
                data = await self.get_bytes(file)
                filename = name or await self.get_file_name(file)
            else:
                raise FileNotFoundError("File not found : {}".format(file))
        elif isinstance(file, bytes):
            if not name:
                raise ValueError("A name must be provided for bytes file")
            data, filename = file, name
        else:
            raise TypeError("`file` must be a string path, URL, or bytes")

        form = FormData()
        form.add_field(
            "file",
            data,
            filename=filename,
            content_type="application/octet-stream"
        )

        async with self.http.session.post(upload_url, data=form) as response:
            response.raise_for_status()
            result = await response.json()
            return result.get("data", {}).get("file_id")