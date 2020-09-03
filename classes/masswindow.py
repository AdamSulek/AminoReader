from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from functions.util import str_checker

class MassDialog(FloatLayout):
    '''
        This Screen is using to showing the mass
        and to calculate molar mass.
    '''
    cancel = ObjectProperty(None)
    mass = ObjectProperty(None)
    set_mass = ObjectProperty(None)
    set_volume = ObjectProperty(None)
    concentration = ObjectProperty(None)
    submit = ObjectProperty(None)

    def __init__(self, m, **kwargs):
        super(Factory.MassDialog, self).__init__(**kwargs)
        self.mass.text = m

    def submit(self):

        if self.set_mass.text == "" and self.set_volume.text == "":
            self.concentration.text = "first enter any value"
        else:
            if str_checker(self.set_mass.text) and str_checker(self.set_volume.text):
                mm = float(self.set_mass.text)
                vol = float(self.set_volume.text)
                molar_mass = float(self.mass.text)
                mol = mm / molar_mass
                word = str(round((mol / vol), 2))
                word += " mol/L"
                self.concentration.text = word
            else:
                self.concentration.text = "enter properly volume and mass"
