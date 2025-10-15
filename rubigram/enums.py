from enum import Enum


class ChatType(str, Enum):
    User = "User"
    Bot = "Bot"
    Group = "Group"
    Channel = "Channel"


class ForwardedFrom(str, Enum):
    User = "User"
    Bot = "Bot"
    Channel = "Channel"


class PaymentStatus(str, Enum):
    Paid = "Paid"
    NotPaid = "NotPaid"


class PollStatus(str, Enum):
    Open = "Open"
    Closed = "Closed"


class LiveLocationStatus(str, Enum):
    Stopped = "Stopped"
    Live = "Live"


class ButtonSelectionType(str, Enum):
    TextOnly = "TextOnly"
    TextImgThu = "TextImgThu"
    TextImgBig = "TextImgBig"


class ButtonSelectionSearch(str, Enum):
    Local = "Local"
    Api = "Api"


class ButtonSelectionGet(str, Enum):
    Local = "Local"
    Api = "Api"


class ButtonCalendarType(str, Enum):
    DatePersian = "DatePersian"
    DateGregorian = "DateGregorian"


class ButtonTextboxTypeKeypad(str, Enum):
    String = "String"
    Number = "Number"


class ButtonTextboxTypeLine(str, Enum):
    SingleLine = "SingleLine"
    MultiLine = "MultiLine"


class ButtonLocationType(str, Enum):
    Picker = "Picker"
    View = "View"


class ButtonLinkType(str, Enum):
    joinchannel = "joinchannel"
    url = "url"


class MessageSender(str, Enum):
    User = "User"
    Bot = "Bot"


class UpdateType(str, Enum):
    UpdatedMessage = "UpdatedMessage"
    NewMessage = "NewMessage"
    RemovedMessage = "RemovedMessage"
    StartedBot = "StartedBot"
    StoppedBot = "StoppedBot"
    UpdatedPayment = "UpdatedPayment"


class ChatKeypadType(str, Enum):
    New = "New"
    Remove = "Remove"


class UpdateEndpointType(str, Enum):
    ReceiveUpdate = "ReceiveUpdate"
    ReceiveInlineMessage = "ReceiveInlineMessage"
    ReceiveQuery = "ReceiveQuery"
    GetSelectionItem = "GetSelectionItem"
    SearchSelectionItems = "SearchSelectionItems"


class ButtonType(str, Enum):
    Simple = "Simple"
    Selection = "Selection"
    Calendar = "Calendar"
    NumberPicker = "NumberPicker"
    StringPicker = "StringPicker"
    Location = "Location"
    Payment = "Payment"
    CameraImage = "CameraImage"
    CameraVideo = "CameraVideo"
    GalleryImage = "GalleryImage"
    GalleryVideo = "GalleryVideo"
    File = "File"
    Audio = "Audio"
    RecordAudio = "RecordAudio"
    MyPhoneNumber = "MyPhoneNumber"
    MyLocation = "MyLocation"
    Textbox = "Textbox"
    Link = "Link"
    AskMyPhoneNumber = "AskMyPhoneNumber"
    AskLocation = "AskLocation"
    Barcode = "Barcode"


class FileType(str, Enum):
    File = "File"
    Image = "Image"
    Video = "Video"
    Gif = "Gif"
    Music = "Music"
    Voice = "Voice"


class ChatAction(str, Enum):
    Typing = "Typing"
    Uploading = "Uploading"
    Recording = "Recording"