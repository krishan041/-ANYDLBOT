import os

class Config:
    SUPER7X_DLBOT_USERS = [6428531614]

    # Telegram bot credentials from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
    # API credentials from https://my.telegram.org/apps
    API_ID = int(os.environ.get("API_ID", "27536109"))
    API_HASH = os.environ.get("API_HASH", "b84d7d4dfa33904d36b85e1ead16bd63").strip()
    
    # Directory for downloads
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # File size limits
    MAX_FILE_SIZE = 50000000  # 50 MB
    TG_MAX_FILE_SIZE = 4194304000  # 4 GB
    FREE_USER_MAX_FILE_SIZE = 50000000  # 50 MB for free users

    # Chunk size for downloading/uploading files
    CHUNK_SIZE = 128  # 128 KB

    # Proxy settings (if required)
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "").strip()

    # Maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # Timeout settings
    PROCESS_MAX_TIMEOUT = 3600  # 1 hour

    # Owner/Administrator's Telegram ID
    OWNER_ID = int(os.environ.get("OWNER_ID", "6428531614"))

    # Bot session name
    SESSION_NAME = "UPLOADER-X-BOT"

    # Maximum results for search queries
    MAX_RESULTS = 50

    # Premium user settings (if applicable)
    PREMIUM_USER = os.environ.get("PREMIUM_USER", "6428531614").strip()

    # Chat base token
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "-1002447298131").strip()
