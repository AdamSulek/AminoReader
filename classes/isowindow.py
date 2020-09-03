from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class IsoValueDialog(FloatLayout):
    '''
        This Screen is using to showing the IsoValue point.
    '''
    cancel = ObjectProperty(None)
    iso = ObjectProperty(None)

    def __init__(self, iso_val, **kwargs):
        super(IsoValueDialog, self).__init__(**kwargs)
        self.iso.text = iso_val
