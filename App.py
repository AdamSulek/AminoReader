from kivy.app import App
from kivy.lang import Builder

from classes.aminowindow import Amino_one, Amino_three
from classes.codonwindow import Codon
from classes.isowindow import IsoValueDialog
from classes.masswindow import MassDialog
from classes.loadwindow import LoadDialog
from classes.welcome import Welcome
from classes.windowmenager import WindowManager

file = Builder.load_file("gui/aminoreader.kv")

sm = WindowManager()
screens = [Welcome(name = "main"), Codon(name = "codon"),
           Amino_one(name = "amino_one"), Amino_three(name = "amino_three")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class AminoreaderApp(App):
    title = "Amino Reader AS"
    def build(self):
        return sm

if __name__ == '__main__':
    AminoreaderApp().run()
