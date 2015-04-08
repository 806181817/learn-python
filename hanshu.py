#提示用户输入相关信息
xuehao=raw_input('请输入学号:')
name=raw_input('请输入姓名:')
age=input('请输入年龄:')
gs=input('请输入高数成绩:')
yy=input('请输入英语成绩:')
zz=input('请输入政治成绩:')

#计算加权平均分(高数60%,英语30%,政治10%)
jq=gs*0.6 + yy*0.3 + zz*0.1

#打印所有的信息
print '学号:',xuehao, '姓名:', name, '年龄:', age
print '高数:',gs, '英语:',yy, '政治:',zz
print '加权平均分:', jq