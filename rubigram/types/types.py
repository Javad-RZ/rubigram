from typing import Optional, Union
from dataclasses import dataclass, field
from .. import enums
from .object import Object


@dataclass
class Chat(Object):
    chat_id: Optional[str] = None
    chat_type: Optional[enums.ChatType] = None
    user_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    username: Optional[str] = None


@dataclass
class File(Object):
    file_id: Optional[str] = None
    file_name: Optional[str] = None
    size: Optional[int] = None


@dataclass
class ForwardedFrom(Object):
    type_from: Optional[enums.ForwardedFrom] = None
    message_id: Optional[str] = None
    from_chat_id: Optional[str] = None
    from_sender_id: Optional[str] = None


@dataclass
class PaymentStatus(Object):
    payment_id: Optional[str] = None
    status: Optional[Union[str, enums.PaymentStatus]] = None


@dataclass
class Bot(Object):
    bot_id: Optional[str] = None
    bot_title: Optional[str] = None
    avatar: Optional[File] = None
    description: Optional[str] = None
    username: Optional[str] = None
    start_message: Optional[str] = None
    share_url: Optional[str] = None


@dataclass
class BotCommand(Object):
    command: Optional[str] = None
    description: Optional[str] = None


@dataclass
class Sticker(Object):
    sticker_id: Optional[str] = None
    file: Optional[File] = None
    emoji_character: Optional[str] = None


@dataclass
class ContactMessage(Object):
    phone_number: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


@dataclass
class PollStatus(Object):
    state: Optional[Union[str, enums.PollStatus]] = None
    selection_index: Optional[int] = None
    percent_vote_options: Optional[list[int]] = None
    total_vote: Optional[int] = None
    show_total_votes: Optional[bool] = None


@dataclass
class Poll(Object):
    question: Optional[str] = None
    options: Optional[list[str]] = None
    poll_status: Optional[PollStatus] = None


@dataclass
class Location(Object):
    longitude: Optional[str] = None
    latitude: Optional[str] = None


@dataclass
class LiveLocation(Object):
    start_time: Optional[str] = None
    live_period: Optional[int] = None
    current_location: Optional[Location] = None
    user_id: Optional[str] = None
    status: Optional[Union[str, enums.LiveLocationStatus]] = None
    last_update_time: Optional[str] = None


@dataclass
class ButtonSelectionItem(Object):
    text: Optional[str] = None
    image_url: Optional[str] = None
    type: Optional[Union[str, enums.ButtonSelectionType]] = None


@dataclass
class ButtonSelection(Object):
    selection_id: Optional[str] = None
    search_type: Optional[str] = None
    get_type: Optional[str] = None
    items: Optional[list[ButtonSelectionItem]] = None
    is_multi_selection: Optional[bool] = None
    columns_count: Optional[str] = None
    title: Optional[str] = None


@dataclass
class ButtonCalendar(Object):
    default_value: Optional[str] = None
    type: Optional[Union[str, enums.ButtonCalendarType]] = None
    min_year: Optional[str] = None
    max_year: Optional[str] = None
    title: Optional[str] = None


@dataclass
class ButtonNumberPicker(Object):
    min_value: Optional[str] = None
    max_value: Optional[str] = None
    default_value: Optional[str] = None
    title: Optional[str] = None


@dataclass
class ButtonStringPicker(Object):
    items: Optional[list[str]] = None
    default_value: Optional[str] = None
    title: Optional[str] = None


@dataclass
class ButtonTextbox(Object):
    type_line: Optional[Union[str, enums.ButtonTextboxTypeLine]] = None
    type_keypad: Optional[Union[str, enums.ButtonTextboxTypeKeypad]] = None
    place_holder: Optional[str] = None
    title: Optional[str] = None
    default_value: Optional[str] = None


@dataclass
class ButtonLocation(Object):
    default_pointer_location: Optional[Location] = None
    default_map_location: Optional[Location] = None
    type: Optional[Union[str, enums.ButtonLocationType]] = None
    title: Optional[str] = None
    location_image_url: Optional[str] = None


@dataclass
class OpenChatData(Object):
    Object_guid: Optional[str] = None
    Object_type: Optional[Union[str, enums.ChatType]] = None


@dataclass
class JoinChannelData(Object):
    username: Optional[str] = None
    ask_join: bool = False


@dataclass
class ButtonLink(Object):
    type: Optional[Union[str, enums.ButtonLinkType]] = None
    link_url: Optional[str] = None
    joinchannel_data: Optional[JoinChannelData] = None
    open_chat_data: Optional[OpenChatData] = None


@dataclass
class AuxData(Object):
    start_id: Optional[str] = None
    button_id: Optional[str] = None


@dataclass
class Button(Object):
    id: Optional[str] = None
    button_text: Optional[str] = None
    type: Optional[Union[str, enums.ButtonType]] = enums.ButtonType.Simple
    button_selection: Optional[ButtonSelection] = None
    button_calendar: Optional[ButtonCalendar] = None
    button_number_picker: Optional[ButtonNumberPicker] = None
    button_string_picker: Optional[ButtonStringPicker] = None
    button_location: Optional[ButtonLocation] = None
    button_textbox: Optional[ButtonTextbox] = None
    button_link: Optional[ButtonLink] = None


@dataclass
class KeypadRow(Object):
    buttons: list[Button] = field(default_factory=list)


@dataclass
class Keypad(Object):
    rows: list[KeypadRow] = field(default_factory=list)
    resize_keyboard: bool = True
    on_time_keyboard: bool = False