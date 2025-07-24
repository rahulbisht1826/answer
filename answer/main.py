import wikipedia
lcode = input("enter language you want to use for search:")
if lcode == "english":
    wikipedia.set_lang("en")
elif lcode == "hindi":
    wikipedia.set_lang("hi")
elif lcode == "french":
    wikipedia.set_lang("fr")
elif lcode == "german":
    wikipedia.set_lang("de")
elif lcode == "kannada":
    wikipedia.set_lang("kn")
elif lcode == "tamil":
    wikipedia.set_lang("ta")
elif lcode == "telugu":
    wikipedia.set_lang("te")
elif lcode == "malayalam":
    wikipedia.set_lang("ml")
elif lcode == "bengali":
    wikipedia.set_lang("bn")
elif lcode == "marathi":
    wikipedia.set_lang("mr")
elif lcode == "urdu":
    wikipedia.set_lang("ur")
elif lcode == "gujarati":
    wikipedia.set_lang("gu")
elif lcode == "punjabi":
    wikipedia.set_lang("pa")
elif lcode == "assamese":
    wikipedia.set_lang("as")
elif lcode == "nepali":
    wikipedia.set_lang("ne")
elif lcode == "sinhala":
    wikipedia.set_lang("si")
elif lcode == "oriya":
    wikipedia.set_lang("or")
elif lcode == "konkani":
    wikipedia.set_lang("kok")
elif lcode == "sanskrit":
    wikipedia.set_lang("sa")
elif lcode == "filipino":
    wikipedia.set_lang("tl")
elif lcode == "spanish":
    wikipedia.set_lang("es")
elif lcode == "italian":
    wikipedia.set_lang("it")
elif lcode == "russian":
    wikipedia.set_lang("ru")
elif lcode == "chinese":
    wikipedia.set_lang("zh")
elif lcode == "japanese":
    wikipedia.set_lang("ja")
elif lcode == "korean":
    wikipedia.set_lang("ko")
elif lcode == "portuguese":
    wikipedia.set_lang("pt")
elif lcode == "arabic":
    wikipedia.set_lang("ar")
elif lcode == "turkish":
    wikipedia.set_lang("tr")
elif lcode == "dutch":
    wikipedia.set_lang("nl")
elif lcode == "swedish":
    wikipedia.set_lang("sv")
elif lcode == "polish":
    wikipedia.set_lang("pl")
elif lcode == "danish":
    wikipedia.set_lang("da")
elif lcode == "finnish":
    wikipedia.set_lang("fi")
elif lcode == "norwegian":
    wikipedia.set_lang("no")
elif lcode == "greek":
    wikipedia.set_lang("el")
elif lcode == "czech":
    wikipedia.set_lang("cs")
elif lcode == "hungarian":
    wikipedia.set_lang("hu")
elif lcode == "thai":
    wikipedia.set_lang("th")
elif lcode == "vietnamese":
    wikipedia.set_lang("vi")
elif lcode == "indonesian":
    wikipedia.set_lang("id")
elif lcode == "ukrainian":
    wikipedia.set_lang("uk")
elif lcode == "hebrew":
    wikipedia.set_lang("he")
elif lcode == "romanian":
    wikipedia.set_lang("ro")
elif lcode == "bulgarian":
    wikipedia.set_lang("bg")
elif lcode == "croatian":
    wikipedia.set_lang("hr")
elif lcode == "slovak":
    wikipedia.set_lang("sk")
elif lcode == "lithuanian":
    wikipedia.set_lang("lt")
elif lcode == "latvian":
    wikipedia.set_lang("lv")
elif lcode == "estonian":
    wikipedia.set_lang("et")
elif lcode == "slovenian":
    wikipedia.set_lang("sl")
elif lcode == "serbian":
    wikipedia.set_lang("sr")
elif lcode == "malay":
    wikipedia.set_lang("ms")
elif lcode == "swahili":
    wikipedia.set_lang("sw")
elif lcode == "persian":
    wikipedia.set_lang("fa")
else:
    print("Language not supported. Defaulting to English.")
    wikipedia.set_lang("en")

search=input("enter what you want to search:")
print(wikipedia.summary(search))
