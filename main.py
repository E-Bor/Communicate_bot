from aiogram.utils import executor
from create import dp
from handlers import register_user_handlers, register_admin_handlers

register_admin_handlers(dp)
register_user_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


