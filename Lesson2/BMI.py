
OBESE_BMI = 30
SLIM_BMI = 18.5
EX_SLIM_BMI = 16

bmi = 2133

if bmi >= OBESE_BMI:
    print("You are overweight!")
elif bmi > SLIM_BMI:
    print("You are in great shape!")
elif bmi > EX_SLIM_BMI:
    print("You are too slim!")
else:
    print("You are extremly slim! See Dr Now!")

import random
print(random.randrange(0,100))

#猜数字，游戏一开始会生成一个随机数（0-100），依次猜这个数字，并且告诉你是否猜中，如果没猜中的话
# 告诉你猜的数字是大了还是小了。直到猜中为止。


'''
if car:
    print("if called, means if status is True")
else:
    print("else called, means if status is False")
'''