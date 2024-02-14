import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #This type of class will ALWAYS inherit from 'unittest.TestCase'
    """Tests for 'name_function.py"""

    def test_first_last_name(self): #Inside of this class, any method (def xxxx) with 'test_' in front will run automatically
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin') #This is the function we want to test
        self.assertEqual(formatted_name, 'Janis Joplin') #using 'assertEqual' to verify that the expected output is generated
    
    def test_first_middle_last_name(self):
        """Do names with middle names work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == "__main__":
    unittest.main()