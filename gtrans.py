from googletrans import Translator
translator = Translator()


test = translator.translate('Hola, cómo estás', src='es', dest='en')
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

print(test.text)
