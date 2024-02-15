import json

merged_users = {}

# Read and merge data from users1.json
with open('users1.json') as f:
    data = json.load(f)
    users = data.get("table", {}).get("users", {})
    merged_users.update(users)

# Merge data from users2.json
with open('users2.json') as f:
    data = json.load(f)
    users = data.get("table", {}).get("users", {})
    for user_id, user_data in users.items():
        if user_id not in merged_users:
            merged_users[user_id] = user_data

# Write merged data to users.json
with open('users.json', 'w') as f:
    json.dump({"table": {"users": merged_users}}, f, indent=4)
