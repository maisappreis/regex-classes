from re import match, search, findall, MULTILINE

# a barra \ se torna um caracte especial se acompanhada de certas letras
# Como nestas: \t\n\r\f\v
# Então, se eu realmente quiser a \ como uma string, e não como um caracter especial
# Eu tenho uma forma de bular isso.

print('1\n2')
# 1
# 2
print('1\\n2') # 1\n2

text = '\\section\n'
print(text) # \section

print(match('\\section', text)) # None
print(match('\\\\section', text)) # <re.Match object; span=(0, 8), match='\\section'>

# Para resolver todo esse problema de forma fácil, basta usar a String Raw
# basta colocar um 'r'

print(match(r'\\section', text)) # <re.Match object; span=(0, 8), match='\\section'>

