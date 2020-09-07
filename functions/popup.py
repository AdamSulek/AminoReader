from kivy.uix.popup import Popup
from kivy.uix.label import Label

def invalidLoad():
    popup = Popup( title = " something went wrong ",
                   content = Label(text = "         Your sequence is empty \
                                \nmake sure if You load proper file"),
                   size_hint = (None, None), size = (400, 400) )
    popup.open()
