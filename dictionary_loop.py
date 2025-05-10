thisdisk = {
    'a': 1,
    'b': 2,
    'c': 3,
}

for key in thisdisk:
    print(key, thisdisk[key])

for key, value in thisdisk.items():
    print(key, value)


for key in thisdisk.keys():
    print(key, thisdisk[key])
    
for value in thisdisk.values():
    print(value)