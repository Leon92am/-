#!usr/bin/env python
# encoding:utf-8
def BracketMatch(string):
    stack = []
    for str1 in string:         #这个循环用来遍历字符串
        if str1 in ["{","[","("]:
            stack.append(str1)
            if len(stack)>=2:
                print stack
                if ["{","[","("].index(str1)<["{","[","("].index(stack[len(stack)-2]): #判断符号优先级
                    return False  #如果优先级不合法就返回False
                elif ["{","[","("].index(str1)==["{","[","("].index(stack[len(stack)-2])and str1 in ["[","("]:#判断连续嵌套是否合法
                    return False  #如果嵌套不合法就返回False
        elif str1 in ["}","]",")"]:
            if str1 == ")" and stack[len(stack)-1] != "(" or str1 =="]" and stack[len(stack)-1]!= "[" or str1 == "}" and stack[len(stack)-1] != "{":   #判断列表中最后一个元素与当前右括号的关系
                return False
            else:
                stack.pop()     #当列表中最后一个元素与当前右括号对应，就进行出栈操作
    if stack == []:             #如果最后列表为空就返回True
        return True
    else:                       #如果列表不为空就返回False
        return False
print(BracketMatch("{[(2+3)*(1-3)]+4}*(14-3)"))
