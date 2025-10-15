from .register import Register
from .on_message import OnMessage

class Decorator(
    Register,
    OnMessage
):
    pass