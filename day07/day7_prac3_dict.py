# ==========================================
# 3. Dictionaries
# ==========================================

person = {
    "name": "Ahmad",
    "age": 25,
    "city": "Lahore"
}

print(person)

#Direct Lookup
print(person["age"])

print(person["name"])

print(person["city"])

#.get()
print("Name: ", person.get("name"))

print("City: ", person.get("city"))

print("Age: ", person.get("age"))

print("Country:", person.get("country"))

print("Country: ", person.get("country", "Unknown"))

#setdefault()
person.setdefault("Country", "Pakistan")

print(person.get("Country"))

print(person)

person.setdefault("age", 45)

print(person)

#update()
person.update({
    "age": 34,
    "profession": "Python Dev"
})

print(person)

#keys()
print(person.keys())

#items()
for key, value in person.items():
    print(key, "=", value)

#values()
print(person.values())

#Dectionary Membership
print("name" in person)

print("Ahmad" in person)

print("Country" in person)

#Delete command
del person["city"]

print(person)

#checks keys
print("name" in person)

#checks values
print("Ahmad" in person.values())