import unittest
import os
import sys
import unittest.mock as mock
import tempfile
from classes.codonwindow import Codon

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

    @mock.patch("classes.codonwindow.Codon.switch_one")
    def test_Codon_load_ok_1(self, mock_switch):
        mock_switch = 1
        self.codon.load(self.test_dir.name, self.adres)

if __name__ == '__main__':
    unittest.main()
