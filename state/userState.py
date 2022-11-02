from aiogram.dispatcher.filters.state import State, StatesGroup

async def update_state(state, name_of_state, update):
    update_fsm = await state.get_data()
    a = update_fsm[name_of_state].copy()
    if update == "🔙Назад":
        return a
    a.append(update)
    await state.update_data(current_state=a)
    updated_fsm = await state.get_data()
    return updated_fsm[name_of_state]



class UserState(StatesGroup):
    """state for change user category"""
    current_state = State()

