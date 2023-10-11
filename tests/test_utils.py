import unittest
import os

from utils import *
from configs import MODES

ROOT_DIR = os.getcwd()
TEST_DIR = ROOT_DIR + r"\tests\sample_files"


class TestUtils(unittest.TestCase):
    def test_get_files_from_existing_dir(self):
        total_files_in_test_dir = len(os.listdir(TEST_DIR))
        files_in_test_dir = os.listdir(TEST_DIR)
        
        self.assertEqual(len(get_files_from_dir(TEST_DIR)), total_files_in_test_dir)
        for file in files_in_test_dir:
            self.assertIn(file, get_files_from_dir(TEST_DIR))
        
    def test_get_file_extension_with_extension(self):
        docextension = get_file_extension('word.doc')
        pdfextension = get_file_extension('pdf.pdf')
        excelextension = get_file_extension('excel.xlsx')
        txtextension = get_file_extension('txt.txt')
        self.assertEqual(docextension, 'doc')
        self.assertEqual(pdfextension, 'pdf')
        self.assertEqual(excelextension, 'xlsx')
        self.assertEqual(txtextension, 'txt')

    def test_get_file_extension_with_no_extension(self):
        noextension = get_file_extension('noextension')
        self.assertEqual(noextension, None)
        
    def test_mode_allowed(self):
        modes = [mode for mode in MODES]
        for mode in modes:
            self.assertEqual(True, mode_allowed(mode))

    def test_mode_not_allowed(self):
        mode = 'thereisnosuchmode'
        self.assertEqual(False, mode_allowed(mode))
        