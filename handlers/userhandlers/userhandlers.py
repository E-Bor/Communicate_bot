from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from create import dp, bot
from config.config import *
from markups.usermarkups import create_markup, markup_start, create_inline_markup, navigator_callback
from state.userState import UserLogingState, update_state
from state.categories import categories_view
from create import database
from Other_functions import check_name_right


# command start
async def command_start(message: types.Message | types.CallbackQuery):
    # print(database.check_user(message.chat.id))
    if isinstance(message, types.Message):
        if database.check_user(message.chat.id) == "Ban":
            await message.answer("Вы забанены Администратором")
        if database.check_user(message.chat.id) == 1:
            await message.answer(text_in_start_old_user, reply_markup=markup_start)
        if database.check_user(message.chat.id) == 0:
            await message.answer(text_in_start_new_user)
            await UserLogingState.name_state.set()
    if isinstance(message, types.CallbackQuery):
        await message.message.answer(text_in_start_old_user, reply_markup=markup_start)

async def name_validation(message: types.Message, state=FSMContext):
    name = check_name_right(message)
    if name is not None:
        print("guud name")




# Get contact information about bot
async def contacts(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer(contacts_in_start)


async def create_inline_menu(message: types.Message):
    await message.delete()
    first_dir = message.text
    path = []
    first_index, first_cats = categories_view(categories, path, first_dir=first_dir)
    markup = create_inline_markup(first_cats, first_index)
    await message.answer(categories_messages[str(first_index)], reply_markup=markup)



async def walk_in_dirs(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.delete()
    if not callback_data["Current_path"]:
        await command_start(callback)

    else:
        cats = categories_view(categories, callback_data["Current_path"])
        markup = create_inline_markup(cats, callback_data["Current_path"])
        await callback.message.answer(categories_messages[callback_data["Current_path"]], reply_markup=markup)


def register_user_handlers(dp:  Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(name_validation, state=UserLogingState.name_state)
    dp.register_message_handler(contacts, lambda message: "Полезные контакты" in message.text)
    dp.register_message_handler(create_inline_menu, filters.Text(["⛔ Оставить заявку", "📞 Связаться", "⚙️ Настройки",
                                                                  "☎ Полезные контакты"]))

    dp.register_callback_query_handler(walk_in_dirs, navigator_callback.filter())
