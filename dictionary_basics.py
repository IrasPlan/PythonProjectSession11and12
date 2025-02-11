from os import times_result

d = {} # empty dictionary
print(d)

eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
print(eng_to_spa["one"])
eng_to_spa["tree"] = "arbol" #add item into dictionary
print(eng_to_spa["tree"])
eng_to_spa.update({"yes": "si", "no": "no"})
print(eng_to_spa)

del eng_to_spa["yes"]
print(eng_to_spa)

print("These are the spanish words that I know")
for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")

print(dir(eng_to_spa))
#['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
eng_spa2 = eng_to_spa.copy()
eng_to_spa.clear()
print(eng_spa2)

new_d = eng_spa2.fromkeys(eng_spa2, "YES")
print(new_d)
#get is one of hte most useful
print(f"car in spanish is {eng_spa2.get('car', 'UNKNOWN')}")
print(list(eng_spa2.items()))
eng_spa2.setdefault("red", "rojo")
print(eng_spa2)






