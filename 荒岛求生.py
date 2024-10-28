"""

一、有一个荒岛，只有左右两个港口，只有一座桥连接这两个港口，现在有一群人需要从两个港口逃生，有的人往右逃生，有的往左逃生，如果两个人相遇，则PK一下，体力值大的能够打赢体力值小的，体力值相同则同归于尽，赢的人才能继续往前逃生，并减少相应的体力。
二、输入描述
一行非0整数，用空格隔开，整数代表向右逃生 ，负数代表向左逃生，整数绝对值代表体力值。
10 20 -20 -5 10
三、输出描述
最多能够逃生的人数

"""


def escape_people(people):
    right_stack = []
    left_stack = []

    for person in people:
        if person > 0:
            right_stack.append(person)
        else:
            left_stack.append(-person)

    while right_stack and left_stack:
        right_person = right_stack[-1]
        left_person = left_stack[-1]

        if right_person > left_person:
            right_stack[-1] -= left_person  # 更新右边人的体力
            left_stack.pop()  # 左边人被淘汰
        elif right_person < left_person:
            left_stack[-1] -= right_person  # 更新左边人的体力
            right_stack.pop()  # 右边人被淘汰
        else:
            right_stack.pop()  # 两人同归于尽
            left_stack.pop()

    return len(right_stack) + len(left_stack)


# 输入示例
# input_data = "10 20 -20 -5 10"

input_data = "5 10 8 -8 -5"

people = list(map(int, input_data.split()))
result = escape_people(people)
print(result)


