from re import match, search, findall, MULTILINE

# 1 - Metacaracter PONTO representa qualquer caracter.

# com o MATCH

match('.', 'abc')
match('.', '0123')
match('.', '   ')
match('.', '\t\t')

print(match('.', 'abc')) # <re.Match object; span=(0, 1), match='a'>
print(match('.', '0123')) # <re.Match object; span=(0, 1), match='0'>
print(match('.', '   ')) # <re.Match object; span=(0, 1), match=' '>
print(match('.', '\t\t')) # <re.Match object; span=(0, 1), match='\t'>

# \t é apenas um caracter, é o TAB
# o mesmo não acontece com o \n (que é a quebra de linha)

match('.', '\n') # None
print(match('.', '\n'))

# com o SEARCH funciona, ele não encontra em \n mas encontra no próximo elemento, o 'a'.

search('.', 'abc')
search('.', '\nabc')

print(search('.', 'abc')) # <re.Match object; span=(0, 1), match='a'>
print(search('.', '\nabc')) # <re.Match object; span=(1, 2), match='a'>

# com o FINDALL encontra o ponto em todas as ocorrências.

findall('.', 'abc')

print(findall('.', 'abc')) # ['a', 'b', 'c']

# 2 - Metacaracter ANCORA de início e fim de string são: ^ e o $

# o ^ é a âncora de ínicio de string

findall('^.', 'abc\ndef\nghi') # encontrar todas as ocorrencias de um caracter que esteja no início da string.
print(findall('^.', 'abc\ndef\nghi')) # ['a']

findall('^.', 'abc\ndef\nghi', MULTILINE) # encontrar todas as ocorrencias de um caracter que esteja no início da string de cada linha.
print(findall('^.', 'abc\ndef\nghi', MULTILINE)) # ['a', 'd', 'g']


# o $ é a âncora de fim de string

findall('.$', 'abc\ndef\nghi') # encontrar todas as ocorrencias de um caracter que esteja no fim da string.
print(findall('.$', 'abc\ndef\nghi')) # ['i']

findall('.$', 'abc\ndef\nghi', MULTILINE) # encontrar todas as ocorrencias de um caracter que esteja no fim da string de cada linha.
print(findall('.$', 'abc\ndef\nghi', MULTILINE)) # ['c', 'f', 'i']

# Combinação ^ com $

match('^.$', 'a') # aqui só funciona se tiver apenas 1 caracter.
match('^.$', 'abc')

print(match('^.$', 'a')) # <re.Match object; span=(0, 1), match='a'>
print(match('^.$', 'abc')) # None

match('^$', '') # aqui só funciona se for VAZIO.
match('^$', 'a')

print(match('^$', '')) # <re.Match object; span=(0, 0), match=''>
print(match('^$', 'a')) # None

findall('^$', '\n', MULTILINE)
print(findall('^$', '\n', MULTILINE)) # ['', '']