users = {
    "id": 1,
    "name": "ameer",
    "username": "ameerkhan",
    "email": "ameerkhan@gmail.com",
    "address": {
        "street": "jl. Ameer",
        "suite": "Apt. 878",
        "city": "Wakanda",
        "zipcode": "65341",
        "geographic": {
            "lat": "656551",
            "lon": "-656854",
        }
    }
}

print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geographic"])
print(users["address"]["geographic"]["lat"])

print("\nUbah JSON")
import json
result = json.dumps(users)
print(result)

with open('result.json','w') as file:
    json.dump(users, file)