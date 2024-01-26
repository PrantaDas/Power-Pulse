from telebot import TeleBot
from telebot.types import Message, CallbackQuery
import requests as req
from tgbot import config
from tgbot.utils.utils import format_user_info
from tgbot.utils.database import Database
from datetime import datetime, timedelta

def any_user(message:Message, bot:TeleBot) -> None:
    """
    Handle messages from any user.

    Parameters:
    - message (Message): The message object received from the user.
    - bot (TeleBot): The TeleBot instance.

    Returns:
    None
    """
    return

def handle_info(bot:TeleBot, db:Database):
    """
    Handle user information queries and related actions.

    Parameters:
    - bot (TeleBot): The TeleBot instance.
    - db (Database): The Database instance for user data storage.

    Returns:
    Callable: Function to handle user information queries.
    """
    def get_user_info(call:CallbackQuery):
        """
        Get and display user information based on the callback query.

        Parameters:
        - call (CallbackQuery): The callback query received.

        Returns:
        None
        """
        user = db.find_one(call.from_user.id)
        acc_no = user.get('acountNo')
        if call.data =='userInfo':
            if acc_no is not None:
                res = req.get(f"{config.DESKO_BASE_URL}/tkdes/customer/getCustomerInfo?accountNo={acc_no}")
                if res.json()['data'] == None:
                    bot.send_message(call.message.chat.id, "❌ User not found. Please try again.")
                    return
                if res.status_code == 200:
                    message_to_send =  format_user_info(res.json()['data'])
                    bot.send_message(call.message.chat.id, text=message_to_send,parse_mode='HTML')
                    return
                else:
                    bot.send_message(call.message.chat.id, "❌ Error fetching customer information. Please try again.")
                    return
            else:
                sent_message = bot.send_message(call.message.chat.id, text="🔓 Give your account number:")
                bot.register_next_step_handler(sent_message,get_account_number(bot,db))
                return
        if call.data == 'balance':
            if call.data == 'balance':
                res_bal = req.get(f"{config.DESKO_BASE_URL}/tkdes/customer/getBalance?accountNo={acc_no}")
                if not res_bal.json()['data']:
                    bot.send_message(call.message.chat.id, "❌ Error fetching customer information. Please try again.")
                    return
                else:
                    message_text = """
                        <b>🔢 Account No: {accountNo}</b>
                        <b>📋 Meter No: {meterNo}</b>
                        <b>💵 Balance: {balance} Taka</b>
                        <b>💵 Current Month Consumption: {currentMonthConsumption} Taka</b>
                        <b>📅 Reading Time: {readingTime}</b> 
                        """
                    bot.send_message(call.message.chat.id, message_text.format(**res_bal.json()['data']),parse_mode='HTML')
                    return
        
        if call.data == 'dailyUsage':
            today_date = str((datetime.now() - timedelta(days=1)).date())
            res_daily = req.get(f"{config.DESKO_BASE_URL}/tkdes/customer/getCustomerDailyConsumption?accountNo={acc_no}&meterNo=&dateFrom={today_date}&dateTo={today_date}")
            res_data = res_daily.json()['data']
            msg_data = """
                        <b>📈  Consumed Unit : {consumedUnit} Unit</b>
                        <b>💵 Consumed Taka: {consumedTaka} Taka</b>
            """
            formated_text = msg_data.format(**res_data[0])
            bot.send_message(call.message.chat.id,formated_text,parse_mode='HTML')
            return
        else :
            bot.send_message(call.message.chat.id,"Feature is coming Soon")
            return

    return get_user_info

def get_account_number(bot:TeleBot,db:Database):
    """
    Prompt user to provide an account number and fetch information.

    Parameters:
    - bot (TeleBot): The TeleBot instance.
    - db (Database): The Database instance for user data storage.

    Returns:
    Callable: Function to handle fetching information based on the provided account number.
    """
    def fetch_info(message:Message):
        """
        Fetch and display user information based on the provided account number.

        Parameters:
        - message (Message): The message object containing the account number.

        Returns:
        None
        """
        account = message.text
        data = {
            "acountNo":account
        }
        db.update(message.from_user.id,data)
        res = req.get(f"{config.DESKO_BASE_URL}/tkdes/customer/getCustomerInfo?accountNo={account}")
        if res.json()['data'] == None:
            bot.send_message(message.chat.id, "❌ User not found. Please try again.")
            return
        if res.status_code == 200:
            message_to_send =  format_user_info(res.json()['data'])
            bot.send_message(message.chat.id, text=message_to_send,parse_mode='HTML')
            return
        else:
            bot.send_message(message.chat.id, "❌ Error fetching customer information. Please try again.")
            return

    
    return fetch_info

