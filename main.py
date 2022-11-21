#!/usr/bin/python3
from models import *
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity

print('create state')
s = State(name="California")
s.save()
print(s)

print('-- create city')
c = City(state_id=s.id, name="San Francisco")
c.save()
print(c)

print('-- create user')
u = User(email="a@a.com", password="pwd")
u.save()
print(u)

print('-- create place 1')
p1 = Place(user_id=u.id, city_id=c.id, name="House 1")
p1.save()
print(p1)

print('-- create place 2')
p2 = Place(user_id=u.id, city_id=c.id, name="House 2")
p2.save()
print(p2)

a1 = Amenity(name="Wifi")
a1.save()
a2 = Amenity(name="Cable")
a2.save()
a3 = Amenity(name="Eth")
a3.save()

p1.amenities.append(a1)
p1.amenities.append(a2)

p2.amenities.append(a1)
p2.amenities.append(a2)
p2.amenities.append(a3)

storage.save()
print('last line')
