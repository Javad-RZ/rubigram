from .send_message import SendMessage
from .send_poll import SendPoll
from .send_location import SendLocation
from .send_contact import SendContact
from .send_sticker import SendSticker
from .delete_message import DeleteMessage
from .remove_chat_keypad import RemoveChatKeypad
from .edit_chat_keypad import EditChatKeypad
from .edit_message_keypad import EditMessageKeypad
from .edit_message_text import EditMessageText
from .edit_message import EditMessage
from .forward_message import ForwardMessage


class Message(
    SendMessage,
    SendPoll,
    SendLocation,
    SendContact,
    SendSticker,
    DeleteMessage,
    RemoveChatKeypad,
    EditChatKeypad,
    EditMessageKeypad,
    EditMessageText,
    EditMessage,
    ForwardMessage
):
    pass