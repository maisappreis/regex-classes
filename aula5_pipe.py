from re import match

# Metacaracter Pipe
# Ele faz o OU

match('a|b', 'abc')
match('a|b', 'bce')
match('a|b', 'cde')

print(match('a|b', 'abc')) # <re.Match object; span=(0, 1), match='a'>
print(match('a|b', 'bce')) # <re.Match object; span=(0, 1), match='b'>
print(match('a|b', 'cde')) # None


