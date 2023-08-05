import uuid
import os
from telebot.types import Message
from telebot import TeleBot
import speech_recognition as sr


class VoiceConvert:
    """
    Преобразование голосового сообщения в текст.
    Работает с библиотекой telebot.
    """
    def __init__(self, bot: TeleBot, language: str = "ru-RU") -> None:
        self.language = language
        self.bot = bot

    def save_voice(
        self,
        filename_voice: str,
        message: Message
    ) -> None:
        """
        Сохранение полученного голосового сообщения.
        """
        file_info = self.bot.get_file(message.voice.file_id)
        downloaded_file = self.bot.download_file(file_info.file_path)
        with open(filename_voice, 'wb') as new_file:
            new_file.write(downloaded_file)

    @staticmethod
    def voice_convert_ogg2wav(
        filename_voice: str,
        filename_converted: str
    ) -> None:
        """
        Подготовка файла с голосовым сообщением к конвертации.
        *.ogg -> *.wav
        """
        os.system("ffmpeg -i " + filename_voice + "  " + filename_converted)

    @staticmethod
    def clear(
        filename_voice: str,
        filename_converted: str
    ) -> None:
        """
        Удаление временных голосовых файлов.
        """
        os.remove(filename_voice)
        os.remove(filename_converted)

    def audio_to_text(self, message: Message) -> str:
        """
        Преобразование голосовго сообщения в текст.
        """
        r = sr.Recognizer()

        filename = str(uuid.uuid4())
        filename_voice = f"./voice/{filename}.ogg"
        filename_converted = f"./ready/{filename}.wav"

        self.save_voice(filename_voice, message)
        self.voice_convert_ogg2wav(filename_voice, filename_converted)

        with sr.AudioFile(filename_converted) as source:
            audio = r.record(source)
            r.adjust_for_ambient_noise(source)

        self.clear(filename_voice, filename_converted)
        return r.recognize_google(audio, language=self.language)
