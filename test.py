from googletrans import Translator, constants
from gtts import gTTS
import os
translator = Translator()


def play_text(text, language) -> None:
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("say.mp3")
    os.system("start say.mp3")


def translate(text, finish_lang) -> str:
    translation = translator.translate(text, dest=finish_lang)
    return translation.text


if __name__ == '__main__':
    while True:
        text = input("Enter text to translate: ")
        finish_lang = input("Enter the language to translate to (en for English): ")
        play_text(translate(text=text, finish_lang=finish_lang), finish_lang)