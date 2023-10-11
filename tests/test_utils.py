import unittest
import os

from utils import *

ROOT_DIR = os.getcwd()
TEST_DIR = ROOT_DIR + r"\tests\sample_files"


class TestUtils(unittest.TestCase):
    def test_get_files_from_existing_dir(self):
        total_files_in_test_dir = len(os.listdir(TEST_DIR))
        files_in_test_dir = os.listdir(TEST_DIR)
        
        self.assertEqual(len(get_files_from_dir(TEST_DIR)), total_files_in_test_dir)
        for file in files_in_test_dir:
            self.assertIn(file, get_files_from_dir(TEST_DIR))
            
    def test_get_files_from_not_existing_dir(self):
        self.assertRaises(FileNotFoundError, lambda: get_files_from_dir('path/that/doesnt/exist'))
        
    def test_get_files_from_dir_invalid_input(self):
        self.assertRaises(TypeError, lambda: get_files_from_dir(None))
        
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
        modeslist = ['list1', 'list2']
        modeset = {'set1', 'set2'}
        modestuple = ('tuple1', 'tupl2')
        self.assertEqual(True, mode_allowed('list1', modeslist))
        self.assertEqual(True, mode_allowed('set1', modeset))
        self.assertEqual(True, mode_allowed('tuple1', modestuple))
        
        self.assertEqual(False, mode_allowed('fakemode', modeslist))
        self.assertEqual(False, mode_allowed('fakemode', modeset))
        self.assertEqual(False, mode_allowed('fakemode', modestuple))

    def test_mode_allowed_invalid_input(self):
        modes = ['mode1', 'mode2', 2, 3]
        self.assertRaises(TypeError, lambda : mode_allowed(None, modes))
        