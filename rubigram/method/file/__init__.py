from .send_gif import SendGif
from .get_file import GetFile
from .get_bytes import GetBytes
from .send_file import SendFile
from .send_photo import SendPhoto
from .send_video import SendVideo
from .send_music import SendMusic
from .send_voice import SendVoice
from .get_file_name import GetFileName
from .send_document import SendDocument
from .download_file import DownloadFile
from .request_send_file import RequestSendFile
from .request_upload_file import RequestUploadFile
from .request_download_file import RequestDownloadFile

class File(
    SendGif,
    GetFile,
    GetBytes,
    SendFile,
    SendPhoto,
    SendVideo,
    SendMusic,
    SendVoice,
    GetFileName,
    SendDocument,
    DownloadFile,
    RequestSendFile,
    RequestUploadFile,
    RequestDownloadFile
):
    pass