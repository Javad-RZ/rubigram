from typing import Callable, Any, Optional, Union
from rubigram.types import Update, InlineMessage
import re
import rubigram


class Filter:
    async def __call__(
        self,
        client: "rubigram.Client",
        update: Union[Update, InlineMessage]
    ) -> bool:
        raise NotImplementedError

    def __invert__(self) -> "Filter":
        return InvertFilter(self)

    def __and__(self, other: "Filter") -> "Filter":
        return AndFilter(self, other)

    def __or__(self, other: "Filter") -> "Filter":
        return OrFilter(self, other)


class InvertFilter(Filter):
    def __init__(self, base: Filter):
        self.base = base

    async def __call__(self, client: "rubigram.Client", update: Any) -> bool:
        return not await self.base(client, update)


class AndFilter(Filter):
    def __init__(self, base: Filter, other: Filter):
        self.base = base
        self.other = other

    async def __call__(self, client: "rubigram.Client", update: Any) -> bool:
        return await self.base(client, update) and await self.other(client, update)


class OrFilter(Filter):
    def __init__(self, base: Filter, other: Filter):
        self.base = base
        self.other = other

    async def __call__(self, client: "rubigram.Client", update: Any) -> bool:
        return await self.base(client, update) or await self.other(client, update)


CUSTOM_FILTER_NAME = "CustomFilter"


def create(func: Callable, name: Optional[str] = None, **kwargs) -> Filter:
    """Create a custom Rubigram filter.

    Custom filters let you control which updates your handlers receive.

    Args:
        func (Callable): Async function that takes (filter, client, update) and returns bool.
        name (str, optional): Filter class name. Defaults to 'CustomFilter'.
        **kwargs: Extra parameters accessible inside the filter.

    Example:
        >>> from rubigram import filters
        >>>
        >>> async def is_admin(client, update):
        >>>     return update.chat_id in ADMIN_IDS
        >>>
        >>> admin = filters.create(is_admin)
    """
    return type(
        name or func.__name__ or CUSTOM_FILTER_NAME,
        (Filter,),
        {"__call__": func, **kwargs}
    )()


async def text_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Filter updates that contain text messages.

    This filter passes only updates that include text content, whether they are
    new messages, edited messages, or inline messages.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The update to check for text content.

    Returns:
        bool: True if the update contains text, False otherwise.

    Example:
        >>> from rubigram improt filters

        >>> @client.on_message(filters.text)
        >>> async def handle_text(client, update):
        >>>     await client.send_message(update.chat_id, "Received a text message!")
    """
    if isinstance(update, Update):
        msg = update.new_message or update.updated_message
        return bool(getattr(msg, "text", None))
    elif isinstance(update, InlineMessage):
        return bool(getattr(update, "text", None))
    return False

text = create(text_filter)


async def file_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Filter updates that contain a file.

    This filter passes only updates that include a file attachment in new messages.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The update to check for a file.

    Returns:
        bool: True if the update contains a file, False otherwise.

    Example:
        >>> from rubigram import filters
        >>>
        >>> @client.on_message(filters.file)
        >>> async def handle_file(client, update):
        >>>     await client.send_message(update.chat_id, "Received a file!")
    """
    if isinstance(update, Update):
        msg = update.new_message
        return bool(getattr(msg, "file", None))
    return False

file = create(file_filter)


async def live_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Filter updates that contain a live location.

    This filter passes only updates that include a live location in new messages.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The update to check for a live location.

    Returns:
        bool: True if the update contains a live location, False otherwise.

    Example:
        >>> from rubigram import filters
        >>>
        >>> @client.on_message(filters.live)
        >>> async def handle_live(client, update):
        >>>     await client.send_message(update.chat_id, "Received a live location!")
    """
    if isinstance(update, Update):
        msg = update.new_message
        return bool(getattr(msg, "live_location", None))
    return False

live = create(live_filter)


async def poll_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Filter updates that contain a poll.

    This filter passes only updates that include a poll in new messages.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The update to check for a poll.

    Returns:
        bool: True if the update contains a poll, False otherwise.

    Example:
        >>> from rubigram import filters
        >>>
        >>> @client.on_message(filters.poll)
        >>> async def handle_poll(client, update):
        >>>     await client.send_message(update.chat_id, "Received a poll!")
    """
    if isinstance(update, Update):
        msg = update.new_message
        return bool(getattr(msg, "poll", None))
    return False

