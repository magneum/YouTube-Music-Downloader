"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
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
import time
import sys
import os
"|"
"|"
"|"
"|"
os.system("clear")
os.system("pip uninstall ffmpeg-python -y ")
os.system("pip install ffmpeg-python")
os.system("clear")
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"
user_time = {}
youtube_next_fetch = 1
HEROKU = getenv("HEROKU", None)
BFS = 64 * 1024
CODE = getenv("CODE", None)
HPCD = getenv("HEROKU", None)
load_dotenv("./𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫.env")
allow_regex = (
    r"^((?:https?:)?\/\/)"
    r"?((?:www|m)\.)"
    r"?((?:youtube\.com|youtu\.be))"
    r"(\/)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)([\w\-]+)(\S+)?$"
)
do_not_allow_regex = (
    r"\/channel\/|\/playlist\?list=|&list=|\/sets\/"
)
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
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
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"
𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜 = Client(
    workers=200,
    api_id=getenv("API_ID"),
    api_hash=getenv("API_HASH"),
    bot_token=getenv("BOT_TOKEN"),
    session_name="デ𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫デ")
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


def boot_reshape(img):
    width, height = img.size
    length = min(width, height)
    left = (width - length) / 2
    top = (height - length) / 2
    right = (width + length) / 2
    bottom = (height + length) / 2
    return img.crop((left, top, right, bottom))


"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


def YouTube_Fetched_Url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


def Shape_It_To_Square(thumbnail, output):
    nonreshpedSQ = Image.open(thumbnail)
    reshpedSQ = boot_reshape(nonreshpedSQ)
    reshpedSQ.thumbnail((320, 320), Image.LANCZOS)
    reshpedSQ.save(output)


"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


def Shape_It_To_Square(thumbnail, output):
    nonreshpedSQQ = Image.open(thumbnail)
    nonreshpedSQQ.save(output)


"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


@𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.on_message(
    filters.private
    & filters.command(
        "start",
        prefixes="/"))
