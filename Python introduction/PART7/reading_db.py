import glob
import shelve
print(glob.glob('person*'))
# print(open('persondb').read()) # nie dziala
db = shelve.open('persondb')
print(len(db))
print(list(db.keys()))

for key, value in db.items():
    print(key, ':', value)