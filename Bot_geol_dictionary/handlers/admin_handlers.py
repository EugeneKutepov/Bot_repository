from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from db.db_service import file_ups

router: Router = Router()

@router.message(Command(commands=['getdb']))
async def process_help_command(message: Message):
    await message.answer_document(file_ups())