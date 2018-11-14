'''
编写一个程序，使它完成以下几件事：首先，它应该读入一行输入，这行就是被加密的消息，这个消息包括大写字母和空格。
你的程序必须测试所有26种可能的移位值S；在这26个可能的原消息中，打印出那个强度最高的。
'''

# 定义变量letterGoodness，它是一个长度为26的列表（列表中的每一项都对应频率表中每个字母的强度值）
letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127,
                  0.0223, 0.0202, 0.0609, 0.0697, 0.0015,
                  0.0077, 0.0402, 0.0241, 0.0675, 0.0751,
                  0.0193, 0.0009, 0.0599, 0.0633, 0.0906,
                  0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]

code = input()
n = 0
maxSUM = 0.0
result = ''
while n < 26:
    sumOfLetters = 0.0
    decoding = ''
    for i in code:
        if i != ' ':
            newCode = ord(i) + n
            if newCode > ord('Z'):
                newCode = newCode - ord('Z') + ord('A') - 1
            idx = newCode - ord('A')
            sumOfLetters += letterGoodness[idx]
        else:
            newCode = 32
        decoding += chr(newCode)
    if maxSUM < sumOfLetters:
        maxSUM = sumOfLetters
        result = decoding
    n += 1

print(result)

#test
#>>> LQKP OG CV GKIJV DA VJG BQQ   - >  JOIN ME AT EIGHT BY THE ZOO
#>>> UIJT JT B TBNQMF MJOF PG UFYU GPS EFDSZQUJOH  ->  THIS IS A SAMPLE LINE OF TEXT FOR DECRYPTING
#>>> S KW DRO FOBI WYNOV YP K WYNOBX WKTYB QOXOBKV  ->  I AM THE VERY MODEL OF A MODERN MAJOR GENERAL
#>>> DQLMW SQTTML BPM ZILQW ABIZ  ->  VIDEO KILLED THE RADIO STAR
#>>> JAZZ  ->  OFEE
#>>> THE SHIFT COULD ALSO EQUAL ZERO  ->  THE SHIFT COULD ALSO EQUAL ZERO
#>>> CAESARS JVTIVK JRCRU IVTZGV  ->  LJNBJAB SECRET SALAD RECIPE
