num = input('digite os numeros com espaço:')
numeros = list(map(int,num.split()))
semduplicatas = set(numeros)
ordemdosnumeros = set (semduplicatas)
print(f' a ordem dos numeros é:{ordemdosnumeros}')
'''o split() serve para dividir a lista em pedaços
o set não deixa duplicar
map() transforma cada item'''
