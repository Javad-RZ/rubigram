from .updater import Updater
from .dispatch import Dispatch
from .setup_endpoint import SetupEndpoints


class Utilities(
    Updater,
    Dispatch,
    SetupEndpoints
):
    pass