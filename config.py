from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgC79hVl6TVbSiD6RZ-Imun9xuq7o6G5c_yesbCKsINn7Hxyi5YCOYyIk28DqO1aYIM0QPZi6cZkuzjB8q6Xd25hNPdnMI3x0f7IV3B9Y4oLJCeeHMa6vsw4qUM2WE_fQvWJXtyP2SFeCVK-34t3klcKljQ8wzDItjTxzeawwh74IODtMMmNTrwzfoof7BGvS5daMAIP9rGuUm-RRhEm9Yh2EwNiK4Cu1Qf0x1R3ptwfTIbbBsknEwb5HxPQauz5Q2XRy5Trl4N9UvEZqzX1iitPSmUsf2POY6jjdNpyqyw5MDtVTjENzXvWU0Kftr_4QeQrpgOfCvBZu6AF6cjR0G_CAAAAAVWiAQ0A")
BOT_TOKEN = getenv("BOT_TOKEN", "5910888289:AAF9HXtyMilAg4s4tl2W2xiXMIOOZbw-XWo")
BOT_NAME = getenv("BOT_NAME", "TaliaMüzik") 
API_ID = int(getenv("API_ID", "8953338"))
API_HASH = getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")
BOT_USERNAME = getenv("BOT_USERNAME", "Efsanestar_bot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8823666").split()))
