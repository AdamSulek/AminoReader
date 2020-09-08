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
        mock_dismiss = self.mock_empty()
        self.codon.load(self.test_dir.name, self.adres)
        result = self.codon.calcMass_1()
        self.assertAlmostEqual(result, 341.17, 1)

    @mock.patch("classes.codonwindow.Codon.dismiss_popup")
    def test_calcIso_1(self, mock_dismiss):
        mock_dismiss = self.mock_empty()
        self.codon.load(self.test_dir.name, self.adres)
        result = float(self.codon.calcIso_1())
        self.assertAlmostEqual(result, 10.35, 1)

    def test_regex(self):
        pattern = '[ACTG]{3,10}'
        text = self.test_file
        result = True
        with open(self.test_file, 'r') as test_file:
            text = test_file.read()
            if not re.match(pattern, text):
                result = False
            self.assertFalse(result)

    def tearDown(self):
        del self.adres
        del self.codon
        del self.test_file
        self.test_dir.cleanup()

if __name__ == '__main__':
    unittest.main()
