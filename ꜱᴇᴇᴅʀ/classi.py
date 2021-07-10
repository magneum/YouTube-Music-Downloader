import os
class Feros(object):
    LOGGER = True
    ENV = bool(os.environ.get("HEROKU", False))
    API_HASH = os.environ.get("API_HASH",
    None)
    APP_ID = os.environ.get("APP_ID",
    None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN",
    None)
    HYTM_KEY = os.environ.get("HYTM_KEY")
class YTGX(Feros):
    LOGGER = True
    
DM = "knite"