users = {
    "id": 1,
    "name": "Anggy",
    "username": "AnggyTesting",
    "email": "AnggyTesting@gmail.com",
    "address": {
        "street": "jl. in Aja Ya",
        "suite": "Apt. 878",
        "city": "Wakanda",
        "zipcode": "65341",
        "geographic": {
            "lat": "656551",
            "lon": "-656854",
        }
    }
}
"""
Show information
"""
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geographic"])
print(users["address"]["geographic"]["lat"])


"""
Create a JSON file
"""
print("\nCreate JSON")
import json
result = json.dumps(users)
print(result)

with open('result.json','w') as file:
    json.dump(users, file)