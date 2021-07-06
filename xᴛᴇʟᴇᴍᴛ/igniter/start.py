from pyrogram import Client as ɦɛʊʟ, filters
from pyrogram import StopPropagation
from pyrogram.types import Message
from ꜰɪɴx import *
from ʏȶʟʍӼ import *

@ɦɛʊʟ.on_message(
filters.private
& filters.command(
"start",
prefixes="/")) 
async def starts(_,ytrgx: Message):
    await ytrgx.reply_photo(
    YMMG,
    reply_markup=JoinButtlock3,
    caption=SCAP
    )
    return StopPropagation