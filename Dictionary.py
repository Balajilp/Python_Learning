user = {
    "name": "Balaji",
    "age": 20,
    "isCommitted": True
}
print(user)
print(type(user))
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x," ", user[x])
for x in user.values():
    print(x)
for x in user.keys():
    print(x)
for x,y in user.items():
    print(x,y)
if "age" in user:
    print("present")
# Changing values
user.update({"gender":"male"})
print(user)
user["age"] = 21
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
del user

users = {
    "user1":{
        "name": "Balaji",
        "age": 20,
        "isCommitted": True
    },
    "user2":{
        "name": "Lakshmi",
        "age": 18,
        "isCommitted": True
    }

}
print(users)