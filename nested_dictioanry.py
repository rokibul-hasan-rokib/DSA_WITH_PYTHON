myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}


myfamily = {    
    "child1": child1,    
    "child2": child2,    
    "child3": child3
}

for x, obj in myfamily.items():
    print(x)
    print(obj["name"])
    print(obj["year"])

    for y in obj:
        print(y)
    # Output: Emil