async def starts(_, 𝐓𝐮𝐛𝐞: Message):
    await 𝐓𝐮𝐛𝐞.delete()
    await 𝐓𝐮𝐛𝐞.reply_photo(
        photo="https://telegra.ph/file/276f806feff4c00c6b501.jpg",
        caption=f"""
一 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 一

📌I Am 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 that can take any youtube audio 
link and send you its music in mere seconds.
📌Just send me the 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 audio link and wait.
⚠️  **ONLY AUDIO! Check below button for VIDEO**
""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("〽️ 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/Krakns")],
            [InlineKeyboardButton(
                "⚜️ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/KrakinzLab")],
            [InlineKeyboardButton("𝐘𝐨𝐮𝗦𝗼𝘂𝗻𝗱🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫",
                                  url="https://t.me/HvYouTubeBot")],
            [InlineKeyboardButton(
                "𝐘𝐨𝐮𝗦𝗼𝘂𝗻𝗱⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫", url="https://t.me/HvYouTubeMusicBot")],
            [InlineKeyboardButton("𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱🟠𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿", url="https://t.me/HvSoundCloudBot")]]))
    return StopPropagation
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"
VOIDED = YouTube_Opts = {'format': 'bestaudio',
                         'outtmpl': '%(title)s - %(extractor)s-%(id)s.%(ext)s',
                         "no_warnings": True,
                         "ignoreerrors": True,
                         'writethumbnail': True}
HV_YouTube_Audio = YoutubeDL(VOIDED)
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


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


"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


@𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.on_message(
    filters.incoming
    & ~filters.edited
    & filters.regex(do_not_allow_regex))
async def just_deny_that(_, 𝐓𝐮𝐛𝐞: Message):
    await 𝐓𝐮𝐛𝐞.delete()
    await 𝐓𝐮𝐛𝐞.reply_photo(photo="https://telegra.ph/file/276f806feff4c00c6b501.jpg",
                           caption=f"""
一 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 一

⚠️  **This Bot will never let users download any playlist audios any sooner**
""")
    return
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


@𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.on_message(
    filters.incoming
    & ~filters.edited
    & filters.regex(allow_regex)
    & ~filters.regex(do_not_allow_regex))
async def just_get_message(_, 𝐓𝐮𝐛𝐞: Message):
    await 𝐓𝐮𝐛𝐞.delete()
    await 𝐓𝐮𝐛𝐞.reply_chat_action("playing")
    await just_get_Message(𝐓𝐮𝐛𝐞)
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


async def just_get_Message(𝐓𝐮𝐛𝐞: Message):
    userLastDownloadTime = user_time.get(𝐓𝐮𝐛𝐞.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round(
                (userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            NO = await 𝐓𝐮𝐛𝐞.reply_text(f"Wait {wait_time * 60} seconds before next Request")
            await asyncio.sleep(1)
            await NO.delete()
            return
    except:
        pass

    url = 𝐓𝐮𝐛𝐞.text.strip()
    try:
        title, thumbnail_url, formats = ask_link_info(url)
        print(title, thumbnail_url, formats)
        now = datetime.now()
        user_time[𝐓𝐮𝐛𝐞.chat.id] = now + \
            timedelta(minutes=youtube_next_fetch)
    except Exception:
        NO = await 𝐓𝐮𝐛𝐞.reply_photo(
            photo="https://telegra.ph/file/276f806feff4c00c6b501.jpg",
            caption=f"""
一 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 一

⚠️  **Failed To Fetch Youtube Data...**
"""
        )
        await asyncio.sleep(2)
        await NO.delete()
        return

    Audio_Hole = HV_YouTube_Audio.extract_info(𝐓𝐮𝐛𝐞.text, download=False)
    if Audio_Hole['duration'] > 3600:
        await 𝐓𝐮𝐛𝐞.reply_photo(
            photo="https://telegra.ph/file/276f806feff4c00c6b501.jpg",
            caption=f"""
一 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 一

⚠️  **Telegram Does not allow users to download media size bigger then 2000mb!**
⚠️  **Please try less then 60min of Audio...**
"""
        )
        return
    HV_YouTube_Audio.process_info(Audio_Hole)
    audio_file = HV_YouTube_Audio.prepare_filename(Audio_Hole)
    await audio_sender(𝐓𝐮𝐛𝐞, Audio_Hole, audio_file)
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"


async def audio_sender(𝐓𝐮𝐛𝐞: Message, Audio_Hole, audio_file):
    await 𝐓𝐮𝐛𝐞.reply_chat_action("upload_audio")
    basename = audio_file.rsplit(".", 1)[-2]
    if Audio_Hole['ext'] == 'webm':
        audio_file_opus = basename + ".opus"
        ffmpeg.input(audio_file).output(audio_file_opus, codec="copy").run()
        os.remove(audio_file)
        audio_file = audio_file_opus
    thumbnail_url = Audio_Hole['thumbnail']
    if os.path.isfile(basename + ".jpg"):
        Master_Thumb = basename + ".jpg"
    else:
        Master_Thumb = basename + "." + \
            YouTube_Fetched_Url(thumbnail_url)
    resized_thumb = basename + "_reshpedSQ.jpg"
    Shape_It_To_Square(Master_Thumb, resized_thumb)
    webpage_url = Audio_Hole['webpage_url']
    title = Audio_Hole['title']
    duration = int(float(Audio_Hole['duration']))
    performer = Audio_Hole['uploader']
    if os.path.isfile(basename + ".jpg"):
        SQ_Thumb = basename + ".jpg"
    else:
        SQ_Thumb = basename + "." + \
            YouTube_Fetched_Url(thumbnail_url)
    Squared_Thumb = basename + "_nonreshpedSQQ.jpg"
    Shape_It_To_Square(SQ_Thumb, Squared_Thumb)
    void = await 𝐓𝐮𝐛𝐞.reply_photo(
        Squared_Thumb,
        caption=f"""
    ✨🤩 𝙽𝚒𝚌𝚎 𝚌𝚑𝚘𝚒𝚌𝚎! 🤩✨ 
🛒𝚈𝚘𝚞𝚛 𝙰𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚑𝚎𝚛𝚎 𝚜𝚑𝚘𝚛𝚝𝚕𝚢

🏷**ᴛɪᴛʟᴇ:**  __**{title}**__
🎬**ꜱɪᴛᴇ:**  [𝐘𝐨𝐮𝐓𝐮𝐛𝐞](https://youtube.com)
💰**ᴘᴇʀꜰᴏʀᴍᴇʀ:**  [{performer}](https://t.me/KrakinzLab)
⌛️**ᴅᴜʀᴀᴛɪᴏɴ:**  [{duration}s](https://t.me/KrakinzLab)
📡**ʟɪɴᴋ:**  __{webpage_url}__

一 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 一
""",
        parse_mode='markdown')
    await 𝐓𝐮𝐛𝐞.reply_audio(
        audio_file,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("〽️ 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/Krakns")],
            [InlineKeyboardButton(
                "⚜️ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/KrakinzLab")],
            [InlineKeyboardButton("𝐘𝐨𝐮𝗦𝗼𝘂𝗻𝗱🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫",
                                  url="https://t.me/HvYouTubeBot")],
            [InlineKeyboardButton(
                "𝐘𝐨𝐮𝗦𝗼𝘂𝗻𝗱⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫", url="https://t.me/HvYouTubeMusicBot")],
            [InlineKeyboardButton("𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱🟠𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿", url="https://t.me/HvSoundCloudBot")]]),
        caption=f"""
一 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 一

🏷**ᴛɪᴛʟᴇ:**  __**{title}**__
🎬**ꜱɪᴛᴇ:**  [𝐘𝐨𝐮𝐓𝐮𝐛𝐞](https://youtube.com)
💰**ᴘᴇʀꜰᴏʀᴍᴇʀ:**  [{performer}](https://t.me/KrakinzLab)
⌛️**ᴅᴜʀᴀᴛɪᴏɴ:**  [{duration}s](https://t.me/KrakinzLab)
📡**ʟɪɴᴋ:**  __{webpage_url}__
""",
        thumb=resized_thumb)
    await void.delete()
    try:
        os.remove(audio_file)
        os.remove(Master_Thumb)
        os.remove(resized_thumb)
        os.remove(Squared_Thumb)
    except Exception as e:
        if HEROKU == "HEROKU":
            LOGS.info(str(e))
        else:
            cprint(e, "cyan")
        pass
    return StopPropagation
UTUBE = """
=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
                                                    GNU GENERAL PUBLIC LICENSE 
                                                        Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一=======================================================================
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
        "|"
        "|"
        "|"
        "|"
        """=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
        GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
            Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
        Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
            一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
        has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
        ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
        "|"
        "|"
        "|"
        "|"
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
        "|"
        "|"
        "|"
        "|"
        """=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
        GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
            Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
        Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
            一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
        has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
        ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
        "|"
        "|"
        "|"
        "|"
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
        "|"
        "|"
        "|"
        "|"
        """=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
        GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
            Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
        Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
            一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
        has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
        ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
        "|"
        "|"
        "|"
        "|"
    try:
        Hyper.decryptFile("xp0e.aes", "xp0edoc.py", HPCD, BFS)
    except Exception as e:
        if HEROKU == "HEROKU":
            LOGS.info(str(e))
        else:
            cprint(e, "cyan")
        pass
        "|"
        "|"
        "|"
        "|"
        """=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
        GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
            Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
        Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
            一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
        has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
        ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
        "|"
        "|"
        "|"
        "|"
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
        "|"
        "|"
        "|"
        "|"
        """=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
        GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
            Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
        Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
            一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
        has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
        ====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
        "|"
        "|"
        "|"
        "|"
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
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
"|"
"|"
"|"
"|"
if HEROKU == "HEROKU":
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.start()
    LOGS.info(UTUBE)
    LOGS.info("🍁🎷一═デ𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞デ═一")
    LOGS.info("ONLINE🍁🎷")
else:
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.start()
    os.system("clear")
    cprint(UTUBE, "green")
    cprint("🍁🎷一═デ𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞デ═一", "yellow")
    cprint("ONLINE🍁🎷", "yellow")
idle()
if HEROKU == "HEROKU":
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.stop()
    LOGS.info(UTUBE)
    LOGS.info("🍁🎷一═デ𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞デ═一")
    LOGS.info("OFFLINE ⚰️🍁")
else:
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.stop()
    os.system("clear")
    cprint(UTUBE, "red")
    cprint("🍁⚰️一═デ𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞デ═一", "cyan")
    cprint("OFFLINE ⚰️🍁", "red")
"|"
"|"
"|"
"|"
"""=================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一==========================================================================
GNU GENERAL PUBLIC LICENSE                                                                                                                      GNU GENERAL PUBLIC LICENSE                                                                               
    Version 3, 29 June 2007                                                                                                                     Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation                                                                                  Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                       Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies                                                                      
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.                                                               of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
    一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一                                                                                                   一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一 
has been licensed under GNU General Public License                                                                 has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁                                                          𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================一デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ 一======================================================================="""
