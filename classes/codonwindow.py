import os
import re
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.factory import Factory
from functions.util import amino_dict, acronyms, mass_dict

nucleotides = ['A', 'C', 'T', 'G']
combination = []
for j in nucleotides:
    for k in nucleotides:
        for l in nucleotides:
            nucleotide = l + k + j
            combination.append(nucleotide)
            nucleotide = ""

class Codon(Screen):
    '''
        This class supports loading files as sequence of nucleotides.

        Contains five button:
            load - assigned to load method
            back - assigned to the dissmiss_popup method
            switch_one - change aminoacid notation
                         by default "on" - three character notation
                                    "off" - one character notation
            calculate mass - assigned to calculate_mass method
            calculate isovalue - assigned to calculate_isoValue method

        Contains two object that store text variables:
            codon_input - store the sequence of codons
            sequence - store the sequence of aminoacids
    '''
    codon_input = StringProperty(defaultvalue='')
    sequence = StringProperty(defaultvalue='')
    switch_one = ObjectProperty(None)

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
        self._popup = Popup(title="Load file", content=content, size_hint=(1, 1))
        self._popup.open()

    def load(self, path, filename):
        '''
            This function load sequence from file, deleting non-coding fragment
            from sequence e.g. white signs, numbers, non-coding character.
        '''
        #{3,10} means 3 to 10 repetition from 'A','C','T','G' character set
        #allows to ommited expression like: 'C:/' or 'GCsequence'
        pattern = '[ACTG]{3,10}'
        # self.sequence = ""
        # result = ""
        self.codon_input = ""
        with open(os.path.join(path, filename[0])) as stream:
            full_text = stream.read()
            for word in full_text.split():
                if re.match(pattern, word):
                    # result += word
                    self.codon_input += word
            #instead of using result direct self.codon assigned
            # print("uwagaa jestem w load a result wynosi: {}".format(result))
            print("uwagaa jestem w load a result wynosi: {}".format(self.codon_input))
            # self.codon_input = result

            if self.switch_one.active:
                self.amino_creator_1()
            else:
                self.amino_creator_3()
            self.dismiss_popup()

    def amino_creator_1(self):
        '''
            This function assigns the text from file (one character aminoacid
            notation) to ObjectProperty variable.
            This text will be displayed in the text window in Welcome class.
        '''
        codon = ""
        for char in range(len(self.codon_input)):
            codon += self.codon_input[char]
            if len(codon) == 3:
                for amino, nucleo in amino_dict(os.path.join(os.getcwd(),
                                                "docs/base.def")).items():
                    for three in nucleo:
                        if three == codon:
                            self.sequence += acronyms(os.path.join(
                                          os.getcwd(), "docs/three.def"))[amino]
                            # print("jestem w amino_1 i ")
                codon = ""
        print("jestem w amino_1 i self.sequence wynosi: {}".format(self.sequence))

    def amino_creator_3(self):
        '''
            This function assigns the text from file (three character aminoacid
            notation) to ObjectProperty variable.
            This text will be displayed in the text window in Welcome class.
        '''
        codon = ""
        for char in range(len(self.codon_input)):
            codon += self.codon_input[char]
            if len(codon) == 3:
                for amino, nucleo in amino_dict(os.path.join(os.getcwd(),
                                                "docs/base.def")).items():
                    for three in nucleo:
                        if three == codon:
                            self.sequence += amino
                codon = ""

    def switch(self, instance, value):
        '''
            This function change the value (True/False) if you press
            "on/off" button.
        '''
        self.sequence = ""
        if self.codon_input != "":
            if value:
                self.amino_creator_1()
            else:
                self.amino_creator_3()
        else:
            self.show_load()

    def calcMass_1(self):
        '''
            This function calculate mass from sequence in one character
            aminoacid notation.
        '''
        result = 0
        for char in self.sequence:
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

    def calcMass_3(self):
        '''
            This function calculate mass from sequence in three character
            aminoacid notation.
        '''
        result = 0
        codon = ""
        for letter in range(len(self.sequence)):
            codon += self.sequence[letter]
            if letter % 3 == 2:
                for three, mass in mass_dict(os.path.join(os.getcwd(),
                                             "docs/baseMass.def")).items():
                    if three == codon:
                        result += mass
                codon = ""
        return round(result, 2)

    def calculate_mass(self):
        '''
            This function trigger Mass Dialog window.
        '''
        if self.codon_input != "":
            if self.switch_one.active:
                result = str(self.calcMass_1())
            else:
                result = str(self.calcMass_3())
            content = Factory.MassDialog(cancel=self.dismiss_popup, m=result)
            self._popup = Popup(title="Mass information", content=content,
                                size_hint=(1, 1))
            self._popup.open()
        else:
            self.show_load()

    def calcIso_1(self):
        '''
            This function calcuate IsoValue from one character aminoacid
            sequence notation.
        '''
        AspNumber, GluNumber, CysNumber, TyrNumber, HisNumber, LysNumber, ArgNumber \
               = 0, 0, 0, 0, 0, 0, 0
        QN1, QN2, QN3, QN4, QN5, QP1, QP2, QP3, QP4, NQ \
               = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        for amino in self.sequence:

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

        pH = 6.5         #starting point pI = 6.5 - theoretically it should be 7, but
                         #average protein pI is 6.5 so we increase the probability
        pHprev = 0.0     #of finding the solution
        pHnext = 14.0    #0-14 is possible pH range
        X = 0.0
        E = 0.01         #epsilon means precision [pI = pH +- E]
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

    def calcIso_3(self):
        '''
            This function calcuate IsoValue from three character aminoacid
            sequence notation.
        '''
        AspNumber, GluNumber, CysNumber, TyrNumber, HisNumber, LysNumber, ArgNumber \
               = 0, 0, 0, 0, 0, 0, 0
        QN1, QN2, QN3, QN4, QN5, QP1, QP2, QP3, QP4, NQ \
               = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        codon = ""
        for amino in range(len(self.sequence)):
            codon += self.sequence[amino]
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

    def calculate_isoValue(self):
        '''
            This function trigger IsoValue Dialog window.
        '''
        if self.codon_input != "":
            result = "Isoelectric Point (pH) is: "
            if self.switch_one.active:
                result += self.calcIso_1()
            else:
                result += self.calcIso_3()
            content = Factory.IsoValueDialog(cancel=self.dismiss_popup, iso_val=result)
            self._popup = Popup(title="IsoValue information", content=content,
                                size_hint=(0.9, 0.9))
            self._popup.open()
        else:
            self.show_load()
