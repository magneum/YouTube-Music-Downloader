from . import *
import shutil

Client = Client(
    HS,
    api_id=Feros.APP_ID,
    api_hash=Feros.API_HASH,
    bot_token=Feros.BOT_TOKEN,
    workers=12,
    plugins=PYT
)

Client.start()
LOGS.info(SI)
idle()
Client.stop()
try:
    shutil.rmtree(K)
    shutil.rmtree(P)
    shutil.rmtree(V)
    shutil.rmtree(Y)
    shutil.rmtree(M)
except:
    pass
LOGS.info(SE)