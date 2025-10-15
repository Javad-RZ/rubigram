from .chat import Chat
from .file import File
from .setting import Setting
from .network import Network
from .messages import Message
from .decorator import Decorator
from .utilities import Utilities

class Method(
    Chat,
    File,
    Setting,
    Network,
    Message,
    Decorator,
    Utilities
):
    pass