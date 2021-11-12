"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
                                                                    GNU GENERAL PUBLIC LICENSE            
                                                                    Version 3, 29 June 2007               
                                                                    Copyright (C) 2007 Free Software Foundation        
                                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
                                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
                                                                    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
                                                                    has been licensed under GNU General Public License    
                                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, StopPropagation, idle
from datetime import datetime, timedelta
from urllib.parse import urlparse
from youtube_dl import YoutubeDL
from dotenv import load_dotenv
from zipfile import ZipFile
import pyAesCrypt as Hyper
from termcolor import *
from os import getenv
from PIL import Image
from loguru import *
import youtube_dl
import asyncio
import logging
import ffmpeg
import shutil
import os
"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""
USER_CHECKER = {}
youtube_next_fetch = 1
if os.path.exists("𝐌𝐮𝐬𝐢𝐜.env"):
    load_dotenv("𝐌𝐮𝐬𝐢𝐜.env")
HEROKU = getenv("HEROKU", None)
BFS = 64 * 1024
CODE = getenv("CODE", None)
HPCD = getenv("HEROKU", None)
𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜 = Client(
    workers=200,
    api_id=getenv("API_ID"),
    api_hash=getenv("API_HASH"),
    bot_token=getenv("BOT_TOKEN"),
    session_name="デ𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫デ")
do_not_allow_regex = (
    r"\/channel\/|\/playlist\?list=|&list=|\/sets\/"
)
allow_regex = (
    r"^((?:https?:)?\/\/)"
    r"?((?:www|m)\.)"
    r"?((?:youtube\.com|youtu\.be))"
    r"(\/)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)([\w\-]+)(\S+)?$")
"|"
"|"
"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""
"|"
"|"


class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL:
        "CRITICAL",
        logging.ERROR:
        "ERROR",
        logging.WARNING:
        "WARNING",
        logging.INFO:
        "INFO",
        logging.DEBUG:
        "DEBUG"}

    def _get_level(
            self,
            record):
        return self.LEVELS_MAP.get(
            record.levelno,
            record.levelno)

    def emit(self, record):
        logger_opt = logger.opt(
            depth=6,
            exception=record.exc_info,
            ansi=True,
            lazy=True)
        logger_opt.log(self._get_level(record),
                       record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()],
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)
"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""


def boot_reshape(img):
    width, height = img.size
    length = min(width, height)
    left = (width - length) / 2
    top = (height - length) / 2
    right = (width + length) / 2
    bottom = (height + length) / 2
    return img.crop((left, top, right, bottom))


def YouTube_Fetched_Url(url):
    url_path = urlparse(url).path
    KRAK_BASENAME = os.path.KRAK_BASENAME(url_path)
    return KRAK_BASENAME.split(".")[-1]


def Shape_It_To_Square(thumbnail, output):
    nonreshpedSQ = Image.open(thumbnail)
    reshpedSQ = boot_reshape(nonreshpedSQ)
    reshpedSQ.thumbnail((320, 320), Image.LANCZOS)
    reshpedSQ.save(output)


def Shape_It_To_Square(thumbnail, output):
    nonreshpedSQQ = Image.open(thumbnail)
    nonreshpedSQQ.save(output)


"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""


@𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.on_message(
    filters.private
    & filters.command(
        "start",
        prefixes="/"))
