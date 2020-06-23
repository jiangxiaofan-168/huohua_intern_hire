import unittest
from assignment import CourseWareB
import json


class AssignmentTest(unittest.TestCase):
    """
    这两个测试必写，你也可以增加其他你认为重要的测试
    """

    def test_load_state(self):
        #given
        raw_state = {
            "commonComponentState":{
                "4cb5f12f9e164c6c545a55202bc818f2":{
                    "answer":[1,3,0,3]}
            }
        }

        # WHEN
        result = CourseWareB().load_raw_state(json.dumps(raw_state))

        # THEN
        target_state = [1,3,0,3]
        self.assertEqual(target_state, result)
        
    def test_right_ans(self):
        # GIVEN
        stream = [1,2,0,3]
        # THEN
        self.assertTrue(CourseWareB().is_user_right(stream))

        stream = [2,3,1,4]
        self.assertTrue(not CourseWareB().is_user_right(stream))

        stream = [1,2,1,3]
        self.assertTrue(not CourseWareB().is_user_right(stream))
        
    #其他测试   
    def test_none_state(self):
        
        raw_state = {"commonComponentState":None}
        result = CourseWareB().load_raw_state(json.dumps(raw_state))
        
        target_state = []
        self.assertEqual(target_state, result)


if __name__ == "__main__":
    unittest.main()
