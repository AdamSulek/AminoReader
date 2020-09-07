import unittest
import os
import sys
import unittest.mock as mock
import tempfile
from classes.aminowindow import Amino_one
from classes.codonwindow import Codon

class Amino_oneTest(unittest.TestCase):

    def mock_empty(self):
        pass

    def setUp(self):
        self.amino_one = Amino_one()
        self.test_dir = tempfile.TemporaryDirectory(prefix='temp_dir')
        self.test_file = os.path.join(self.test_dir.name, 'test_file')
        with open(self.test_file, 'w') as test_file:
            test_file.write("ARNARN")
        self.adres = []
        self.adres.append(self.test_file)

    @mock.patch("classes.aminowindow.Amino_one.sequence")
    @mock.patch("classes.aminowindow.Amino_one.dismiss_popup")
    def test_calcMass(self, mock_popup, mock_seq):
        mock_popup = self.mock_empty()
        mock_seq = "ARN"
        result = self.amino_one.calcMass()
        print("result: {}".format(result))
        self.amino_one.load(self.test_dir.name, self.adres)

    # @mock.patch("classes.aminowindow.Amino_one.sequence")
    # @mock.patch("classes.aminowindow.Amino_one.dismiss_popup")
    # def test_calcMass(self, mock_popup, mock_seq):
    #     mock_seq = "ARN"
    #     mock_popup = self.mock_empty()
    #     # self.amino_one.load(self.test_dir.name, self.adres)
    #     result = self.amino_one.calcMass()
    #     print("result: {}".format(result))
    #     # print("self.amino_one.sequence: {}".format(self.amino_one.sequence))
    #     # self.assertEqual(result, 341.17)
    #     self.assertAlmostEqual(result, 341.18, 1)

class CodonTest(unittest.TestCase):

    def mock_empty(self):
        pass

    def setUp(self):
        self.codon = Codon()
        self.test_dir = tempfile.TemporaryDirectory(prefix='temp_dir')
        self.test_file = os.path.join(self.test_dir.name, 'test_file')
        with open(self.test_file, 'w') as test_file:
            test_file.write("RRAPNSPGRGATIHAEEKRMSPVASDLPSVVGDIGAQPH")
        self.adres = []
        self.adres.append(self.test_file)

    @mock.patch("classes.codonwindow.Codon.codon_input")
    @mock.patch("classes.codonwindow.Codon.sequence")
    @mock.patch("classes.codonwindow.Codon.switch_one")
    @mock.patch("classes.codonwindow.Codon.dismiss_popup")
    def test_Codon_load_ok_1(self, mock_popup, mock_switch, mock_seq, mock_codon_input):
        mock_popup = self.mock_empty()
        mock_codon_input = "GCTCGTAAT"
        mock_seq = "ARN"
        mock_switch = 1
        self.codon.load(self.test_dir.name, self.adres)

if __name__ == '__main__':
    unittest.main()
