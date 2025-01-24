#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from config import Config
from pyrogram import Client as LazyDeveloper
from aiohttp import web
import asyncio

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def handle(request):
    return web.Response(text="Bot is running")

async def run_bot():
    try:
        # create download directory, if not exist
        if not os.path.isdir(Config.DOWNLOAD_LOCATION):
            os.makedirs(Config.DOWNLOAD_LOCATION)
        plugins = dict(root="plugins")
        Warrior = LazyDeveloper("@WebXBots",
                                bot_token=Config.BOT_TOKEN,
                                api_id=Config.API_ID,
                                api_hash=Config.API_HASH,
                                plugins=plugins)
        await Warrior.start()
        logger.info("Bot started successfully.")
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

async def main():
    try:
        app = web.Application()
        app.router.add_get('/', handle)

        port = int(os.environ.get("PORT", 8080))

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', port)
        await site.start()

        logger.info(f"Web server started on port {port}")
        await run_bot()
    except Exception as e:
        logger.error(f"Failed to start server: {e}")

if __name__ == "__main__":
    asyncio.run(main())
