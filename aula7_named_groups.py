from re import match

# Quando tempo uma Espressão Regular com vários grupos, pode ser difícil ler o id de cada um deles
# Por isso, o Python tem uma extenção específica chamada Named Group
# Basta adicionar: ?P<nome>


html1 = '<input type="text" id="id_cpf" name="cpf">'

html2 = '<input id="id_cpf" name="cpf" type="text">'


pattern2 = r'<(?P<tag>.+?) (?:(?:type="(?P<type>.+?)"|id="(.+?)"|name="(?P<name>.+?)") ?)*'

m = match(pattern2, html1)

print(m.groups()) # ('input', 'text', 'id_cpf', 'cpf')
print(m.groupdict()) # {'tag': 'input', 'type': 'text', 'name': 'cpf'}