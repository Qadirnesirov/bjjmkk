from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgAdb_bgtvdTdnHPk9OHTGfoTU1aXnby2Czyc_iL3dUPkZddfJMtGnbGjxB5R6KbgbB7QeNKwWep4tWrd2naID2l20sw8Zn04xOOZewizyfdY14-wSqq9a0pTP3VrupB0lfkp-wa7Yhj36f9wkUaNZhQp_MyBl-W6d-8Dkms4_SmR2ZPHHv6NkFXVNx8OTYfdc8rX3eOduxwxczweltQumGBw1kg5H227F77iObLBgr1oAZ-kWsHIAtSdd12KKS2wm3fmB8izX59ruwzDalfoGKYKHLxaRDnJpLNGB_Zgz3TB8ZRna1S_RgWBBaHRxppkAokPfWYhR2r8NnIzVY8fo9pceHPDgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5910888289:AAF9HXtyMilAg4s4tl2W2xiXMIOOZbw-XWo")
BOT_NAME = getenv("BOT_NAME", "TaliaMüzik") 
API_ID = int(getenv("API_ID", "8953338"))
API_HASH = getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")
BOT_USERNAME = getenv("BOT_USERNAME", "Efsanestar_bot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8823666").split()))
