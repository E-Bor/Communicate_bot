from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from create import dp, bot
from config.config import *
from markups.usermarkups import create_markup, markup_start, create_inline_markup
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
    update_fsm = await state.get_data()
    a = update_fsm["current_state"].copy()
    a.pop(-1)
    await state.reset_data()
    await state.update_data(current_state=a)
    new_state = Dispatcher.get_current().current_state()

    if not a:
        await state.finish()
        await callback.message.delete()
        await command_start(callback)
    else:
        await change_category(callback, new_state)


# Start with request button
async def request(message: types.Message, state: FSMContext):
    await message.delete()
    await UserState.current_state.set()
    state = Dispatcher.get_current().current_state()
    await state.update_data(current_state=["request"])
    markup = create_inline_markup(["⛔Оставить заявку", "💡Поделиться предложением" ])
    await message.answer(categories_messages["['request]"], reply_markup=markup)


# Start with connect button
async def connect(message: types.Message, state: FSMContext):
    await message.delete()
    await UserState.current_state.set()
    state = Dispatcher.get_current().current_state()
    await state.update_data(current_state=["connect"])
    markup = create_inline_markup(["📞 Перезвоните мне", "📞 Свяжитесь со мной в чат-боте"])
    await message.answer(categories_messages["['connect']"], reply_markup=markup)


# Start with settings button
async def settings(message: types.Message, state: FSMContext):
    await message.delete()
    await UserState.current_state.set()
    state = Dispatcher.get_current().current_state()
    await state.update_data(current_state=["settings"])
    markup = create_inline_markup(["🛠Поменять имя", "🛠Сменить номер"])
    await message.answer(categories_messages["['settings']"], reply_markup=markup)


# Swap categories_view in all bot
async def change_category(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    a = await update_state(state, "current_state", callback.data)
    markup = create_inline_markup(categories_view(categories, a))
    await callback.message.answer(categories_messages[str(a)], reply_markup=markup)






def register_user_handlers(dp:  Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(contacts, lambda message: "Полезные контакты" in message.text,
                                )
    dp.register_message_handler(request, lambda message: "⛔ Оставить заявку" in message.text,
                                )
    dp.register_message_handler(connect, lambda message: "📞 Связаться" in message.text,
                                )
    dp.register_message_handler(settings, lambda message: "⚙️ Настройки" in message.text,
                                )
    dp.register_callback_query_handler(button_back, lambda callback: "🔙Назад" in callback.data, state=UserState.current_state
                                )
    dp.register_callback_query_handler(change_category, state=UserState.current_state)
