import unittest
import os
from TxtRules import txtSub

class TestTxtRules(unittest.TestCase):
    file_name = "test.txt"
    tests = ["ALCAPPPS", "this is with spaces", "184375493", "r3move!! &93ui c4r1^s", "", " ", "!", "que hubo\n!\n!!J"]
    results = ["alcappps", "this is with spaces", "184375493", "r3move 93ui c4r1s", "", " ", "",  "que hubo\n\nj"]

    def crearArch(self,idx):
        f = open(self.file_name, "w+")
        f.write(self.tests[idx])
        f.close()

    def eliminarArch(self):
        os.remove(self.file_name)

    def test_txtSub(self):
         #for j in range(1):#
         for r in range(len(self.tests)):
             with self.subTest(r=r):
                 self.crearArch(r)
                 self.assertEqual(txtSub(self.file_name), self.results[r])
                 self.eliminarArch()

if __name__ == '__main__':
    unittest.main()
