<p align="center">
  <img src="http://rubigram.ir/Rubigram.jpg" alt="Rubigram" width="200"/>
</p>

# Rubigram

Rubigram is a powerful asynchronous Python framework for **building advanced bots on Rubika**, offering features like concurrent message handling, advanced filtering, and support for both webhooks and polling.

---

## Features

- Asynchronous and fast: handle multiple messages concurrently.
- Advanced filters for private chats, commands, and text messages.
- Easy message and media sending (text, images, videos, files).
- Support for both **webhooks** and **polling**.
- Interactive keyboards and buttons for better user engagement.
- Flexible integration with databases for storing settings and data.

---

## Installation
```bash
pip install RubigramClient
```

## Quick Example
```python
from rubigram import Client
from rubigram.types import Update

client = Client(token="your_token_bot")

@client.on_message()
async def get_messages(client: Client, update: Update):
    await update.reply("Hi, rubigram user.")

client.run()```
