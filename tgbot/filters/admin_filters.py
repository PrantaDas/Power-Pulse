from telebot.custom_filters import SimpleCustomFilter
from ..models.user_models import Admin


class AdminFilter(SimpleCustomFilter):
    """
    Filter for admin users
    """
    key = 'admin'
    def check(self, message):
        return int(message.chat.id) == int(Admin.ADMIN.value)