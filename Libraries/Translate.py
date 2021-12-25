import os
import googletrans
from gtts import gTTS
from googletrans import Translator
import playsound
import textract
translator = Translator()
lang_dict = {v: k for k, v in googletrans.LANGUAGES.items()}
