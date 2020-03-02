import unittest
from doceaveinticuatro import transform

class testTransform(unittest.TestCase):
    def test_transform(self):
        tts=[
            {'in':"02:23p.m", 'ex':"14:23hrs"},
            {'in':"11:42p.m", 'ex':"23:42hrs"},
            {'in':"11:42a.m", 'ex':"11:42hrs"},
            {'in':"12:00p.m", 'ex':"12:00hrs"},
            {'in':"12:00a.m", 'ex':"00:00hrs"},
            {'in':"02:23p.m", 'ex':"14:23hrs"},
            {'in':"01:05a.m", 'ex':"01:05hrs"},
            {'in':"11:59p.m", 'ex':"23:59hrs"},
         ]
        for tc in tts:
            self.assertEqual(transform(tc['in']), tc['ex'])


if __name__=="__main__":
    unittest.main()