#-*- coding:utf-8 -*- 

######学生基本信息############ 
#姓名： 赵岩
#学号： 1403050227
#班级： 通风14-2班

#物理题：17.28 
###########题目############### 
import math

I0=3.0
I1=1.0/2*I0
I2=I1*math.cos(math.radians(30))**2
I3=I2*math.cos(math.radians(30))**2
I4=I3*math.cos(math.radians(30))**2
I4/I1

print 'I4/I1的比值为:',I4/I1
