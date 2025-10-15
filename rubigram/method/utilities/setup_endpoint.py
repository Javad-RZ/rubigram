import rubigram
from ...logger import logger


class SetupEndpoints:
    async def setup_endpoints(self: "rubigram.Client"):
        endpoint_types = [
            "ReceiveUpdate",
            "ReceiveInlineMessage"
        ]
        for endpoint_type in endpoint_types:
            setup = await self.update_bot_endpoints(
                "{}/{}".format(self.endpoint, endpoint_type),
                endpoint_type
            )
            logger.info("[<] set endpoint for {} : {}".format(endpoint_type, setup["status"]))