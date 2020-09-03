import os
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.factory import Factory
from functions.util import acronyms, mass_dict

class Amino_one(Screen):
    '''
        This class supports loading files of one character aminoacids notation.

        Contains four button:
            load - assigned to load method
            back - assigned to the dissmiss_popup method
            calculate mass - assigned to calculate_mass method
            calculate isovalue - assigned to calculate_isoValue method

        Contains one object that store text variables:
            sequence
    '''
    sequence = ObjectProperty(None)

    def dismiss_popup(self):
        '''
            This function dissmiss Popup window.
        '''
        self._popup.dismiss()

    def show_load(self):
        '''
            This function trigger Load Dialog window.
        '''
        content = Factory.LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(1, 1))
        self._popup.open()

    def load(self, path, filename):
        '''
            This function load sequence from file.
        '''
        with open(os.path.join(path, filename[0])) as stream:
            self.sequence.text = stream.read()
            self.dismiss_popup()

    def calcMass(self):
        '''
            This function calculate mass from one character aminoacid sequence
            notation.
        '''
        result = 0
        for char in self.sequence.text:
            for amino, letter in acronyms(os.path.join(os.getcwd(),
                                          "docs/three.def")).items():
                for sign in letter:
                    if sign == char:
                        codon = amino
                        for three, mass in mass_dict(os.path.join(os.getcwd(),
                                                "docs/baseMass.def")).items():
                            if three == codon:
                                result += mass
        return round(result, 2)

    def calculate_mass(self):
        '''
            This function trigger Mass Dialog window.
        '''
        if self.sequence.text != "":
            result = str(self.calcMass())
            content = Factory.MassDialog(cancel=self.dismiss_popup, m=result)
            self._popup = Popup(title="Mass information", content=content,
                                                          size_hint=(1, 1))
            self._popup.open()
        else:
            self.show_load()

    def calcIso(self):
        '''
            This function calculate Isovalue Point (one character notation).
        '''
        AspNumber, GluNumber, CysNumber, TyrNumber, HisNumber, LysNumber, ArgNumber \
               = 0, 0, 0, 0, 0, 0, 0
        QN1, QN2, QN3, QN4, QN5, QP1, QP2, QP3, QP4, NQ \
               = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        for amino in self.sequence.text:

            if amino == 'D':
                AspNumber += 1
            if amino == 'E':
                GluNumber += 1
            if amino == 'C':
                CysNumber += 1
            if amino == 'Y':
                TyrNumber += 1
            if amino == 'H':
                HisNumber += 1
            if amino == 'K':
                LysNumber += 1
            if amino == 'R':
                ArgNumber += 1

        pH = 6.5       #starting point pI = 6.5 - theoretically it should be 7, but
                       #average protein pI is 6.5 so we increase the probability
        pHprev = 0.0   #of finding the solution
        pHnext = 14.0  #0-14 is possible pH range
        X = 0.0
        E = 0.01       #epsilon means precision [pI = pH +- E]
        temp = 0.0
        iso = 0
        numberIter = 0

        while not iso:
           QN1 = -1 / (1 + pow(10, (3.65-pH)))
           QN2 = -AspNumber / (1 + pow(10, (3.9 - pH)))
           QN3 = -GluNumber / (1 + pow(10, (4.07 -  pH)))
           QN4 = -CysNumber / (1 + pow(10, (8.18 - pH)))
           QN5 = -TyrNumber / (1 + pow(10, (10.46 - pH)))
           QP1 = HisNumber / (1 + pow(10, (pH - 6.04)))
           QP2 = 1 / (1 + pow(10, (pH - 8.2)))
           QP3 = LysNumber / (1 + pow(10, (pH - 10.54)))
           QP4 = ArgNumber / (1 + pow(10, (pH - 12.48)))

           NQ = QN1 + QN2 + QN3 + QN4 + QN5 + QP1 + QP2 + QP3 + QP4
           if NQ < 0:
               temp = pH
               pH = pH - ((pH-pHprev)/2)
               pHnext = temp
           else:
               temp = pH
               pH = pH + ((pHnext-pH)/2)
               pHprev = temp
           if (pH - pHprev) < E and (pHnext - pH) < E:
               iso = 1

           numberIter += 1

        return str(round(pH, 2))

    def calculate_isoValue(self):
        '''
            This function trigger IsoValue Dialog window.
        '''
        if self.sequence.text != "":
            result = "Isoelectric Point (pH) is: "
            result += self.calcIso()
            content = Factory.IsoValueDialog(cancel=self.dismiss_popup, iso_val=result)
            self._popup = Popup(title="IsoValue information", content=content,
                                                              size_hint=(1, 1))
            self._popup.open()
        else:
            self.show_load()

