from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# API By Harshith || https://t.me/MutyalaHarshith
LOGO_API_URL1 = "https://harshithapi.herokuapp.com/logo?text="

LOGO_API_URL2 = "https://harshithapi.herokuapp.com/logo?square=true&text="