poll = create(poll_filter)


async def contact_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Check if the update contains a contact message.

    This filter checks if the incoming update is a message of type `Update` 
    and whether it includes a contact object (`contact_message`). 
    Inline messages will always return False for this filter because contacts
    cannot be sent via inline messages.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The incoming update to check.

    Returns:
        bool: True if the update contains a contact message, False otherwise.

    Example:
        >>> @client.on_message(filters.contact)
        >>> async def handle_contact(client, update):
        >>>     await client.send_message(update.chat_id, "You sent a contact!")
    """
    if isinstance(update, Update):
        msg = update.new_message
        return bool(getattr(msg, "contact_message", None))
    return False

contact = create(contact_filter)


async def sticker_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Check if the update contains a sticker.

    This filter checks if the incoming update is a message of type `Update` 
    and whether it includes a sticker object (`sticker`). 
    Inline messages will always return False for this filter because stickers
    cannot be sent via inline messages.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The incoming update to check.

    Returns:
        bool: True if the update contains a sticker, False otherwise.

    Example:
        >>> @client.on_message(filters.sticker)
        >>> async def handle_sticker(client, update):
        >>>     await client.send_message(update.chat_id, "You sent a sticker!")
    """
    if isinstance(update, Update):
        msg = update.new_message
        return bool(getattr(msg, "sticker", None))
    return False

sticker = create(sticker_filter)


async def location_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Check if the update contains a location.

    This filter checks if the incoming update is a message of type `Update` 
    and whether it includes a location object (`location`). 
    Inline messages will always return False because locations cannot be sent
    via inline messages.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The incoming update to check.

    Returns:
        bool: True if the update contains a location, False otherwise.

    Example:
        >>> @client.on_message(filters.location)
        >>> async def handle_location(client, update):
        >>>     await client.send_message(update.chat_id, "You shared a location!")
    """
    if isinstance(update, Update):
        msg = update.new_message
        return bool(getattr(msg, "location", None))
    return False

location = create(location_filter)


async def forward_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Check if the update is a forwarded message.

    This filter checks if the incoming update is a message of type `Update` 
    and whether it includes a `forwarded_from` object indicating the message
    was forwarded from another user, bot, or channel. 
    Inline messages will always return False because forwarding is only for chat messages.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The incoming update to check.

    Returns:
        bool: True if the update is forwarded, False otherwise.

    Example:
        >>> @client.on_message(filters.forward)
        >>> async def handle_forward(client, update):
        >>>     await client.send_message(update.chat_id, "This message was forwarded!")
    """
    if isinstance(update, Update):
        msg = update.new_message
        return bool(getattr(msg, "forwarded_from", None))
    return False

forward = create(forward_filter)


async def edited_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Check if the update contains an edited message.

    This filter checks if the incoming update is of type `Update` and contains
    an `updated_message` object. Inline messages cannot be edited, so they
    will always return False.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The incoming update to check.

    Returns:
        bool: True if the update is an edited message, False otherwise.

    Example:
        >>> @client.on_message(filters.edited)
        >>> async def handle_edited(client, update):
        >>>     await client.send_message(update.chat_id, "This message was edited!")
    """
    if isinstance(update, Update):
        return bool(update.updated_message)
    return False

edited = create(edited_filter)


async def private_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Check if the update comes from a private chat.

    This filter verifies if the incoming update belongs to a private chat.
    Private chat IDs in Rubigram start with 'b0'.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The update to check.

    Returns:
        bool: True if the update is from a private chat, False otherwise.

    Example:
        >>> @client.on_message(filters.private)
        >>> async def handle_private(client, update):
        >>>     await client.send_message(update.chat_id, "Private chat message received!")
    """
    return str(update.chat_id).startswith("b0")

private = create(private_filter)


