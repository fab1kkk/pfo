import unittest
import os

from utils import *



class TestUtils(unittest.TestCase):
    def test_get_file_extension_with_extension(self):
        docextension = get_file_extension('word.doc')
        pdfextension = get_file_extension('pdf.pdf')
        excelextension = get_file_extension('excel.xlsx')
        txtextension = get_file_extension('txt.txt')
        samplepath = get_file_extension(r'here\random\path\file.ext')
        self.assertEqual(docextension, 'doc')
        self.assertEqual(pdfextension, 'pdf')
        self.assertEqual(excelextension, 'xlsx')
        self.assertEqual(txtextension, 'txt')
        self.assertEqual(samplepath, 'ext')

    def test_get_file_extension_with_no_extension(self):
        noextension = get_file_extension('noextension')
        self.assertEqual(noextension, 'no_filetype')
        
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
        