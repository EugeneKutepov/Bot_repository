from aiogram import Bot, Dispatcher
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Text
from aiogram.exceptions import TelegramBadRequest

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# BOT_TOKEN = 'BOT TOKEN HERE'


BOT_TOKEN: str = '6054779759:AAE8JqMOb0O6BHmngBGjOyjXZoiKPAFVUNQ'

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()


LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAICuGQM60xVP0YI233-o-IidzYHY7zNAAKSyTEbkFJpSLbelRrE-7iyAQADAgADcwADLwQ',
    'photo_id2': 'AgACAgIAAxkBAAICumQM69Jy7Cb76_wdgraHjZciPsrbAAKUyTEbkFJpSCGgPQobSCiEAQADAgADcwADLwQ',
    'voice_id1': 'AwACAgIAAxkBAAICwmQM7gqyuYQoxvDsTxd0pnJO4brPAALDKwACkFJpSD3oy2zaZR9CLwQ',
    'voice_id2': 'AwACAgIAAxkBAAICxmQM7i4Tbi_1SZ7CJCiSD_8SGEebAALFKwACkFJpSC5-jy3sE-6ALwQ',
    # 'audio_id1': 'CQACAgIAAxkBAAIVRWPKsPl83xynqlF9YvF5MRyF9GxeAAL1JAACkhBZSmyFCDY61yX8LQQ',
    # 'audio_id2': 'CQACAgIAAxkBAAIVR2PKsXppkdhAnOlqwpOHDJivtfvJAAL4JAACkhBZSoMVyPSB59h5LQQ',
    'document_id1': 'BQACAgIAAxkBAAICvGQM7GpxiMzsWpdQrG6psvlBnuUFAAK9KwACkFJpSJ4WfQeFvHLHLwQ',
    'document_id2': 'BQACAgIAAxkBAAICvmQM7L8fyVGDZw4lBCDXcMGoMb9lAAK-KwACkFJpSD3CieGCweDSLwQ',
    'video_id1': 'BAACAgIAAxkBAAICwGQM7ZNq0IWbBRyYHqMlHiLM9GG5AALBKwACkFJpSBTzFPBHLPGzLwQ',
    'video_id2': 'BAACAgIAAxkBAAICxGQM7g2u8cPMGraA_6_N1vlY8I73AALEKwACkFJpSDdXFJv8vahvLwQ',
    }


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'videoС')
    await message.answer_document(
                        document=LEXICON['video_id1'],
                        caption='Это видео 1',
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(Text(text=['text',
                              'audio',
                              'video',
                              'document',
                              'photo',
                              'voice']))
async def process_button_press(callback: CallbackQuery):
    markup = get_markup(2, 'video')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaDocument(
                media=LEXICON['video_id2'],
                caption='Это video 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaDocument(
                media=LEXICON['video_id1'],
                caption='Это video 1'),
            reply_markup=markup)


# Этот хэндлер будет срабатывать на все остальные сообщения
@dp.message()
async def send_echo(message: Message):
    print(message)
    await message.answer(
            text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)