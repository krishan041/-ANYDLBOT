#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from config import Config
from pyrogram import Client as LazyDeveloper
from aiohttp import web

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def handle(request):
    return web.Response(text="Bot is running")

if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = LazyDeveloper("@WebXBots",
                            bot_token=Config.BOT_TOKEN,
                            api_id=Config.API_ID,
                            api_hash=Config.API_HASH,
                            plugins=plugins)
    
    app = web.Application()
    app.router.add_get('/', handle)
    
    port = int(os.environ.get("PORT", 8080))
    web.run_app(app, port=port)
    
    Warrior.run()
