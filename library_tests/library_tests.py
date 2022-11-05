from models.library import *
from models import library

import unittest

class TestLibrary(unittest.TestCase):
    
    def test_book_has_title(self):
        book_title = library.return_book_title("Becoming")
        self.assertEquals("Becoming",book_title)
