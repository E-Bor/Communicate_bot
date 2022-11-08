from config.config import bad_name_in_reg


async def check_name_right(message):
    names = message.text.split()
    if len(names) == 2 and names[0].istitle() and names[1].istitle() and len(names[0]) > 1 and len(names[1]) > 1:
        return message.text
    else:
        await message.answer(bad_name_in_reg)

