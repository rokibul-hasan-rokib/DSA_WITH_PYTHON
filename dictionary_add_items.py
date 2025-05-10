thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["color"] = "red"
thisdict["engine"] = "V8"
thisdict["year"] = 2020

print(thisdict)

thisdict.update({"color": "blue", "engine": "V6"})
print(thisdict)