# https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/
import gettext
import locale

print( locale.getlocale() )



# Set up message catalog access
trans = gettext.translation(domain='messages', localedir = 'locale', languages =['de'])  
# domain = prefix der .mo Datei
# localedir = Unterverzeichnis 'locale' des Projektverzeichnis
# languages = Sprache bzw. Unterverzeichnis von 'locale', das die
# Namenskonventionen bedienen sollte.

trans.install() # mit dieserm Befehl erklärt gettext Python, was die Funktion _() bedeutet


print(_('Hello World!'))








        


