
from random import randrange

m_list = []
chars = ['a', 'b', 'c', 'd', 'e']

for i in range(5):
    m_list.append(randrange(0, 150))
objs = { y : x for x, y in zip(chars, m_list) }
print(objs)
print(objs[max(objs)])


print(objs.values())