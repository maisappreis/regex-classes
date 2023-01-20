from re import match, search, findall, MULTILINE

# Classes de Caracteres
# Se declara uma classe de caracteres com []

# pegar as vogais
findall('[aeiou]', 'Maisa Pierini Preis')
print(findall('[aeiou]', 'Maisa Pierini Preis')) # ['a', 'i', 'a', 'i', 'e', 'i', 'i', 'e', 'i']

# Se tiver o ^ dentro do [], é uma negação.

# não pegar vogais, ou seja, pegará tudo exceto as vogais.
findall('[^aeiou]', 'Maisa Pierini Preis')
print(findall('[^aeiou]', 'Maisa Pierini Preis')) # ['M', 's', ' ', 'P', 'r', 'n', ' ', 'P', 'r', 's']

# Definir um range, um intevalo

findall('[i-r]', 'Maisa Pierini Preis')
print(findall('[i-r]', 'Maisa Pierini Preis')) # ['i', 'i', 'r', 'i', 'n', 'i', 'r', 'i']

# Definir mulyiplos ranges, intervalos

findall('[a-fA-z]', 'Maisa Pierini Preis')
print(findall('[a-fA-z]', 'Maisa Pierini Preis')) # ['M', 'a', 'i', 's', 'a', 'P', 'i', 'e', 'r', 'i', 'n', 'i', 'P', 'r', 'e', 'i', 's']

# SEQUENCIAS ESPECIAIS - são ranges muito usadas.
# abreviações equivalentes.

findall('[a-zA-Z0-9_]') # De A a Z minusculo e maiusculo, e numeros de 0 a 9, ou o _
findall('[\w]') # ou apenas findall('\w') 

findall('[^a-zA-Z0-9_]')
findall('[\W]')

findall('[0-9]')
findall('[\d]')

findall('[^0-9]')
findall('[\D]')

findall('[\t\n\r\f\v]')
findall('[\s]')

findall('[^\t\n\r\f\v]')
findall('[\S]')







