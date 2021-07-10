from . import *
import shutil
Client.start()
LOGS.info(SI)
idle()
try:
    shutil.rmtree(K)
    shutil.rmtree(P)
    shutil.rmtree(V)
    shutil.rmtree(Y)
    shutil.rmtree(M)
except:
    pass
Client.stop()
LOGS.info(SE)