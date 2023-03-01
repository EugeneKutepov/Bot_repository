from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from lexicon.lexicon import LEXICON_RU

def create_kb_answer(list_terms:dict):
    terms = []
    for key in list_terms.keys():
        button = InlineKeyboardButton(
            text=key, callback_data=list_terms[key])
        terms.append([button])
    print(len(terms))
    return InlineKeyboardMarkup(inline_keyboard=terms)
