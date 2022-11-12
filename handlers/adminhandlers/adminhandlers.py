from aiogram import Bot, types, Dispatcher
from create import dp, bot
from config.config import ADMINS_ID, PATH

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


def register_admin_handlers(dp:  Dispatcher):
    dp.register_message_handler(start_admin_group, user_id=ADMINS_ID, commands=["start_admin_group"])
    dp.register_message_handler(start_offer_group, user_id=ADMINS_ID, commands=["start_offer_group"])
    dp.register_message_handler(start_report_group, user_id=ADMINS_ID, commands=["start_report_group"])
