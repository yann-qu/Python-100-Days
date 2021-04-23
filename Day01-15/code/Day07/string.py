'''
Author: Yannq
Date: 2021-02-18 18:43:11
LastEditTime: 2021-02-18 21:54:11
LastEditors: Yannq
FilePath: \Day07\string.py
Description: python字符串的常用操作
Attention: 
'''
# %%
str1 = 'hello world'

# %%
# 切片
print(str1[1:5])
# %%
# 反转
print(str1[::-1])
# %%
# step = 2
print(str1[::2])
# %%
# 计算字符串长度
print(len(str1))
# %%
# 获得字符串首字母大写的拷贝
print(str1.capitalize())
# %%
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())
# %%
# 获得字符串变大写的拷贝
print(str1.upper())
# %%
# 查找字符串子串
print(str1.find('llo'))
# %%
# 查找是否以指定的字符串开头
print(str1.startswith('Hel')) # 区分大小写
print(str1.startswith('hel'))
# %%
# 检查是否以指定的字符串结尾
print(str1.endswith('ld'))
# %%
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
# %%
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
# %%
str3 = '  yannqu@qq.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())


# %%
# 格式化字符串输出
a, b = 3, 5
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b)) # 数字下标和后面的顺序是对应的
print(f'{a} * {b} = {a * b}')
# %%
