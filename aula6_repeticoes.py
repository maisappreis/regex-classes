from re import match, findall

# Quantidades Específicas
# Exemplo: ele espera receber exatamente 4, nem menos, nem mais.

match(r'\d{4}', '1234') # Pega os 4
match(r'\d{4}', '123') # None
match(r'\d{4}', '12345') # Só pega os 4 primeiros, ignora o 5

print(match(r'\d{4}', '1234')) # <re.Match object; span=(0, 4), match='1234'>
print(match(r'\d{4}', '123')) # None, por que não tem 4
print(match(r'\d{4}', '12345')) # <re.Match object; span=(0, 4), match='1234'>


# Quantidades Mínimas
# Exemplo: ele espera receber no mínimo 2, então é 2 ou mais.

match(r'\d{2,}', '12') # pega os 2
match(r'\d{2,}', '123456789') # pega todos
match(r'\d{2,}', '1') # None, porque só tem 1

print(match(r'\d{2,}', '12')) # <re.Match object; span=(0, 2), match='12'>
print(match(r'\d{2,}', '123456789')) # <re.Match object; span=(0, 9), match='123456789'>
print(match(r'\d{2,}', '1')) # None

# Mas, se eu colocar esse ? eu transformo o padrão de Ganancioso para Preguiçoso.
match(r'\d{2,}?', '123456789') # <re.Match object; span=(0, 2), match='12'>


# Quantidades Mínimas e Máximas
# Exemplo: ele espera receber no mínimo 2 e máximo de 4.

match(r'\d{2,4}', '12345')
match(r'\d{2,4}', '1234')
match(r'\d{2,4}', '123')
match(r'\d{2,4}', '1')

print(match(r'\d{2,4}', '12345')) # <re.Match object; span=(0, 4), match='1234'>
print(match(r'\d{2,4}', '1234')) # <re.Match object; span=(0, 4), match='1234'>
print(match(r'\d{2,4}', '123')) # <re.Match object; span=(0, 3), match='123'>
print(match(r'\d{2,4}', '1')) # None


# Mas, se eu colocar esse ? eu transformo o padrão de Ganancioso para Preguiçoso.
# Ele pega apenas o mínimo
print(match(r'\d{2,4}?', '12345')) # <re.Match object; span=(0, 2), match='12'>


# Quero 0 ou 1 ocorrência:

match(r'\d{0,1}', '12345')
match(r'\d{,1}', '12345') # posso omitir o 0 que funciona igual
match(r'\d{,1}?', '12345') # aqui ele pega o mínimo possível, e o mínimo é 0

print(match(r'\d{0,1}', '12345')) # <re.Match object; span=(0, 1), match='1'>
print(match(r'\d{,1}', '12345')) # <re.Match object; span=(0, 1), match='1'>
print(match(r'\d{,1}?', '12345')) # <re.Match object; span=(0, 0), match=''>

# Outra maneira de fazer 0 ou 1 ocultando as {} e adicionando o ?
# a primeira ? é o modificador de repetição, e repete o que vem antes
# a segunda ? é o modificador do operador de repetição, que transforma de ganancioso para preguiçoso

match(r'\d?', '12345') # Fez 0 ou 1 e pegou o máximo possível: gananciosa pega o 1
match(r'\d??', '12345') # Fez 0 ou 1 e pegou o mínimo possível: preguiçosa pega o 0


# Quero 0 ou MAIS ocorrências

match(r'\d{0,}', '12345') # <re.Match object; span=(0, 5), match='12345'>
match(r'\d{,}', '12345') # <re.Match object; span=(0, 5), match='12345'>

print(match(r'\d{0,}', '12345'))
print(match(r'\d{,}', '12345'))

# Outra maneira de fazer 0 ou MAIS é ocultando as {} e adicionando o *
# o * indica que ele quer o anterior ocorrendo 0 ou mais vezes.

match(r'\d*', '12345') # ganancioso
match(r'\d*?', '12345') # preguiçoso

print(match(r'\d*', '12345')) # <re.Match object; span=(0, 5), match='12345'>
print(match(r'\d*?', '12345')) # <re.Match object; span=(0, 0), match=''>


# Quero 1 ou MAIS ocorrências

match(r'\d{1,}', '12345')
print(match(r'\d{1,}', '12345')) # <re.Match object; span=(0, 5), match='12345'>

# Outra maneira de fazer 1 ou MAIS é ocultando as {} e adicionando o +

match(r'\d+', '12345') # ganancioso
match(r'\d+', 'abc') # None, só aceita dígito
match(r'\d+?', '12345') # preguiçoso

print(match(r'\d+', '12345')) # <re.Match object; span=(0, 5), match='12345'>
print(match(r'\d+', 'abc')) # None, só aceita dígito
print(match(r'\d+?', '12345')) # <re.Match object; span=(0, 1), match='1'>


# Importância do ? preguiçoso

text = 'attr1="value1" attr2="value2"'

print(findall(r'".+"', text)) # ['"value1" attr2="value2"']
print(findall(r'".+?"', text)) # ['"value1"', '"value2"']

# Porém usar o + pode ser perigoso caso se tenha atributos vazios.

text2 = 'attr1="" attr2=""'
print(findall(r'".+?"', text2)) # ['"" attr2="']
print(findall(r'".*?"', text2)) # ['""', '""']


# Match Object

m = match(r'\d+', '12345')

print(type(m)) # <class 're.Match'>
print(m.group()) # 12345
print(m.start()) # 0
print(m.end()) # 5
print(m.span()) # (0, 5) > tupla do Start e End
print(match(r'\s+', '1234')) # None, porque não encontra a corrêspondencia.


# Grupo de Captura é entre ()
# Expressões regurares não são apenas para checar padrões na string
# Também servem para extrair informações dela

html1 = '<input type="text" id="id_cpf" name="cpf">'

# quero que faça match com qqr caracter antes de um espaço.

pattern = r'<(.+?) type="(.+?)" id="(.+?)" name="(.+?)"'
p = match(pattern, html1)

print(p) # <re.Match object; span=(0, 41), match='<input type="text" id="id_cpf" name="cpf"'>
print(p.groups()) # ('input', 'text', 'id_cpf', 'cpf')
print(p.group(0)) # <input type="text" id="id_cpf" name="cpf"
print(p.group(1)) # input
print(p.group(2)) # text
print(p.group(3)) # id_cpf
print(p.group(3, 2, 1)) # ('id_cpf', 'text', 'input')


# Grupo de Não Captura
# quando está fora de ordem, por exemplo.

html2 = '<input id="id_cpf" name="cpf" type="text">'

pattern2 = r'<(.+?) (?:(?:type="(.+?)"|id="(.+?)"|name="(.+?)") ?)*'

n = match(pattern2, html1)
print(n) # <re.Match object; span=(0, 41), match='<input type="text" id="id_cpf" name="cpf"'>
print(n.groups()) # ('input', 'text', 'id_cpf', 'cpf')

q = match(pattern2, html2)
print(q) # <re.Match object; span=(0, 41), match='<input id="id_cpf" name="cpf" type="text"'>
print(q.groups()) # ('input', 'text', 'id_cpf', 'cpf')





