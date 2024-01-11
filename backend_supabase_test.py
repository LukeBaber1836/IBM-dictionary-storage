import backend_supabase as db
import unittest   # The test framework


class Test_get_definition(unittest.TestCase):
    def test_single_definition(self):
        self.assertEqual(db.get_definition('hello'), 'Definition 1:  Expression of greeting used by two or more people who meet each other.\n \n')

    # This test is designed to fail for demonstration purposes.
    def test_over_5_definition(self):
        result = 'Definition 1:  Having a high temperature.\n \nDefinition 2:  Sexually attractive.\n \nDefinition 3:  The quality or state of being warm.\n \nDefinition 4:  Characterized by violent and forceful activity or movement; very intense.\n \nDefinition 5:  (color) bold and intense.\n \nDefinition 6:  Of, pertaining to, or containing spice; or spicy flavour: Provoking a burning sensation due to the presence of chillies or similar hot spices.\n \n'
        self.assertEqual(db.get_definition('hot'), result)

if __name__ == '__main__':
    unittest.main()