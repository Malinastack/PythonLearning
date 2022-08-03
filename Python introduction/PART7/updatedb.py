import shelve
db = shelve.open('persondb')
print(type(db))
for key, value in db.items():
    print(key, ':', value)

anna = db['Anna Red']
anna.give_raise(10)
db['Anna Red'] = anna
db.close()
