import unittest
import os

from utils import *
from configs import MODES


ROOT_DIR = os.getcwd()
TEST_DIR = ROOT_DIR + r"\tests\sample_files"

def mock_sample_files():
    return ['word.doc', 'pdf.pdf', 'excel.xlsx', 'txt.txt']


class TestUtils(unittest.TestCase):
    def test_get_files_from_existing_dir(self):
        files_in_test_dir = len(os.listdir(TEST_DIR))
        self.assertEqual(len(get_files_from_dir(TEST_DIR)), files_in_test_dir)
        
    def test_get_file_extension(self):
        docextension = get_file_extension('word.doc')
        pdfextension = get_file_extension('pdf.pdf')
        excelextension = get_file_extension('excel.xlsx')
        txtextension = get_file_extension('txt.txt')
        noextension = get_file_extension('noextension')
        self.assertEqual(docextension, 'doc')
        self.assertEqual(pdfextension, 'pdf')
        self.assertEqual(excelextension, 'xlsx')
        self.assertEqual(txtextension, 'txt')
        self.assertEqual(noextension, None)
