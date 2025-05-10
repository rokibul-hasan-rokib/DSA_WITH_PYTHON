thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["color"] = "red"
thisdict["engine"] = "V8"
thisdict["year"] = 2020
thisdict["model"] = "Focus"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict.clear()
print(thisdict)

del thisdict
print(thisdict)