import json

x = '{ "firstName": "tester", "lastName": "tester", "city": "Vilnius"}'

y=json.loads(x)

print (y["firstName"])

y["firstName"] = "John"
y["lastName"] = "Doe"
y["Age"] = 30

updated_json = json.dumps(y)
print("\nThe manipulated json:")
print(updated_json)