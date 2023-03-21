LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\nВведи любой геологический термин',
    '/help': 'Это бот для работы с геологическим словарем от <a href="https://vsegei.ru">ВСЕГЕИ</a> издания 2010 года.\n\n '
             'Вы вводите в строке геологический термин, а бот выдаст результат поиска. '
             'В случае слишком большого списка, результаты выводятся порциями по 50 позиций.\n\n'
             'Edited by <a href="https://www.linkedin.com/in/eugene-kutepov-b41318142">Eugene Kutepov</a> in associate with <a href="t.me/geolchat">Геологи</a>',
    'absent': 'Такой термин отсутствует в словаре'}

def show_definition(data):
    return data