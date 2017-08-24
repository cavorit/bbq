# https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/
import gettext
import locale

print( locale.getlocale() )



# Set up message catalog access
trans = gettext.translation('helloHallo', localedir = 'locale', 

trans.install()
_ = trans.ugettext

print(_('Hello World!'))








        