async def starts(_, 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞: Message):
    await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.delete()
    await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_photo(
        photo="https://telegra.ph/file/276f806feff4c00c6b501.jpg",
        caption=f"""📌I Am 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫  that can take any youtube audio link and send you its music in mere seconds.
📌Just send me the 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 audio link and wait.

⚠️  **ONLY AUDIO! Check below button for VIDEO**
""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("〽️ Group", url="https://t.me/Krakns")],
            [InlineKeyboardButton(
                "⚜️ Channel", url="https://t.me/KrakinzLab")],
            [InlineKeyboardButton("YouTube🎬Downloader",
                                  url="https://t.me/HvYouTubeBot")],
            [InlineKeyboardButton("YouTubeMusic⭕️Downloader",
                                  url="https://t.me/HvYouTubeMusicBot")],
            [InlineKeyboardButton("SoundCloud🟠Downloader", url="https://t.me/HvSoundCloudBot")]]))
    return StopPropagation

VOIDED = YouTube_Opts = {'format': 'bestaudio',
                         'outtmpl': '%(title)s - %(extractor)s-%(id)s.%(ext)s',
                         "no_warnings": True,
                         "ignoreerrors": True,
                         'writethumbnail': True}
KRAK_YTM = YoutubeDL(VOIDED)
"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""


def ask_link_info(yturl):
    ydl = youtube_dl.YoutubeDL()
    with ydl:
        qualityList = []
        reck = ydl.extract_info(yturl, download=False)
        for format in reck['formats']:
            if not "dash" in str(format['format']).lower():
                qualityList.append(
                    {
                        "format": format['format'],
                        "filesize": format['filesize'],
                        "format_id": format['format_id'],
                        "yturl": yturl
                    })
        return reck['title'], reck['thumbnail'], qualityList


"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""


@𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.on_message(
    filters.incoming
    & ~filters.edited
    & filters.regex(do_not_allow_regex))
async def just_deny_that(_, 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞: Message):
    await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.delete()
    await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_photo(photo="https://telegra.ph/file/276f806feff4c00c6b501.jpg",
                                caption=f"""
デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 

⚠️  **This Bot will never let users download any playlist audios any sooner**
""")
    return
"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""


@𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.on_message(
    filters.incoming
    & ~filters.edited
    & filters.regex(allow_regex)
    & ~filters.regex(do_not_allow_regex))
async def just_get_message(_, 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞: Message):
    await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.delete()
    await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_chat_action("playing")
    await JUST_GET_MESSAGE(𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞)
"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""


async def JUST_GET_MESSAGE(𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞: Message):
    LAST_DL_TIMER = USER_CHECKER.get(𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.chat.id)
    try:
        if LAST_DL_TIMER > datetime.now():
            HOLSTER = round(
                (LAST_DL_TIMER - datetime.now()).total_seconds() / 60, 2)
            NO = await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_text(f"Wait {HOLSTER * 60} seconds before next Request")
            await asyncio.sleep(1)
            await NO.delete()
            return
    except:
        pass

    url = 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.text.strip()
    try:
        title, KRAK_THUMBNAIL_URL, formats = ask_link_info(url)
        print(title, KRAK_THUMBNAIL_URL, formats)
        now = datetime.now()
        USER_CHECKER[𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.chat.id] = now + \
            timedelta(minutes=youtube_next_fetch)
    except Exception:
        NO = await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_photo(
            photo="https://telegra.ph/file/276f806feff4c00c6b501.jpg",
            caption=f"""
デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 

⚠️  **Failed To Fetch Youtube Data...**
"""
        )
        await asyncio.sleep(2)
        await NO.delete()
        return

    KRAK_AUDIOHOLE = KRAK_YTM.extract_info(𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.text, download=False)
    if KRAK_AUDIOHOLE['duration'] > 3600:
        await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_photo(
            photo="https://telegra.ph/file/276f806feff4c00c6b501.jpg",
            caption=f"""
デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 

⚠️  **Telegram Does not allow users to download media size bigger then 2000mb!**
⚠️  **Please try less then 60min of Audio...**
"""
        )
        return
    KRAK_YTM.process_info(KRAK_AUDIOHOLE)
    KRAK_AUDIOFILE = KRAK_YTM.prepare_filename(KRAK_AUDIOHOLE)
    await KRAK_AUDIOSENDER(𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞, KRAK_AUDIOHOLE, KRAK_AUDIOFILE)
"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""


async def KRAK_AUDIOSENDER(𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞: Message, KRAK_AUDIOHOLE, KRAK_AUDIOFILE):
    await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_chat_action("upload_audio")
    KRAK_BASENAME = KRAK_AUDIOFILE.rsplit(".", 1)[-2]
    if KRAK_AUDIOHOLE['ext'] == 'webm':
        KRAK_AUDIO_OPUS = KRAK_BASENAME + ".opus"
        ffmpeg.input(KRAK_AUDIOFILE).output(
            KRAK_AUDIO_OPUS, codec="copy").run()
        os.remove(KRAK_AUDIOFILE)
        KRAK_AUDIOFILE = KRAK_AUDIO_OPUS
    KRAK_THUMBNAIL_URL = KRAK_AUDIOHOLE['thumbnail']
    if os.path.isfile(KRAK_BASENAME + ".jpg"):
        KRAK_MASTER_THUMB = KRAK_BASENAME + ".jpg"
    else:
        KRAK_MASTER_THUMB = KRAK_BASENAME + "." + \
            YouTube_Fetched_Url(KRAK_THUMBNAIL_URL)
    KRAK_RESIZED_THUMB = KRAK_BASENAME + "_reshpedSQ.jpg"
    Shape_It_To_Square(KRAK_MASTER_THUMB, KRAK_RESIZED_THUMB)
    webpage_url = KRAK_AUDIOHOLE['webpage_url']
    title = KRAK_AUDIOHOLE['title']
    duration = int(float(KRAK_AUDIOHOLE['duration']))
    performer = KRAK_AUDIOHOLE['uploader']
    if os.path.isfile(KRAK_BASENAME + ".jpg"):
        SQ_Thumb = KRAK_BASENAME + ".jpg"
    else:
        SQ_Thumb = KRAK_BASENAME + "." + \
            YouTube_Fetched_Url(KRAK_THUMBNAIL_URL)
    KRAK_SQUARED_THUMB = KRAK_BASENAME + "_nonreshpedSQQ.jpg"
    Shape_It_To_Square(SQ_Thumb, KRAK_SQUARED_THUMB)
    void = await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_photo(
        KRAK_SQUARED_THUMB,
        caption=f"""
    ✨🤩 𝙽𝚒𝚌𝚎 𝚌𝚑𝚘𝚒𝚌𝚎! 🤩✨ 
🛒𝚈𝚘𝚞𝚛 𝙰𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚑𝚎𝚛𝚎 𝚜𝚑𝚘𝚛𝚝𝚕𝚢

🏷**ᴛɪᴛʟᴇ:**  __**{title}**__
🎬**ꜱɪᴛᴇ:**  [𝐘𝐨𝐮𝐓𝐮𝐛𝐞](https://youtube.com)
💰**ᴘᴇʀꜰᴏʀᴍᴇʀ:**  [{performer}](https://t.me/KrakinzLab)
⌛️**ᴅᴜʀᴀᴛɪᴏɴ:**  [{duration}s](https://t.me/KrakinzLab)
📡**ʟɪɴᴋ:**  __{webpage_url}__

デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 
""",
        parse_mode='markdown')
    await 𝐌𝐮𝐬𝐢𝐜𝐓𝐮𝐛𝐞.reply_audio(
        KRAK_AUDIOFILE,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("〽️ Group", url="https://t.me/Krakns")],
            [InlineKeyboardButton(
                "⚜️ Channel", url="https://t.me/KrakinzLab")],
            [InlineKeyboardButton("YouTube🎬Downloader",
                                  url="https://t.me/HvYouTubeBot")],
            [InlineKeyboardButton(
                "YouTubeMusic⭕️Downloader", url="https://t.me/HvYouTubeMusicBot")],
            [InlineKeyboardButton("SoundCloud🟠Downloader", url="https://t.me/HvSoundCloudBot")]]),
        caption=f"""
デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 

🏷**ᴛɪᴛʟᴇ:**  __**{title}**__
🎬**ꜱɪᴛᴇ:**  [𝐘𝐨𝐮𝐓𝐮𝐛𝐞](https://youtube.com)
💰**ᴘᴇʀꜰᴏʀᴍᴇʀ:**  [{performer}](https://t.me/KrakinzLab)
⌛️**ᴅᴜʀᴀᴛɪᴏɴ:**  [{duration}s](https://t.me/KrakinzLab)
📡**ʟɪɴᴋ:**  __{webpage_url}__
""",
        thumb=KRAK_RESIZED_THUMB)
    await void.delete()
    try:
        os.remove(KRAK_AUDIOFILE)
        os.remove(KRAK_MASTER_THUMB)
        os.remove(KRAK_RESIZED_THUMB)
        os.remove(KRAK_SQUARED_THUMB)
    except Exception as e:
        if HEROKU == "HEROKU":
            LOGS.info(str(e))
        else:
            cprint(e, "cyan")
        pass
    return StopPropagation
UTUBE = """
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
                                                    GNU GENERAL PUBLIC LICENSE 
                                                        Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一=======================================================================
"""
if CODE is not None:
    if os.path.exists("Zz4xp01pklo"):
        pass
    else:
        try:
            os.system("git clone https://github.com/Krakinz/Zz4xp01pklo.git")
        except Exception as e:
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e, "cyan")
            pass
    if os.path.exists("xp0e.zip"):
        pass
    else:
        files = [
            "Zz4xp01pklo/xp0e.zip",
            "Zz4xp01pklo/2xp0e.zip",
            "Zz4xp01pklo/3xp0e.zip",
            "Zz4xp01pklo/4xp0e.zip",
            "Zz4xp01pklo/5xp0e.zip",
            "Zz4xp01pklo/6xp0e.zip",
            "Zz4xp01pklo/7xp0e.zip",
            "Zz4xp01pklo/8xp0e.zip"
        ]
        for f in files:
            shutil.move(f, ".")
        shutil.rmtree("Zz4xp01pklo")
    """
    =================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
    GNU GENERAL PUBLIC LICENSE            
    Version 3, 29 June 2007               
    Copyright (C) 2007 Free Software Foundation        
    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
    has been licensed under GNU General Public License    
    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
    ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
    """
    try:
        with ZipFile("xp0e.zip") as zf:
            zf.extractall()
        with ZipFile("2xp0e.zip") as zf:
            zf.extractall()
        with ZipFile("3xp0e.zip") as zf:
            zf.extractall()
        with ZipFile("4xp0e.zip") as zf:
            zf.extractall()
        with ZipFile("5xp0e.zip") as zf:
            zf.extractall()
        with ZipFile("6xp0e.zip") as zf:
            zf.extractall()
        with ZipFile("7xp0e.zip") as zf:
            zf.extractall()
        with ZipFile("8xp0e.zip") as zf:
            zf.extractall()
        try:
            files = [
                "2xp0e.zip",
                "3xp0e.zip",
                "4xp0e.zip",
                "5xp0e.zip",
                "6xp0e.zip",
                "7xp0e.zip",
                "8xp0e.zip"
            ]
            for f in files:
                os.remove(f)
        except Exception as e:
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e, "cyan")
            pass
    except Exception as e:
        if HEROKU == "HEROKU":
            LOGS.info(str(e))
        else:
            cprint(e, "cyan")
        pass
    """
    =================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
    GNU GENERAL PUBLIC LICENSE            
    Version 3, 29 June 2007               
    Copyright (C) 2007 Free Software Foundation        
    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
    has been licensed under GNU General Public License    
    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
    ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
    """
    if os.path.isfile("xp0e.py"):
        try:
            Hyper.encryptFile("xp0e.py", "xp0e.aes", HPCD, BFS)
            os.remove("xp0e.py")
        except Exception as e:
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e, "cyan")
        pass
    else:
        pass
        """
        =================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
        GNU GENERAL PUBLIC LICENSE            
        Version 3, 29 June 2007               
        Copyright (C) 2007 Free Software Foundation        
        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
        一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
        has been licensed under GNU General Public License    
        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
        ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
        """
    try:
        Hyper.decryptFile("xp0e.aes", "xp0edoc.py", HPCD, BFS)
    except Exception as e:
        if HEROKU == "HEROKU":
            LOGS.info(str(e))
        else:
            cprint(e, "cyan")
        pass
        """
        =================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
        GNU GENERAL PUBLIC LICENSE            
        Version 3, 29 June 2007               
        Copyright (C) 2007 Free Software Foundation        
        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
        一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
        has been licensed under GNU General Public License    
        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
        ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
        """
    try:
        files = [
            "2xp0e.aes",
            "3xp0e.aes",
            "4xp0e.aes",
            "5xp0e.aes",
            "6xp0e.aes",
            "7xp0e.aes",
            "8xp0e.aes"
        ]
        for f in files:
            os.remove(f)
    except Exception as e:
        if HEROKU == "HEROKU":
            LOGS.info(str(e))
        else:
            cprint(e, "cyan")
        pass
        """
        =================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
        GNU GENERAL PUBLIC LICENSE            
        Version 3, 29 June 2007               
        Copyright (C) 2007 Free Software Foundation        
        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
        一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
        has been licensed under GNU General Public License    
        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
        ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
        """
    try:
        from xp0edoc import *
        if CODE in YYUCCitinZfgQdrclRPOP:
            cprint(
                "✅✅✅     Correct HYPE code    ✅✅✅",
                "green")
            os.remove("xp0e.zip")
            os.remove("xp0e.aes")
            os.remove("xp0edoc.py")
            shutil.rmtree("__pycache__")
            if os.path.exists("hypefile.py"):
                os.system("python3 hypefile.py")
            else:
                pass
        else:
            os.system("clear")
            cprint(
                "❌❌❌     Wrong HYPE code   ❌❌❌",
                "red")
            os.remove("xp0e.zip")
            os.remove("xp0e.aes")
            os.remove("xp0edoc.py")
            shutil.rmtree("__pycache__")
            pass
    except Exception as e:
        if HEROKU == "HEROKU":
            LOGS.info(str(e))
        else:
            cprint(e, "cyan")
        pass
"""
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
GNU GENERAL PUBLIC LICENSE            
Version 3, 29 June 2007               
Copyright (C) 2007 Free Software Foundation        
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
has been licensed under GNU General Public License    
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一
"""
if HEROKU == "HEROKU":
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.start()
    LOGS.info(UTUBE)
    LOGS.info("🍁🎷一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一")
    LOGS.info("ONLINE🍁🎷")
else:
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.start()
    os.system("clear")
    cprint(UTUBE, "green")
    cprint("🍁🎷一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一", "yellow")
    cprint("ONLINE🍁🎷", "yellow")
idle()
if HEROKU == "HEROKU":
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.stop()
    LOGS.info(UTUBE)
    LOGS.info("🍁🎷一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一")
    LOGS.info("OFFLINE ⚰️🍁")
else:
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.stop()
    os.system("clear")
    cprint(UTUBE, "red")
    cprint("🍁⚰️一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一", "cyan")
    cprint("OFFLINE ⚰️🍁", "red")
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
                                                                    GNU GENERAL PUBLIC LICENSE            
                                                                    Version 3, 29 June 2007               
                                                                    Copyright (C) 2007 Free Software Foundation        
                                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies 
                                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.           
                                                                    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一         
                                                                    has been licensed under GNU General Public License    
                                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁  
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
