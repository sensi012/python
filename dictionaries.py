################################################
# dictionaries
################################################
capitals = {"USA": "Washington D.C",
"India": "New Dehli", 
"Russia": "Moscow"
}

# print(dir(capitals))

# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})

# print(capitals)

# capitals.update({"USA": "Detroit"})
# print(capitals)

# capitals.pop("Russia")
# print(capitals)

# capitals.popitem()
# print(capitals)

# capitals.clear()
# print(capitals)

# keys = capitals.keys()
# print(capitals)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")