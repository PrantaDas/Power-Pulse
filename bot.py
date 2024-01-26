# filters
from tgbot.filters.admin_filters import AdminFilter

# handlers
from tgbot.handlers.user import any_user, handle_info

# middlewares
from tgbot.middlewares.antiflood_middleware import antispam_func
from tgbot.middlewares.user_middleware import check_user

# utils
from tgbot.utils.database import Database

# telebot
from telebot import TeleBot

# config
from tgbot import config

# api helper
from telebot import apihelper

# initiate db
db = Database()

# enabling middleware
apihelper.ENABLE_MIDDLEWARE = True

# checking for bot token
if not config.BOT_TOKEN:
    raise ValueError("Bot token is missing")

# initiate the bot instance
bot = TeleBot(config.BOT_TOKEN, num_threads = 10)

# registering the handlers
def register_handler():
    bot.register_message_handler(any_user, commands=['start','hi','hello','hey'], admin=False, pass_bot=True)
    bot.register_callback_query_handler(handle_info(bot,db),func=lambda call:True)

register_handler()

# registering middlewares
bot.register_middleware_handler(antispam_func,update_types=['message'])
bot.register_middleware_handler(check_user(db), update_types=['message'])

# custom filters
bot.add_custom_filter(AdminFilter())

def run() -> None:
    try:
        print("=> All environments are loaded")
        print("=> Bot started")
        bot.infinity_polling()

    except KeyboardInterrupt as e:
        # Handle the KeyboardInterrupt gracefully
        print(f"KeyboardInterrupt: {e}")
    
    except Exception as e:
        # Handle any other unexpected exception
        print(f"Exception: {e}")


if __name__ == '__main__':
    run()