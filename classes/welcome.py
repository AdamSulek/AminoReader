from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class Welcome(Screen):
    '''
        This class represents the display place of the loaded sequences.

        This class contains two different possibilities of displaying:

            from_codon - contains 2 rows for displayed sequence
                         one row for nucleotide and
                         one row for aminoacid notation

            from_amino - contains 1 rows for displayed sequence
    '''
    from_codon = ObjectProperty(None)
    from_amino = ObjectProperty(None)
