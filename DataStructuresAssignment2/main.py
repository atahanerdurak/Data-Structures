from HashTable import HashTable

table = HashTable()
table['a'] = 1
table['b'] = 34
print(table['a'] == 1 and table['b'] == 34)

table['a'] = 99
print(table['a'] == 99)
print(list(table))