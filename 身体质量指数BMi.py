#身体质量指数BMi
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 10:36
# @Author  : LittleControl
# @Site    : 
# @File    : 身体质量指数BMi.py
# @Software: PyCharm
height,weight =eval(input("请输入身高（米）和体重（公斤）[逗号隔开]:"))
BMI=weight/pow(height,2)
print('BMI 数值为:{:.2f}'.format(BMI))
who,nat ='',''
if BMI <18.5:
    who,nat ='偏瘦','偏瘦'
elif 18.5<= BMI<24:
    who,nat ='正常','正常'
elif 24<=BIM<25:
    who,nat='偏胖','正常'
elif 25<=BMI<28:
    who,nat ='偏胖','偏胖'
elif 28<=BIM<30:
    who,nat ='肥胖','偏胖'
else:
    who,nat ='肥胖','肥胖'
print('BMI 指标为：国内{0},国际{1}'.format(who,nat))
