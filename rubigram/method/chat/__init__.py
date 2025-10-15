from .get_me import GetMe
from .get_chat import GetChat
from .get_update import GetUpdates

class Chat(
    GetMe,
    GetChat,
    GetUpdates
):
    pass