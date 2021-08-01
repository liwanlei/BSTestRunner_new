'''
  @Description      
  @auther         leizi
'''
import  unittest,os
from  BSTestRunner import  BSTestRunner
BASH_DIR="history"
report_path = os.path.join(BASH_DIR,"test.html")
openone = open(report_path, 'w+')
class  Clasee(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def testoen(self):
        self.assertEqual(1,2)
if __name__=="__main__":
    besautiful = BSTestRunner(title="报告",
                              description="测试报告",
                              stream=openone,
                              trynum=2,
                              filepath=BASH_DIR,
                              is_show=True)
    test_suit = unittest.TestSuite()
    test_suit.addTests([Clasee("testoen")])
    besautiful.run(test_suit)