from aiogram.dispatcher.filters.state import State, StatesGroup


async def update_state(state, name_of_state, update):
    update_fsm = await state.get_data()
    a = update_fsm[name_of_state].copy()
    a.append(update)
    await state.update_data(current_state=a)

def check_name_right(name):
    names = name.split()
    if len(names) != 2:
        return


class UserLogingState(StatesGroup):
    """state for user registration"""
    name = State()
    phone = State()

class UserReportState(StatesGroup):
    """state for creating report"""
    address = State()
    photo = State()
    reason = State()

