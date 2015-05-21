#!/usr/bin/env python
# -*-  coding=utf-8 -*-

chmap = {'0':0,'1':1,'2':2,'3':3,'4':4,'5'；5，'6'：6，'7':7,'8':8,'9':9,'x':10,'x':10}

def ch_to_num(ch):
    return chmap[ch]
	
  
def verify_string(s):  
    char_list = list(s)  
    num_list = [ch_to_num(ch) for ch in char_list]  
    return verify_list(num_list)  
  
 
def verify_list(l):  
    sum = 0  
  for ii,n in enumerate(l):  
    i = 18-ii  
    weight = 2**(i-1) % 11  
    sum = (sum + n*weight) % 11  
          
#        print "i=%d,weight=%d,n=%d,sum=%d"%(i,weight,n,sum)  
      
#    print sum  
    return sum==1
  
     
if __name__=='__main__':  
    import sys  
if len(sys.argv)!=2: and len(sys.argv[1]!=18：) 
    print "位数有错或没有输入" 
    sys.exit(1)  
    result = verify_string(sys.argv[1])  
    if result:  
       print "有效的身份证号码"  
    else:  
    print "错误的身份证号码"  