########################
# 判断一个字符是否为回文 #
########################

word = "madam"

is_palindrome = word[::-1].find(word)
# string[::-1] 可以用来返回一个倒叙的字符串
# find(str, beg=0, end=len(string))
# str -- 指定检索的字符串
# beg -- 开始索引，默认=0
# end -- 结束索引，默认为字符串长度
# 如果包含字符串返回开始的索引值，否则返回-1
# 所以这里的意思是利用find()方法来返回一个倒叙的字符串是否包含其本身

print(is_palindrome)
# 如果是一个回文，结果会打印结果为0，否则打印-1

################################################
## Another way: BY A LOOP CONTINUOUS JUDGMENT ##
################################################

# while True:
#     word = input("Enter the content:")
#     if word == 'stop':
#         break
#     is_palindrome = word[::-1].find(word)
    
#     print(is_palindrome)