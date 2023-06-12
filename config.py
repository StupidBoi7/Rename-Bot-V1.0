import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25695562")

API_HASH = os.environ.get("API_HASH", "0b691c3e86603a7e34aae0b5927d725a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6280390519:AAGQOMWfbTJqpDeKs85EoHsWQTyrPFFElPw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "AnimeDownloaderChat_Bot", "Overflow_s") 

DB_NAME = os.environ.get("DB_NAME","mongodb+srv://vidoso7560:vidoso7560@cluster0.odwizw5.mongodb.net/?retryWrites=true&w=majority")     

DB_URL = os.environ.get("DB_URL","cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
