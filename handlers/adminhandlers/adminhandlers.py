from aiogram import Bot, types, Dispatcher
from create import dp, bot
from config.config import ADMINS_ID, PATH
from database.database import UserData
from aiogram.utils.exceptions import ChatNotFound
loaded_id = []


def read_write_chat_info(path: str, new_id: str):
    list_id = list()
    with open(path, "r+") as f:
        for i in f:
            list_id.append(i.strip())
    with open(path, "w+") as f:
        if new_id not in list_id:
            list_id.append(str(new_id))
        for i in list_id:
            f.write(f"{i}\n")
    return list_id

def update_chats_id():
    path = ["\\config\\admin_chatlist","\\config\\offer_chatlist","\\config\\report_chatlist"]
    all_id = list()
    for i in path:
        current_list = list()
        with open(PATH+i, "r+") as f:
            for j in f:
                current_list.append(j.strip())
        all_id.append(current_list)
    global loaded_id
    loaded_id = all_id


async def start_admin_group(message: types.Message):
    new_admin_chat = str(message.chat.id)
    path_to_admin_groups = PATH+"\\config\\admin_chatlist"
    read_write_chat_info(path_to_admin_groups, new_admin_chat)
    await message.answer("Этот чат успешно добавлен в список чатов для админов")
    update_chats_id()


async def start_offer_group(message: types.Message):
    new_offer_chat = str(message.chat.id)
    path_to_admin_groups = PATH + "\\config\\offer_chatlist"
    read_write_chat_info(path_to_admin_groups, new_offer_chat)
    await message.answer("Этот чат успешно добавлен в список чатов для предложений")
    update_chats_id()


async def start_report_group(message: types.Message):
    new_report_chat = str(message.chat.id)
    path_to_admin_groups = PATH + "\\config\\report_chatlist"
    read_write_chat_info(path_to_admin_groups, new_report_chat)
    await message.answer("Этот чат успешно добавлен в список чатов для заявок")
    update_chats_id()


async def send_message_to_all_users(message: types.Message):
    print(message)
    message_to_all = message.text.replace("/send_to_all", "")
    userdata = UserData()
    all_id = [i[0] for i in userdata.get_all_id()]
    for i in all_id:
        try:
            await bot.send_message(i, message_to_all)
        except ChatNotFound:
            print("chat_not found")


async def check_user_in_db(message: types.Message):
    print(message)
    request = message.text.replace("/get_info ", "")
    userdata = UserData()
    info = userdata.get_info_about_user(request)
    nickname = ""
    for i in info[1]:
        if i in ["*","_", "$", "!", ".", ","]:
            i = "\\"+i
            nickname += i
        else:
            nickname += i
    print(nickname)
    answer = f"id пользователя\: {info[0]}\n Ник пользователя в телеграмме: {nickname}\n Номер телефона пользователя: {info[2]}\n Имя и фамилия пользователя: {info[3]}\n Статус бана пользователя: {str(info[4])}"
    await message.answer(answer, parse_mode=None)


async def ban_unban_users(message: types.Message):
    mess = message.text.split()
    print(mess)
    if "/ban" in mess:
        userdata = UserData()
        userdata.edit_position(mess[-1], "userban", "TRUE")
        await message.answer(f"Пользователь c id {mess[-1]} забанен")
    if "/unban" in mess:
        userdata = UserData()
        userdata.edit_position(mess[-1], "userban", "FALSE")
        await message.answer(f"Пользователь c id {mess[-1]} разбанен")


def register_admin_handlers(dp:  Dispatcher):
    update_chats_id()
    dp.register_message_handler(start_admin_group, user_id=ADMINS_ID, commands=["activate_admin_group"])
    dp.register_message_handler(start_offer_group, user_id=ADMINS_ID, commands=["activate_offer_group"])
    dp.register_message_handler(start_report_group, user_id=ADMINS_ID, commands=["activate_report_group"])
    dp.register_message_handler(send_message_to_all_users, chat_id=loaded_id[0], commands=["send_to_all"])
    dp.register_message_handler(check_user_in_db, chat_id=loaded_id[0], commands=["get_info"])
    dp.register_message_handler(ban_unban_users, chat_id=loaded_id[0], commands=["ban"])
    dp.register_message_handler(ban_unban_users, chat_id=loaded_id[0], commands=["unban"])
