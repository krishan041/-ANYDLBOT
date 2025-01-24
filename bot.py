#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from aiohttp import web
import asyncio
from config import Config
from pyrogram import Client

# Logging setup
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Web handler
async def handle(request):
    return web.Response(text="Bot is running")

# Bot initialization and startup
async def start_bot():
    try:
        # Ensure download directory exists
        if not os.path.isdir(Config.DOWNLOAD_LOCATION):
            os.makedirs(Config.DOWNLOAD_LOCATION)

        # Plugin configuration
        plugins = dict(root="plugins")

        # Initialize the bot
        bot = Client(
            "my_bot",  # This is the session name
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            plugins=plugins
        )
        
        # Start the bot
        await bot.start()
        logger.info("Bot started successfully.")
        await asyncio.Event().wait()  # Keep the bot running
    except Exception as e:
        logger.error(f"Error while starting the bot: {e}")
        raise

# Web server initialization
async def start_server():
    try:
        app = web.Application()
        app.router.add_get("/", handle)

        port = int(os.environ.get("PORT", 8080))  # Default port: 8080
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", port)
        await site.start()

        logger.info(f"Web server running on port {port}")
    except Exception as e:
        logger.error(f"Error while starting the web server: {e}")
        raise

# Main function to run both the bot and server
async def main():
    try:
        await asyncio.gather(
            start_server(),  # Start web server
            start_bot()      # Start Telegram bot
        )
    except Exception as e:
        logger.error(f"Error in main: {e}")

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
