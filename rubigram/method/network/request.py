from typing import Optional
import rubigram


class Request:
    def __init__(self, client: "rubigram.Client"):
        self.client = client
        self.api: str = f"https://botapi.rubika.ir/v3/{client.token}/"

    async def request(
        self,
        method: str,
        data: Optional[dict] = {}
    ) -> dict:

        url = self.api + method
        async with self.client.http.session.post(url, json=data) as response:
            response.raise_for_status()
            res: dict = await response.json()
            return res.get("data")