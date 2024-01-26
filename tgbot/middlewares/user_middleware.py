from telebot import TeleBot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.utils.database import Database


info_btn = InlineKeyboardButton(text="💁 User Info",callback_data='userInfo')
check_balance_btn = InlineKeyboardButton(text="💵 Balance",callback_data='balance')
today_consump_btn = InlineKeyboardButton(text="📈 Daily Usage",callback_data='dailyUsage')
see_usage_btn = InlineKeyboardButton(text="📊 Total Usage",callback_data='totalUsage')

keyboard = InlineKeyboardMarkup()
keyboard.add(info_btn,check_balance_btn,today_consump_btn,see_usage_btn)

def check_user(db:Database):
    def middleware_handler(bot:TeleBot,message:Message, *args, **kwargs) -> None:
        if message.text != '/start':
            return
        user = db.find_one(message.from_user.id)
        if not user:
            db.insert_one(message)
            bot.send_message(message.chat.id,text="Hello User 😊, Welcome to [POWER PULSE BOT](https://t.me/powerPusleBot) ✨✨",parse_mode="Markdown")
            bot.send_message(message.chat.id,text="🟢 Choose an Option 🟢",reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, text=f"Hello @{user.get('username')}, Welcome Back ✨✨",reply_markup=keyboard)

    return middleware_handler
    