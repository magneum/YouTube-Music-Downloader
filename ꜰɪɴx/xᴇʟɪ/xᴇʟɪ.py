import asyncio
from pyrogram.types import Message


async def rmVER(message: Message, text: str, delay: int):
    reply = await message.reply_text(text, quote=True)
    await asyncio.sleep(delay)
    await reply.delete()
    
async def delete_server(
    messages: tuple,
    delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
  
async def delete_help(
    messages: tuple,
    delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()

async def delete_server(
    messages: tuple,
    delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
        
async def delete_repl(
    messages: tuple,
    delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()

async def delete_gave(
    messages: tuple,
    delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()    
        