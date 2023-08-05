class MessagesProcessor:
    """
    Класс для обработки голосовых и текстовых сообщений.
    """
    def __init__(self) -> None:
        """
        Инициализация статусов, для ответа
        """
        self.UNKNOWN = -1
        self.HELLO_ANDREY = 1
        self.MY_HOBBIES = 2
        self.PHOTO_NEW = 3
        self.PHOTO_LAST = 4
        self.MY_VOICES = 5
        self.HELP = 6

    def get_answer_сode(
        self,
        text_message: str,
        is_voice: bool = False
    ) -> int:
        """
        Функция возвращает статус для ответа боту.
        text_message - текстовый запрос боту
        is_voice - содержит информация откуда получен запрос
        """
        if is_voice:
            return self.get_answer_code_voice(text_message)
        return self.get_answer_code_text(text_message)

    def get_answer_code_voice(self, text_message) -> int:
        """
        Обработка запросов голосовых сообщений.
        """
        if 'Андрей' in text_message:
            if 'привет' in text_message:
                return self.HELLO_ANDREY
            elif 'расскажи о своих увлечениях' in text_message.lower():
                return self.MY_HOBBIES
            elif 'пришли свое последнее фото' in text_message.lower():
                return self.PHOTO_NEW
            elif 'пришли свое старое фото' in text_message.lower():
                return self.PHOTO_LAST
            elif 'пришли свои голосовые сообщения' in text_message.lower():
                return self.MY_VOICES
            elif 'что умеет твой бот' in text_message.lower():
                return self.HELP
        return -1

    def get_answer_code_text(self, text_message) -> int:
        """
        Обработка запросов текстовых сообщений.
        """
        if text_message == '👋 Привет, Андрей!':
            return self.HELLO_ANDREY
        elif (
            text_message == '🤖 Мои увлечения 🤖' 
            or text_message == 'Андрей, расскажи о своих увлечениях'
        ):
            return self.MY_HOBBIES
        elif (
            text_message == '🤩 Фото сейчас 🤩'
            or text_message == 'Андрей, пришли свое последнее фото'
        ):
            return self.PHOTO_NEW
        elif (
            text_message == '💩 Фото молодого 💩'
            or text_message == 'Андрей, пришли свое старое фото'
        ):
            return self.PHOTO_LAST
        elif (
            text_message == '🎤 Мои голосовые сообщения 🎤'
            or text_message == 'Андрей, пришли свои голосовые сообщения'
        ):
            return self.MY_VOICES
        elif (
            text_message == '❓ Справка ❓'
            or text_message == 'Андрей, что умеет твой бот'
        ):
            return self.HELP
        return -1
