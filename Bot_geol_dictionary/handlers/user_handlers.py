from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import create_kb_answer
from lexicon.lexicon import LEXICON_RU, show_definition
from services.services import parse_term, read_direct_link

router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])



@router.message()
async def process_yes_answer(message: Message):
    kbs = create_kb_answer(parse_term(message.text))
    for kb in kbs:
        await message.answer(text="Результаты поиска:", reply_markup=kb)


@router.callback_query()
async def process_buttons_press(callback: CallbackQuery):
    answer = read_direct_link(callback.data)
    #print(callback.value)
    await callback.message.answer(text=answer)