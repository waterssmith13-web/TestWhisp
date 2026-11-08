from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("9047407190:AAFjkuIscghTXhLbc5QBGm2AUF-qHp66oNc")  # Bot token
ADMINS = env.list("923996862")  # adminlar ro'yxati
IP = env.str("localhost")  # Xosting ip manzili
