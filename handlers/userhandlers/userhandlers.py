from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from create import dp, bot
from config.config import *
from markups.usermarkups import create_markup, markup_start, create_inline_markup, navigator_callback
from state.userState import UserState, update_state
from state.categories import categories_view
from aiogram.types import ReplyKeyboardRemove


# command start
async def command_start(message: types.Message):
    # сделать проверку на существование пользователя по id телеграмма
    if isinstance(message, types.Message):
        await message.answer(text_in_start_old_user, reply_markup=markup_start)
    # сделать регистрацию пользователя в боте
    if isinstance(message, types.CallbackQuery):
        await message.message.answer(text_in_start_old_user, reply_markup=markup_start)

# Get contact information about bot
async def contacts(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer(contacts_in_start)


# Go back in categories
async def button_back(callback: types.CallbackQuery, state: FSMContext):
    pass


# # Start with request button
# async def request(message: types.Message, state: FSMContext):
#     await message.delete()
#     markup = create_inline_markup(["⛔Оставить заявку", "💡Поделиться предложением" ])
#     await message.answer(categories_messages["['request]"], reply_markup=markup)
#
#
# # Start with connect button
# async def connect(message: types.Message, state: FSMContext):
#     await message.delete()
#     await UserState.current_state.set()
#     state = Dispatcher.get_current().current_state()
#     await state.update_data(current_state=["connect"])
#     markup = create_inline_markup(["📞 Перезвоните мне", "📞 Свяжитесь со мной в чат-боте"])
#     await message.answer(categories_messages["['connect']"], reply_markup=markup)
#
#
# # Start with settings button
# async def settings(message: types.Message, state: FSMContext):
#     await message.delete()
#     await UserState.current_state.set()
#     state = Dispatcher.get_current().current_state()
#     await state.update_data(current_state=["settings"])
#     markup = create_inline_markup(["🛠Поменять имя", "🛠Сменить номер"])
#     await message.answer(categories_messages["['settings']"], reply_markup=markup)



async def create_inline_menu(message: types.Message):
    await message.delete()
    first_dir = message.text
    path = []
    first_index, first_cats = categories_view(categories, path, first_dir=first_dir)
    markup = create_inline_markup(first_cats, first_index)

    # Примерработы с категорями
    # parent_category = [1, 0]
    # cats = categories_view(categories, parent_category)
    # print(cats)
    # markup = create_inline_markup(cats, parent_category)
    await message.answer("hello", reply_markup=markup)


async def walk_in_dirs(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer()
    print(callback_data)






def register_user_handlers(dp:  Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(contacts, lambda message: "Полезные контакты" in message.text,
                                 )
    # dp.register_message_handler(request, lambda message: "⛔ Оставить заявку" in message.text,
    #                             )
    # dp.register_message_handler(connect, lambda message: "📞 Связаться" in message.text,
    #                             )
    # dp.register_message_handler(settings, lambda message: "⚙️ Настройки" in message.text,
    #                             )
    # dp.register_callback_query_handler(button_back, lambda callback: "🔙Назад" in callback.data, state=UserState.current_state
    #                             )
    # dp.register_callback_query_handler(change_category, state=UserState.current_state)
    dp.register_message_handler(create_inline_menu, filters.Text(["⛔ Оставить заявку", "📞 Связаться", "⚙️ Настройки",
                                                                  "☎ Полезные контакты"]))

    dp.register_callback_query_handler(walk_in_dirs, navigator_callback.filter())
