from config.config import bad_name_in_reg, bad_phone_in_reg


async def check_name_right(message):
    names = message.text.split()
    if len(names) == 2 and names[0].istitle() and names[1].istitle() and len(names[0]) > 1 and len(names[1]) > 1:
        return message.text
    else:
        await message.answer(bad_name_in_reg)

async def check_phone_right(message):
    length = True if len(message.text) == 12 else False
    plus_is_fine = True if message.text[:2] == "+7" else False
    letter_is_fine = True

    for i in message.text:
        if i not in ["0","1","2","3","4","5","6","7","8","9","+"]:
            letter_is_fine = False
    if length and plus_is_fine and letter_is_fine:
        print(length, plus_is_fine, letter_is_fine)
        return message.text
    else:
        print(length, plus_is_fine, letter_is_fine)
        await message.answer(bad_phone_in_reg)
