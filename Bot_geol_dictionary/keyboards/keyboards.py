from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from lexicon.lexicon import LEXICON_RU

def create_kb_answer(list_terms:dict):
    terms, kbs = [], []
    i = 0
    for key in list_terms.keys():
        if i <=50:
            button = InlineKeyboardButton(
                text=key, callback_data=list_terms[key])
            terms.append([button])
            i+=1
        else:
            button = InlineKeyboardButton(
                text=key, callback_data=list_terms[key])
            terms.append([button])
            kb = InlineKeyboardMarkup(inline_keyboard=terms)
            kbs.append(kb)
            terms, i = [], 0
    if len(terms) !=0:
        kb = InlineKeyboardMarkup(inline_keyboard=terms)
        kbs.append(kb)
    print(len(terms))
    return kbs
