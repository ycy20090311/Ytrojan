from os import environ
from thirdhand.Strings import SUPPORTED_LANGUAGES

def getLanguage():
    lang = ""
    try:
        lang = environ['LANG']
    except KeyError:
        print("[WARN] Cannot found $LANG environment variable. Back to English.")
        return "en_US"
    lang_and_encoding = lang.split('.')
    lang = lang_and_encoding[0]
    if lang in SUPPORTED_LANGUAGES:
        return lang
    else:
        print(f"[WARN] Unsupported language {lang}. Back to the default language (English).")
        return "en_US"
