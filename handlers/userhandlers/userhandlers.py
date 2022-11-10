from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from create import dp, bot
from config.config import *
from markups.usermarkups import create_markup, markup_start, create_inline_markup, navigator_callback
from state.userState import UserLogingState, update_state, UserReportState, UserOfferState, UserUpdateSettingsState,UserDialogWithAdmins
from state.categories import categories_view
from create import database
from .Other_functions import check_name_right, check_phone_right


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
            await UserLogingState.name.set()
    if isinstance(message, types.CallbackQuery):
        await message.message.answer(text_in_start_old_user, reply_markup=markup_start)


# function for check name in rules
async def name_validation(message: types.Message, state=FSMContext):
    name = await check_name_right(message)
    if isinstance(name, str):
        await state.update_data({"name":name})
        await message.answer(text_in_start_phone_number)
        await UserLogingState.next()


async def phone_validation(message: types.Message, state=FSMContext):
    phone = await check_phone_right(message)
    if isinstance(phone, str):
        await state.update_data({"phone": phone})
        data = await state.get_data()
        database.add_position(message.from_user.id, data["phone"], data["name"], "FALSE")
        await state.finish()
        await command_start(message)


# Get contact information about bot
async def contacts(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer(contacts_in_start)


async def create_inline_menu(message: types.Message):
    await message.delete()
    first_dir = message.text
    path = []
    first_index, first_cats = categories_view(categories, path, first_dir=first_dir)
    markup = create_inline_markup(first_cats, str(first_index))
    await message.answer(categories_messages[str(first_index)], reply_markup=markup)


# changing directory. callback_data current its a users way
async def walk_in_dirs(callback: types.CallbackQuery, callback_data: dict):
    functions = {
        "00": create_report_start,
        "01": new_offer_from_user,
        "100": request_for_telephone_call,
        "20": update_name,
        "21": update_phone_number,
        "11": dialog_with_admins
    }
    await callback.message.delete()
    print(callback_data["Current_path"])
    if not callback_data["Current_path"]:
        await command_start(callback)
    elif callback_data["Current_path"] in ["00", "01", "100", "20", "21","11"]:
        await functions[str(callback_data["Current_path"])](callback, callback_data)
    else:
        cats = categories_view(categories, callback_data["Current_path"])
        markup = create_inline_markup(cats, callback_data["Current_path"])
        answer = categories_messages[callback_data["Current_path"]].replace("\|phone\| ",\
        f"__\+{str(database.read_data(callback.from_user.id)[0][1])}__") if callback_data["Current_path"]== "10" else \
            categories_messages[callback_data["Current_path"]]
        await callback.message.answer(answer, reply_markup=markup)


async def create_report_start(callback: types.CallbackQuery, callback_data: dict):
    await UserReportState.address.set()
    cats = categories_view(categories, callback_data["Current_path"])
    markup = create_inline_markup(cats, callback_data["Current_path"])
    print(markup, type(markup))
    await callback.message.answer(categories_messages[callback_data["Current_path"]], reply_markup=markup)

# catching callbacks in state UserReportState in send report menu
async def report_callbacks(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    print(callback_data)
    if callback_data["Current_path"] == "0":
        await state.finish()
        await walk_in_dirs(callback, callback_data)
    else:
        states = {
            "00": UserReportState.address,
            "000": UserReportState.photo,
            "0000": UserReportState.reason
            }
        await state.set_state(states[callback_data["Current_path"]])
        cats = categories_view(categories, callback_data["Current_path"])
        markup = create_inline_markup(cats, callback_data["Current_path"])
        await callback.message.answer(categories_messages[callback_data["Current_path"]], reply_markup=markup)


async def report_address(message: types.Message, state: FSMContext):
    await state.update_data({"address": message.text})
    cats = categories_view(categories, "000")
    markup = create_inline_markup(cats, "000")
    await message.answer(categories_messages["000"], reply_markup=markup)
    await UserReportState.next()


async def report_photo_check_type(message: types.Message, state: FSMContext):
    await message.answer(bad_message_in_report)


async def report_photo(message: types.Message, state: FSMContext):
    await state.update_data({"photo": message.photo[-1].file_id})
    cats = categories_view(categories, "0000")
    markup = create_inline_markup(cats, "0000")
    await message.answer(categories_messages["0000"], reply_markup=markup)
    await UserReportState.next()


async def report_reason(message: types.Message, state: FSMContext):
    await state.update_data({"message": message.text})
    report_data = await state.get_data()   # from this data generating messages from admins
    await state.finish()
    await message.answer(report_success_message)


async def new_offer_from_user(callback: types.CallbackQuery, callback_data: dict):
    await UserOfferState.offer.set()
    cats = categories_view(categories, callback_data["Current_path"])
    markup = create_inline_markup(cats, callback_data["Current_path"])
    await callback.message.answer(categories_messages[callback_data["Current_path"]], reply_markup=markup)


async def new_offer_from_user_register(message: types.Message, state: FSMContext):
    await state.update_data({"offer": message.text})
    offer_data = await state.get_data()  # from this data generating messages from admins about new offer
    await state.finish()
    await message.answer(offer_success_message)


async def new_offer_from_user_register_bad(message: types.Message, state: FSMContext):
    await message.answer(bad_offer_message)


async def request_for_telephone_call(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.answer(answer_in_telephone_call)
    #create some for send telephone number to admin group


async def update_phone_number(callback: types.CallbackQuery, callback_data: dict):
    await UserUpdateSettingsState.New_Phone.set()
    cats = categories_view(categories, callback_data["Current_path"])
    markup = create_inline_markup(cats, callback_data["Current_path"])
    await callback.message.answer(categories_messages[callback_data["Current_path"]], reply_markup=markup)


async def update_phone_number_catch(message: types.Message, state: FSMContext):
    phone = await check_phone_right(message)
    if isinstance(phone, str):
        await state.update_data({"New_phone": message.text})
        new_phone = await state.get_data()
        await state.finish()
        await message.answer(phone_update_settings_success)
        database.edit_position(message.from_user.id, "userphone", new_phone["New_phone"])



async def update_name(callback: types.CallbackQuery, callback_data: dict):
    await UserUpdateSettingsState.New_Name.set()
    cats = categories_view(categories, callback_data["Current_path"])
    markup = create_inline_markup(cats, callback_data["Current_path"])
    await callback.message.answer(categories_messages[callback_data["Current_path"]], reply_markup=markup)


async def update_name_catch(message: types.Message, state: FSMContext):
    name = await check_name_right(message)
    if isinstance(name, str):
        await state.update_data({"New_name": message.text})
        new_name = await state.get_data()
        await state.finish()
        await message.answer(phone_update_settings_success)
        database.edit_position(message.from_user.id, "username", new_name["New_name"])


async def dialog_with_admins(callback: types.CallbackQuery, callback_data: dict):
    await UserDialogWithAdmins.messages.set()
    cats = categories_view(categories, callback_data["Current_path"])
    markup = create_inline_markup(cats, callback_data["Current_path"])
    await callback.message.answer(categories_messages[callback_data["Current_path"]], reply_markup=markup)

async def messages_replier(message: types.Message, state: FSMContext):
    print(message.text)


async def stop_dialog_with_admins(callback: types.CallbackQuery, callback_data: dict,state =FSMContext):
    await state.finish()
    await callback.message.answer(stop_dialog_with_admins_message)



def register_user_handlers(dp:  Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(name_validation, state=UserLogingState.name)
    dp.register_message_handler(phone_validation, state=UserLogingState.phone)
    dp.register_message_handler(contacts, lambda message: "Полезные контакты" in message.text)
    dp.register_message_handler(create_inline_menu, filters.Text(["⛔ Оставить заявку", "📞 Связаться", "⚙️ Настройки",
                                                                  "☎ Полезные контакты"]))
    dp.register_callback_query_handler(report_callbacks, navigator_callback.filter(), state=[UserReportState.address,
                                                                                             UserReportState.reason,
                                                                                             UserReportState.photo,
                                                                                             UserOfferState.offer])
    dp.register_message_handler(report_address, state=UserReportState.address)
    dp.register_message_handler(report_photo_check_type, state=UserReportState.photo)
    dp.register_message_handler(report_photo, state=UserReportState.photo, content_types=["photo"])
    dp.register_message_handler(report_reason, state=UserReportState.reason)

    dp.register_message_handler(new_offer_from_user_register, state=UserOfferState.offer)
    dp.register_message_handler(new_offer_from_user_register_bad, state=UserOfferState.offer, content_types=["photo",
                                                                                                         "video"])
    dp.register_message_handler(update_phone_number_catch, state=UserUpdateSettingsState.New_Phone)
    dp.register_message_handler(update_name_catch, state=UserUpdateSettingsState.New_Name)
    dp.register_message_handler(messages_replier, state=UserDialogWithAdmins.messages)
    dp.register_callback_query_handler(stop_dialog_with_admins, navigator_callback.filter(), state=UserDialogWithAdmins.messages)
    dp.register_callback_query_handler(walk_in_dirs, navigator_callback.filter())
