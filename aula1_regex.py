import re

re.match('abc', 'abc')
print(re.match('abc', 'abc')) # <re.Match object; span=(0, 3), match='abc'>

# span é a posição que ele encontrou o texto
# match é o texto

re.match('abc', 'ewdabc')
print(re.match('abc', 'ewdabc')) # None

re.search('abc', 'ewdabc')
print(re.search('abc', 'ewdabc')) # <re.Match object; span=(3, 6), match='abc'>

# span=(3, 6) > posição onde encontrou o 'abc'

re.findall('abc', '123abc456abc')
print(re.findall('abc', '123abc456abc')) # ['abc', 'abc']
