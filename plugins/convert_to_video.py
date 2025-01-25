#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase
from helper_funcs.display_progress import progress_for_pyrogram

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
# https://stackoverflow.com/a/37631799/4723940
from PIL import Image

# Removed pydrive import and related code

# Rest of the code remains unchanged

@pyrogram.Client.on_message(pyrogram.filters.command(["converttovideo"]))
async def convert_to_video(bot, message):
    TRChatBase(message.from_user.id, message.text, "converttovideo")
    if str(message.from_user.id) not in Config.SUPER3X_DLBOT_USERS:
        await bot.send_message(
            chat_id=message.chat.id,
            text=Translation.NOT_AUTH_USER_TEXT,
            reply_to_message_id=message.id
        )
        return
    if message.reply_to_message is not None:
        description = Translation.CUSTOM_CAPTION_UL_FILE
        download_location = Config.DOWNLOAD_LOCATION + "/"
        a = await bot.send_message(
            chat_id=message.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=message.id
        )
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=message.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(Translation.DOWNLOAD_START, a.id, message.chat.id, c_time)
        )
        if the_real_download_location is not None:
            await bot.edit_message_text(
                text=Translation.SAVED_RECVD_DOC_FILE,
                chat_id=message.chat.id,
                message_id=a.id
            )
            # don't care about the extension
            await bot.edit_message_text(
                text=Translation.UPLOAD_START,
                chat_id=message.chat.id,
                message_id=a.id
            )
            logger.info(the_real_download_location)
            # get the correct width, height, and duration for videos greater than 10MB
            # ref: message from @BotSupport
            width = 0
            height = 0
            duration = 0
            metadata = extractMetadata(createParser(the_real_download_location))
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(message.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                thumb_image_path = None
            else:
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                # get the correct width, height, and duration for videos greater than 10MB
                # resize image
                # ref: https://t.me/PyrogramChat/44663
                # https://stackoverflow.com/a/21669827/4723940
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                # https://stackoverflow.com/a/37631799/4723940
                # img.thumbnail((90, 90))
                img.resize((90, height))
                img.save(thumb_image_path, "JPEG")
                # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
            # try to upload file
            c_time = time.time()
            await bot.send_video(
                chat_id=message.chat.id,
                video=the_real_download_location,
                caption=description,
                duration=duration,
                width=width,
                height=height,
                supports_streaming=True,
                # reply_markup=reply_markup,
                thumb=thumb_image_path,
                reply_to_message_id=message.reply_to_message.id,
                progress=progress_for_pyrogram,
                progress_args=(
                    Translation.UPLOAD_START, a.id, message.chat.id, c_time
                )
            )
            try:
                os.remove(the_real_download_location)
                os.remove(thumb_image_path)
            except:
                pass
            await bot.edit_message_text(
                text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                chat_id=message.chat.id,
                message_id=a.id,
                disable_web_page_preview=True
            )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=Translation.REPLY_TO_DOC_FOR_C2V,
            reply_to_message_id=message.id
          )
