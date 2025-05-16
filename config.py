# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", ""))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7216155592:AAEK_pmwjuehRju7-FjBGxTw7G1GD-QAJYQ")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("cobra_txtbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1843979302").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002650028673"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://namanjain123eudhc:opmaster@cluster0.5iokvxo.mongodb.net/?retryWrites=true&w=majority")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002650028673"))

