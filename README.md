<p align="center">
  <img src="http://rubigram.ir/Rubigram.jpg" alt="Rubigram" width="200"/>
  <p Rubika Api Framework for Python </p>
    
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

**From pypi:**
```bash
pip install RubigramClient
```
**From github:**
```bash
git clone https://github.com/Javad-RZ/Rubigram.git
cd Rubigram
```

## Quick Example
```python
from rubigram import Client, filters
from rubigram.types import Update

client = Client(token="your_token_bot")

@client.on_message(filters.command("start"))
async def get_messages(client: Client, update: Update):
    await update.reply("Hi, rubigram user.")

client.run()
```

## Contex Manager
```python
from rubigram import Client
import asyncio

token = "your_token_bot"

async def main():
    async with Client(token=token) as client:
        info = await client.get_me()
        print(info.username)

asyncio.run(main())
```
