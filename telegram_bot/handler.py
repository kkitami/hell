from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from sendToChatter import send_to_chatter

class Message(StatesGroup):
    get = State()

router=Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет!  Я бот, который будет уведомлять о назначении исполнителя на лид Odoo и ")

@router.callback_query(F.data == 'send_message')
async def handle_send_message(callback_query: CallbackQuery, state: FSMContext):
    message = callback_query.message
    lead_id = message.text.split('\n')[0][3:]
    await message.answer('Введите ваше сообщение:')
    # запись lead_id из сообщения в память state
    await state.update_data(lead_id=lead_id)
    await state.set_state(Message.get)
    await callback_query.answer()

@router.message()
async def handle_message(message: Message, state: FSMContext):

    user_message = message.text
    data = await state.get_data()
    lead_id = data['lead_id']
    try:
         await send_to_chatter(lead_id, user_message)
         await message.answer('Ваше сообщение успешно отправлено в chatter!')
    except Exception as e:
        print(e)