async def group_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Check if the update comes from a group chat.

    This filter verifies if the incoming update belongs to a group chat.
    Group chat IDs in Rubigram start with 'g0'.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The update to check.

    Returns:
        bool: True if the update is from a group chat, False otherwise.

    Example:
        >>> @client.on_message(filters.group)
        >>> async def handle_group(client, update):
        >>>     await client.send_message(update.chat_id, "Group chat message received!")
    """
    return str(update.chat_id).startswith("g0")

group = create(group_filter)


async def channel_filter(client, update: Union[Update, InlineMessage]) -> bool:
    """Check if the update comes from a channel.

    This filter verifies if the incoming update belongs to a channel.
    Channel IDs in Rubigram start with 'c0'.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Union[Update, InlineMessage]): The update to check.

    Returns:
        bool: True if the update is from a channel, False otherwise.

    Example:
        >>> @client.on_message(filters.channel)
        >>> async def handle_channel(client, update):
        >>>     await client.send_message(update.chat_id, "Channel message received!")
    """
    return str(update.chat_id).startswith("c0")

channel = create(channel_filter)


async def forward_bot_filter(client, update: Update) -> bool:
    """Check if a message is forwarded from a bot.

    This filter passes only updates where the message is a forward
    from a bot account.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Update): The update to check.

    Returns:
        bool: True if the message was forwarded from a bot, False otherwise.

    Example:
        >>> @client.on_message(filters.forward_bot)
        >>> async def handle_forward_bot(client, update):
        >>>     await client.send_message(update.chat_id, "Forwarded from a bot!")
    """
    if update.new_message and update.new_message.forwarded_from:
        return update.new_message.forwarded_from.type_from == "Bot"
    return False

forward_bot = create(forward_bot_filter)


async def forward_user_filter(client, update: Update) -> bool:
    """Check if a message is forwarded from a user.

    This filter passes only updates where the message is a forward
    from a regular user account.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Update): The update to check.

    Returns:
        bool: True if the message was forwarded from a user, False otherwise.

    Example:
        >>> @client.on_message(filters.forward_user)
        >>> async def handle_forward_user(client, update):
        >>>     await client.send_message(update.chat_id, "Forwarded from a user!")
    """
    if update.new_message and update.new_message.forwarded_from:
        return update.new_message.forwarded_from.type_from == "User"
    return False

forward_user = create(forward_user_filter)


async def forward_channel_filter(client, update: Update) -> bool:
    """Check if a message is forwarded from a channel.

    This filter passes only updates where the message is a forward
    from a channel.

    Args:
        client (rubigram.Client): The Rubigram client instance.
        update (Update): The update to check.

    Returns:
        bool: True if the message was forwarded from a channel, False otherwise.

    Example:
        >>> @client.on_message(filters.forward_channel)
        >>> async def handle_forward_channel(client, update):
        >>>     await client.send_message(update.chat_id, "Forwarded from a channel!")
    """
    if update.new_message and update.new_message.forwarded_from:
        return update.new_message.forwarded_from.type_from == "Channel"
    return False

forward_channel = create(forward_channel_filter)


def command(
    commands: Union[str, list[str]],
    prefix: Union[str, list[str]] = "/",
    case_sensitive: bool = False
) -> bool:
    """Filter updates that start with specific command(s).

    This filter passes only updates where the message text starts with
    one of the specified commands, optionally supporting multiple prefixes
    and case sensitivity.

    Args:
        commands (Union[str, list[str]]): A command or list of commands to match.
        prefix (Union[str, list[str]], optional): Command prefix(es). Defaults to "/".
        case_sensitive (bool, optional): Whether matching should be case sensitive. Defaults to False.

    Returns:
        Filter: A Rubigram filter that can be used with @app.on_message.

    Example:
        >>> @app.on_message(filters.command("start"))
        >>> async def handle_start(client, update):
        >>>     await client.send_message(update.chat_id, "Bot started!")

        >>> @app.on_message(filters.command(["start", "help"], prefix=["/", "!"]))
        >>> async def handle_multiple(client, update):
        >>>     await client.send_message(update.chat_id, "Command received!")
    """

    async def func(client, update):
        if isinstance(update, Update):
            msg = update.new_message or update.updated_message
            if not msg or not getattr(msg, "text", None):
                return False
            text = msg.text if case_sensitive else msg.text.lower()
            cmds = [
                c if case_sensitive else c.lower() for c in (
                    commands if isinstance(commands, list) else [commands]
                )
            ]
            prefixes_list = prefix if isinstance(prefix, list) else [prefix]
            full_cmds = [p + c for p in prefixes_list for c in cmds]
            return any(text.startswith(cmd) for cmd in full_cmds)
        return False

    return create(
        func,
        "CommandFilter",
        commands=commands,
        prefix=prefix,
        case_sensitive=case_sensitive
    )


def chat(chat_id: Union[str, list[str]]):
    """Filter updates based on chat ID(s).

    This filter passes only updates that belong to the specified chat ID(s).

    Args:
        chat_id (Union[str, list[str]]): A chat ID or list of chat IDs to filter.

    Returns:
        Filter: A Rubigram filter that can be used with @app.on_message or @app.on_inline.

    Example:
        >>> @app.on_message(filters.chat("b0123456789"))
        >>> async def handle_private(client, update):
        >>>     await client.send_message(update.chat_id, "Hello private chat!")

        >>> @app.on_message(filters.chat(["g0123", "g0456"]))
        >>> async def handle_groups(client, update):
        >>>     await client.send_message(update.chat_id, "Hello group!")
    """

    async def func(client, update: Union[Update, InlineMessage]):
        chat_ids = chat_id if isinstance(chat_id, list) else [chat_id]
        return update.chat_id in chat_ids

    return create(
        func,
        "ChatFilter",
        chat_id=chat_id
    )


def regex(pattern: str):
    """Filter updates whose text matches a regular expression.

    This filter passes only updates (new messages, edited messages, or inline messages)
    where the text content matches the specified regex pattern.

    Args:
        pattern (str): The regular expression pattern to match against the message text.

    Returns:
        Filter: A Rubigram filter that can be used with @app.on_message or @app.on_inline.

    Example:
        >>> @app.on_message(filters.regex(r"hello|hi"))
        >>> async def handle_greetings(client, update):
        >>>     await client.send_message(update.chat_id, "Hello there!")
    """

    async def func(client, update: Union[Update, InlineMessage]):
        text = ""
        if isinstance(update, Update):
            if update.type == "NewMessage":
                text = getattr(update.new_message, "text", "")
            elif update.type == "UpdatedMessage":
                text = getattr(update.updated_message, "text", "")
        elif isinstance(update, InlineMessage):
            text = getattr(update, "text", "")

        return bool(re.search(pattern, text)) if text else False

    return create(
        func,
        "RegexFilter",
        pattern=pattern
    )


def button(button_id: Union[str, list[str]], prefix: Union[str, list[str]] = "", case_sensitive: bool = False):
    """Filter inline messages based on button IDs.

    This filter passes only `InlineMessage` updates whose button ID matches
    one of the specified IDs, optionally supporting multiple prefixes
    and case sensitivity.

    Args:
        button_id (str | list[str]): Button ID or list of button IDs to match.
        prefix (str | list[str], optional): Prefix or list of prefixes for the button IDs. Defaults to "".
        case_sensitive (bool, optional): Whether matching should be case sensitive. Defaults to False.

    Returns:
        Filter: A Rubigram filter that can be used with @app.on_inline or similar handlers.

    Example:
        >>> @app.on_inline(filters.button("btn_1"))
        >>> async def handle_btn(client, update):
        >>>     await client.send_message(update.chat_id, "Button 1 pressed!")

        >>> @app.on_inline(filters.button(["btn_1", "btn_2"], prefix="prefix_"))
        >>> async def handle_multiple_buttons(client, update):
        >>>     await client.send_message(update.chat_id, "Button pressed!")
    """

    button_ids = [
        btn if case_sensitive else btn.lower() for btn in (
            button_id if isinstance(button_id, list) else [button_id]
        )
    ]
    prefixes = prefix if isinstance(prefix, list) else [prefix]
    btn_ids = [p + b for p in prefixes for b in button_ids]

    async def func(flt, client, update: InlineMessage):
        if isinstance(update, InlineMessage):
            text = update.aux_data.button_id or ""
            text = text if case_sensitive else text.lower()
            return any(text.startswith(b) for b in btn_ids)
        return False

    return create(
        func,
        "ButtonFilter",
        button_ids=button_ids,
        prefixes=prefixes,
        case_sensitive=case_sensitive
    )