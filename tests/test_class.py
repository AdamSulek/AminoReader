import unittest
import os
import re
import sys
import unittest.mock as mock
import tempfile
from classes.aminowindow import Amino_one, Amino_three
from classes.codonwindow import Codon
from functions.util import amino_dict

class Amino_oneTest(unittest.TestCase):

    def mock_empty(self):
        pass

    def setUp(self):
        self.amino_one = Amino_one()
        self.test_dir = tempfile.TemporaryDirectory(prefix='temp_dir')
        self.test_file = os.path.join(self.test_dir.name, 'test_file')
        with open(self.test_file, 'w') as test_file:
            test_file.write("ARN")
        self.adres = []
        self.adres.append(self.test_file)

    @mock.patch("classes.aminowindow.Amino_one.dismiss_popup")
    def test_calcMass(self, mock_popup):
        mock_popup = self.mock_empty()
        self.amino_one.load(self.test_dir.name, self.adres)
        result = self.amino_one.calcMass()
        self.assertAlmostEqual(result, 341.18, 1)

    @mock.patch("classes.aminowindow.Amino_one.dismiss_popup")
    def test_calcIso(self, mock_popup):
        mock_popup = self.mock_empty()
        self.amino_one.load(self.test_dir.name, self.adres)
        result = float(self.amino_one.calcIso())
        self.assertAlmostEqual(result, 10.35, 1)

    def tearDown(self):
        del self.adres
        del self.amino_one
        del self.test_file
        self.test_dir.cleanup()

class Amino_threeTest(unittest.TestCase):

    def mock_empty(self):
        pass

    def setUp(self):
        self.amino_three = Amino_three()
        self.test_dir = tempfile.TemporaryDirectory(prefix='temp_dir')
        self.test_file = os.path.join(self.test_dir.name, 'test_file')
        with open(self.test_file, 'w') as test_file:
            test_file.write("AlaArgAsn")
        self.adres = []
        self.adres.append(self.test_file)

    @mock.patch("classes.aminowindow.Amino_three.dismiss_popup")
    def test_calcMass(self, mock_popup):
        mock_popup = self.mock_empty()
        self.amino_three.load(self.test_dir.name, self.adres)
        result = self.amino_three.calcMass()
        self.assertAlmostEqual(result, 341.18, 1)

    @mock.patch("classes.aminowindow.Amino_three.dismiss_popup")
    def test_calcIso(self, mock_popup):
        mock_popup = self.mock_empty()
        self.amino_three.load(self.test_dir.name, self.adres)
        result = float(self.amino_three.calcIso())
        self.assertAlmostEqual(result, 10.35, 1)

    def tearDown(self):
        del self.adres
        del self.amino_three
        del self.test_file
        self.test_dir.cleanup()

class CodonTest(unittest.TestCase):

    def mock_empty(self):
        pass

    def setUp(self):
        self.codon = Codon()
        self.test_dir = tempfile.TemporaryDirectory(prefix='temp_dir')
        self.test_file = os.path.join(self.test_dir.name, 'test_file')
        with open(self.test_file, 'w') as test_file:
            test_file.write("GCTCGTAAT")
        self.test_file_three = os.path.join(self.test_dir.name, 'test_file_three')
        with open(self.test_file_three, 'w') as test_file_three:
            test_file_three.write("AlaArgAsn")
        self.adres = []
        self.adres.append(self.test_file)
        self.adres_three = []
        self.adres_three.append(self.test_file_three)

    @mock.patch("classes.codonwindow.Codon.dismiss_popup")
    def test_calcMass_1(self, mock_dismiss):
        # print("test self.switch_one: {}".format(self.switch_one))
        mock_dismiss = self.mock_empty()
        self.codon.load(self.test_dir.name, self.adres)
        # self.codon.amino_creator_1()
        result = self.codon.calcMass_1()
        # print("test Codon caclMass_1, result: {}".format(result))
        self.assertAlmostEqual(result, 341.17, 1)

    @mock.patch("classes.codonwindow.Codon.switch_one")
    @mock.patch("classes.codonwindow.Codon.dismiss_popup")
    def test_calcMass_3(self, mock_switch, mock_dismiss):
        mock_switch = False
        mock_dismiss = self.mock_empty()
        self.codon.load(self.test_dir.name, self.adres_three)
        # self.codon.amino_creator_3()
        result = self.codon.calcMass_3()
        # print("test Codon three self.sequence: {}".format(self.codon.sequence))
        print("test Codon caclMass_3, result: {}".format(result))
        # self.assertAlmostEqual(result, 341.17, 1)


    def test_calcIso(self):
        pass
        #10.35


    def test_regex(self):
        pattern = '[ACTG]{3,10}'
        text = self.test_file
        result = False
        with open(self.test_file, 'r') as test_file:
            text = test_file.read()
            if re.match(pattern, text):
                result = True
            self.assertTrue(result)

    # def test_amino_creator_1(self):
    #     local_result = False
    #     for amino, nucleo in amino_dict(os.path.join(os.getcwd(),
    #                                     "docs/base.def")).items():
    #         for three in nucleo:
    #             if three == "AAA":
    #                 local_result = True
    #     self.assertTrue(local_result)

    # def test_amino_creator_1_codonstop(self):
    #     #codon stop can not be in a sequence
    #     #this program not count codon stop in theire structure, just ommited it
    #     #and not contain in base.def file
    #     local_result = False
    #     for amino, nucleo in amino_dict(os.path.join(os.getcwd(),
    #                                     "docs/base.def")).items():
    #         for three in nucleo:
    #             if three == "TAA":
    #                 local_result = True
    #     self.assertFalse(local_result)

    #do poprawy
    # @mock.patch("classes.codonwindow.Codon.sequence")
    # def test_calcMass_1(self, mock_sequence):
    #     mock_sequence = "ARN"
    #     #341.17
    #     # codon = Codon()
    #     result = self.codon.calcMass_1()
    #     print(result)
        # self.assertEqual(result, 341.17)

    #do poprawy
    # @mock.patch("classes.codonwindow.Codon.sequence")
    # def test_calcMass_3(self, mock_sequence):
    #     mock_sequence = "AlaArgAsn"
    #     #341.17
    #     result = self.codon.calcMass_3()
    #     print(result)
    #     self.assertEqual(result, 341.17)

    def tearDown(self):
        del self.adres
        del self.codon
        del self.test_file
        self.test_dir.cleanup()

if __name__ == '__main__':
    unittest.main()
