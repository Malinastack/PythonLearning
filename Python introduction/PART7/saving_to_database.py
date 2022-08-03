from person import Person, Manager
import shelve

bob = Person('Roberto Green')
anna = Person('Anna Red', job='programist', pay=4500)
tom = Manager('Thomas Black', 15000)
db = shelve.open('persondb')
for obj in (bob, anna, tom):
    db[obj.name] = obj
db.close()


