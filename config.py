from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/08f1061f32fc52b45a722.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/08f1061f32fc52b45a722.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/WOODcraft_Mirror_Topic")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Opleech")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5827766615,6104498512").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
