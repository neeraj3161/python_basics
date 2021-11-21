import unittest
from name_function import get_full_name
from name_function import get_formatted_name

class Name_function_test(unittest.TestCase):
    def test_function_formattedName(self):
        formatted_name=get_full_name('John','Cook')
        self.assertEqual(formatted_name,'John Cook')
# if __name__=='__main__':
#     unittest.main()

    # this is how we check if a code or fucntion will run

class Name_function_test2(unittest.TestCase):
    def test_another_function(self):
        formatted_name=get_formatted_name('Neeraj','Dhananjay','Tripathi')
        self.assertEqual(formatted_name,"Neeraj Dhananjay Tripathi")
if __name__=='__main__':
    unittest.main()