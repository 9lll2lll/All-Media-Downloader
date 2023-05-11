import os




class Config((object)):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6153192492:AAHdhacQxEemZnRChKZp6B943NEV2_ytAZM")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", "6817364"))
    API_HASH = os.environ.get("API_HASH", "b2aea0b75ceca34bf5333107ac526c02")
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = {int(x) for x in os.environ.get("BANNED_USERS", "").split()}
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # The download location for auth users.

    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = None  # os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "887108671"))
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "1ApWapzMBu3ovTJgp-xdmo-ujOni9vM7vShRpcLW609aJCmM0_y6NDbko5PEJm4vzVVavZX74fkKxbMnMyQMxEwX5W-hAjqjpW2u-miMryZSaYNY36Iu9nfd2yPJyYLet5yUhksCtMRL-0dvYjgpKX5xuhkXn-fQBY5QGvXR97IIh64mzkxXr6KlVq0skdTyoTZwiVafSnDXucoJLIFlhSiP3QrlaWS-9J2DFhjd35M_fj14xGeDWk60Lz8jLaevOQPS6hrQgCx8nJEGfi-XeWlRaJLWN52pKomu1Njm0wqaXgjgdFBFoQ38x24uOP5YNSqJ0UONTb9aLJ4eYVo57awmOfVY6LBk=")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://lrflagmx:gru1ZYyrI-bLMLckQRXogSixUSq2DFRB@arjuna.db.elephantsql.com/lrflagmx")
    PROCESS_TEXT = """
    Process: {}
    """
    LOGGED_AS_USER = """
    Successfully Logged Into Mega.nz User Account
    """
    LOGIN_ERROR_TEXT = """
    Can't Get Mega Email and Password Login as an Anonymouse User
    """

    ERROR_TEXT = """ 
    Log: {}
    Save the Log file and Send it to @Nexa_bots for Help :)
    """

    
