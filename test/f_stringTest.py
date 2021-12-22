"""
-------------------------------------------------
   File Name：     f_stringTest
   Description :
   Author :       DuanZhangjie
   date：         2021-12-21 16:57
-------------------------------------------------
"""
# f-string用大括号 {} 表示被替换字段，其中直接填入替换内容：
name = 'abc'
a = f'hello,{name}'
print(a)    #显示：hello,abc

# f-string的大括号 {} 可以填入表达式或调用函数，Python会求出其结果并填入返回的字符串内：
b=f'总数量是：{5*20+1}'
print(b)    #显示：总数量是：101
name='abc'
print(f'转化为大写：{name.upper()}')    #显示：转化为大写：ABC

# f-string大括号内所用的引号不能和大括号外的引号定界符冲突，可根据情况灵活切换 ' 和 "
# 若 ' 和 " 不足以满足要求，还可以使用 ''' 和 """
print(f"""He said {"I'm Eric"}""")

# f-string还可用于多行字符串：
a=f"""Hello,
1
2
3"""
print(a)

# 自定义格式：对齐、宽度、符号、补零、精度、进制等
# f-string采用 {content:format} 设置字符串格式，其中 content 是替换并填入字符串的内容，
# 可以是变量、表达式或函数等，format 是格式描述符。采用默认格式时不必指定 {:format}。
