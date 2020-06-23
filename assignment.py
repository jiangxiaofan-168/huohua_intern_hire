import json
class CourseWareB():

    def load_raw_state(cls,raw_state):
        """
        答案状态在commonComponentState下的4cb5f12f9e164c6c545a55202bc818f2下的answer字段
        数据存储形式是list
        """
        state = json.loads(raw_state).get("commonComponentState")
        panel_status = []
        if state is not None:
            if "4cb5f12f9e164c6c545a55202bc818f2" in state:
                panel_status = state["4cb5f12f9e164c6c545a55202bc818f2"]["answer"]
        return panel_status

    def is_user_right(cls,stream):
        """
        正确答案是1，2，0，3
        """
        right_ans = [1, 2, 0, 3]
        return stream == right_ans

if __name__ == "__main__":
    """
    在这里处理日志输出，输出结果为result.csv，三个字段为：学生ID，状态，是否为正确状态
    """
    import pandas as pd
    with open('data.csv', 'r') as file:
        data = [line.split() for line in file]
    uid = [line[0] for line in data[1:]]
    states = [line[3] for line in data[1:]]
    ans = []
    for state in states:
        ans.append(CourseWareB().is_user_right(CourseWareB().load_raw_state(state)))
    states = [json.dumps(json.loads(line[3]).get("commonComponentState").get('4cb5f12f9e164c6c545a55202bc818f2')) for line in data[1:]]
    dataframe = pd.DataFrame({'uid':uid,'state':states,'if_state_true':ans})
    dataframe.to_csv("result.csv",index = False,sep = ',')
