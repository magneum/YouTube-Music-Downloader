from pyrogram import Client, idle
import shutil
from logging import INFO, basicConfig, getLogger
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGS = getLogger(__name__)
from ꜱᴇᴇᴅʀ import *
from JKEDPPWEFJMXZPADOWQDJNADSMP import *
from knite import *


Client = Client(
    HS,
    api_id=Feros.APP_ID,
    api_hash=Feros.API_HASH,
    bot_token=Feros.BOT_TOKEN,
    workers=12,
    plugins=PYT
)