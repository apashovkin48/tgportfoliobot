from dotenv import load_dotenv
from telebot import TeleBot, types
import os
from tg_voice_convert import VoiceConvert
from messages_processor import MessagesProcessor


load_dotenv()

bot = TeleBot(os.getenv('TGBOT_TOKEN'))
voice_convert = VoiceConvert(bot)
messages_processor = MessagesProcessor()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_hello = types.KeyboardButton('👋 Привет, Андрей!')
    markup.add(btn_hello)
    bot.send_message(
        message.from_user.id,
        '👋 Привет! Меня зовут Андрей и это мой Бот портфолио!\n'
        'Чтобы со мной лучше познакомиться ты можешь воспользоваться '
        'интерфейсной панелью или задать мне вопросы лично, '
        'отправив голосовое сообщение. \n'
        'Если нужна информация о работе бота воспользуйся справкой или '
        'документацией на [GitHub](https://github.com/apashovkin48/tgportfoliobot).',
        reply_markup=markup,
        parse_mode='Markdown'
    )


@bot.message_handler(content_types=['text', 'voice'])
def message_processing(message):
    is_voice = True if message.content_type == 'voice' else False
    text = ''
    if not is_voice:
        text = message.text
    else:
        text = voice_convert.audio_to_text(message)

    res = messages_processor.get_answer_сode(text, is_voice)

    if res == messages_processor.HELLO_ANDREY:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_hobbie = types.KeyboardButton('🤖 Мои увлечения 🤖')
        btn_photo_now = types.KeyboardButton('🤩 Фото сейчас 🤩')
        btn_photo_young = types.KeyboardButton('💩 Фото молодого 💩')
        btn_voices = types.KeyboardButton('🎤 Мои голосовые сообщения 🎤')
        btn_help = types.KeyboardButton('❓ Справка ❓')

        markup.add(
            btn_hobbie,
            btn_photo_now,
            btn_photo_young,
            btn_voices,
            btn_help
        )
        bot.send_message(
            message.from_user.id,
            'Хочешь узнать обо мне?\n'
            'Нажми, напиши или отправь голосовое сообщение боту 🔥.',
            reply_markup=markup
        )

    elif res == messages_processor.MY_HOBBIES:
        bot.send_message(
            message.from_user.id,
            'Мои увлечения:\n'
            '1️⃣ Занимаюсь спортом. Посещаю тренажерный зал и '
            'сбрасываю лишний вес. За последнее время сбросил более 20кг, '
            'но поставленная цель еще впереди.\n'
            '2️⃣ Робототехника. Работаю в компании, которая занимается '
            'автоматизацией производственных процессов с использованием '
            'роботов манипуляторов. \n'
            '3️⃣ Последнее время полюбил прокачиваться в решении алгоритмов '
            'яндекc.контест и leetcode. Приятно ощущать, что с каждым разом '
            'задачки становятся для тебя все легче и легче.\n',
            parse_mode='Markdown'
        )

    elif res == messages_processor.PHOTO_NEW:
        bot.send_message(
            message.from_user.id,
            'Андрюша, 25 годиков 🔥🔥🔥',
            parse_mode='Markdown'
        )
        bot.send_photo(
            message.from_user.id,
            open('./media/photo_now.jpeg', 'rb')
        )

    elif res == messages_processor.PHOTO_LAST:
        bot.send_message(
            message.from_user.id,
            'Андрюша, 18 лет 💩💩💩',
            parse_mode='Markdown'
        )
        bot.send_photo(
            message.from_user.id,
            open('./media/photo_last.jpeg', 'rb')
        )

    elif res == messages_processor.MY_VOICES:
        bot.send_message(
            message.from_user.id,
            'Прослушав данное сообщение ваша бабушка напишет свой GPT 🧠',
            parse_mode='Markdown'
        )
        bot.send_audio(message.chat.id, open('./media/GPT.ogg', 'rb'))
        bot.send_message(
            message.from_user.id,
            'Если не знаешь разницы между SQL и NoSQL '
            'то это специально для тебя 🧨',
            parse_mode='Markdown'
        )
        bot.send_audio(message.chat.id, open('./media/SQL.ogg', 'rb'))
        bot.send_message(
            message.from_user.id,
            'Моя первая и единственная любовь ❤️❤️❤️',
            parse_mode='Markdown'
        )
        bot.send_audio(message.chat.id, open('./media/LOVE.ogg', 'rb'))

    elif res == messages_processor.HELP:
        bot.send_message(
            message.from_user.id,
            'Голосовые и текстовые команды:\n'
            '1️⃣ Андрей, расскажи о своих увлечениях\n'
            '2️⃣ Андрей, пришли свое последнее фото\n'
            '3️⃣ Андрей, пришли свое старое фото\n'
            '4️⃣ Андрей, пришли свои голосовые сообщения\n'
            '5️⃣ Андрей, что умеет твой бот\n',
            parse_mode='Markdown'
        )

    elif res == messages_processor.UNKNOWN:
        bot.send_message(
            message.from_user.id,
            'Я еще не умею отвечать на такие вопросы, '
            'но когда-нибудь научусь!',
            parse_mode='Markdown'
        )


bot.infinity_polling()
