import os
import ffmpeg
import asyncio
from ꜰɪɴx import *
from ʏȶʟʍӼ import *
from pyrogram.types import Message
from pyrogram import Client as ɦɛʊʟ, filters, StopPropagation

@ɦɛʊʟ.on_message(
filters.private
& filters.regex(DY))
async def mscgetter(_,ytrgx: Message):
    await mscupldr(ytrgx)   
async def mscupldr(ytrgx: Message):
    await ytrgx.reply_chat_action(PL)
    try:
        VMft = ydl.extract_info(ytrgx.text, download=True)
        if VMft['duration'] > KTM:
            push = await ytrgx.reply_photo(YMGI,
            reply_markup=JOIN_BUTTLOCK,
            caption=CAP_NO)
            await delete_server((push,ytrgx),30)
            await push.delete()
            return
        d_status = await ytrgx.reply_text(FT,
        quote=True,
        disable_notification=False)
        ydl.process_info(VMft)
        audio_file = ydl.prepare_filename(VMft)
        task = asyncio.create_task(audio_sender(ytrgx, VMft,audio_file))
        await ytrgx.reply_chat_action("record_video")
        await d_status.delete()
        while not task.done():
            await asyncio.sleep(1)
            await ytrgx.reply_chat_action("playing")
        await ytrgx.reply_chat_action("cancel")
        if ytrgx.chat.type == "private":
            await ytrgx.delete()
    except Exception as e:
        await ytrgx.reply_text(repr(e))
        
async def audio_sender(ytrgx: Message, VMft, audio_file):
    basename = audio_file.rsplit(".", 1)[-2]
    if VMft['ext'] == 'webm':
        audio_file_opus = basename + ".opus"
        ffmpeg.input(audio_file).output(audio_file_opus, codec="copy").run()
        os.remove(audio_file)
        audio_file = audio_file_opus
    thumbnail_url = VMft['thumbnail']
    if os.path.isfile(basename + KJP):
        img_room = basename + KJP
    else:
        img_room = basename + "." + \
            file_url(thumbnail_url)
    resized_img = basename + RSQG
    reshpSq(img_room, resized_img)
    webpage_url = VMft['webpage_url']
    title = VMft['title']
    duration = int(float(VMft['duration']))
    performer = VMft['uploader']
    if os.path.isfile(basename + KJP):
        Simg_room = basename + KJP
    else:
        Simg_room = basename + "." + \
            file_url(thumbnail_url)
    Sresized_img = basename + NRSQG
    reshpSq(Simg_room, Sresized_img)
    void = await ytrgx.reply_photo(
        Sresized_img,
        caption=f'''✨🤩 𝙽𝚒𝚌𝚎 𝚌𝚑𝚘𝚒𝚌𝚎! 
🛒𝚈𝚘𝚞𝚛 𝙰𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚑𝚎𝚛𝚎 𝚜𝚑𝚘𝚛𝚝𝚕𝚢
TITLE: `{title}`
WEBPAGE: {webpage_url}

一═デ⭕️𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐌𝐮𝐬𝐢𝐜 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫⭕️デ═一
''',
        parse_mode='markdown',
        )

    await ytrgx.reply_audio(
        audio_file,
        reply_markup=JOIN_BUTTLOCK2,
        caption=kbbk,
        title=title,
        performer=performer,
        duration=duration,
        thumb=resized_img
        )
    os.remove(audio_file)
    os.remove(img_room)
    os.remove(resized_img)
    os.remove(Sresized_img) 
    return StopPropagation