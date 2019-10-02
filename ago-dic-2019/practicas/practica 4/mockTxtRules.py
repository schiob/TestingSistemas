import unittest
import TxtRules
from TxtRules import txtSub
from TxtRules import getLines
from unittest.mock import Mock
from unittest.mock import patch
import mock

# def func(case_path):
#     if case_path is "caps.txt":
#         return "ALCAPPPS"
#     elif case_path is "spaces.txt":
#         return "this is with spaces"
#     elif case_path is "numbers.txt":
#         return "184375493"
#     elif case_path is "chars.txt":
#         return "r3move!! &93ui c4r1^s"
#     elif case_path is "space_lines.txt":
#         return "que hubo\n!\n!!J"
#     elif case_path is "test.txt":
#         return "This is just your regular sentence, with numbers, such as 12 and special characters like +?!"
#

class TestMockTxtRules(unittest.TestCase):
    paths = ["caps.txt", "spaces.txt", "numbers.txt", "chars.txt", "space_lines.txt", "test.txt"]
    results = ["alcappps", "this is with spaces", "184375493", "r3move 93ui c4r1s", "que hubo\n\nj", "this is just your regular sentence with numbers such as 12 and special characters like "]
    file = ["ALCAPPPS", "this is with spaces", "184375493", "r3move!! &93ui c4r1^s", "que hubo\n!\n!!J", "This is just your regular sentence, with numbers, such as 12 and special characters like +?!"]

    @mock.patch('TxtRules.getLines')
    def testtxtSub(self, mock_open):
        #mock_open.return_value = func #lambda: "holi"

        for r in range(len(self.paths)):
            with self.subTest(r=r):
                mock_open.return_value = self.file[r]
                #with patch("TxtRules") as MokClass:
                #mock_open.return_value = self.func(self.paths[r])
                #instance = MokClass .return_value
                #instance.getLines.return_value = self.func[r]
                self.assertEqual(TxtRules.txtSub(self.paths[r]), self.results[r])
                mock_open.asser_called_with(self.paths[r])
if __name__ == '__main__':
    unittest.main()