class Amino_three(Amino_one):
    '''
        This class supports loading files of one character aminoacids notation.
        This class inherits from Amino_one class.

        The only different is in class method: calcIso and calcMass.
        Overloaded method use different iteration through aminoacids sequence.
    '''
    sequence = ObjectProperty(None)

    def calcIso(self):
        '''
            This function calculate Isovalue Point (three character notation).
        '''
        AspNumber, GluNumber, CysNumber, TyrNumber, HisNumber, LysNumber, ArgNumber \
               = 0, 0, 0, 0, 0, 0, 0
        QN1, QN2, QN3, QN4, QN5, QP1, QP2, QP3, QP4, NQ \
               = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        codon = ""
        for amino in range(len(self.sequence.text)):
            codon += self.sequence.text[amino]
            if len(codon) == 3:
                if codon == "Asp":
                    AspNumber += 1
                if codon == "Glu":
                    GluNumber += 1
                if codon == "Cys":
                    CysNumber += 1
                if codon == "Tyr":
                    TyrNumber += 1
                if codon == "His":
                    HisNumber += 1
                if codon == "Lys":
                    LysNumber += 1
                if codon == "Arg":
                    ArgNumber += 1

                codon = ""

        pH = 6.5        #starting point pI = 6.5 - theoretically it should be 7, but
                        #average protein pI is 6.5 so we increase the probability
        pHprev = 0.0    #of finding the solution
        pHnext = 14.0   #0-14 is possible pH range
        X = 0.0
        E = 0.01        #epsilon means precision [pI = pH +- E]
        temp = 0.0
        iso = 0
        numberIter = 0

        while not iso:
           QN1 = -1 / (1 + pow(10, (3.65-pH)))
           QN2 = -AspNumber / (1 + pow(10, (3.9 - pH)))
           QN3 = -GluNumber / (1 + pow(10, (4.07 -  pH)))
           QN4 = -CysNumber / (1 + pow(10, (8.18 - pH)))
           QN5 = -TyrNumber / (1 + pow(10, (10.46 - pH)))
           QP1 = HisNumber / (1 + pow(10, (pH - 6.04)))
           QP2 = 1 / (1 + pow(10, (pH - 8.2)))
           QP3 = LysNumber / (1 + pow(10, (pH - 10.54)))
           QP4 = ArgNumber / (1 + pow(10, (pH - 12.48)))

           NQ = QN1 + QN2 + QN3 + QN4 + QN5 + QP1 + QP2 + QP3 + QP4
           if NQ < 0:
               temp = pH
               pH = pH - ((pH-pHprev)/2)
               pHnext = temp
           else:
               temp = pH
               pH = pH + ((pHnext-pH)/2)
               pHprev = temp
           if (pH - pHprev) < E and (pHnext - pH) < E:
               iso = 1

           numberIter += 1

        return str(round(pH, 2))

    def calcMass(self):
        '''
            This function calculate mass from three character aminoacids
            sequence notation.
        '''
        result = 0
        codon = ""
        for char in range(len(self.sequence.text)):
            codon += self.sequence.text[char]
            if char % 3 == 2:
                for three, mass in mass_dict(os.path.join(os.getcwd(),
                                            "docs/baseMass.def")).items():
                    if three == codon:
                        result += mass
                codon = ""
        return round(result, 2)
