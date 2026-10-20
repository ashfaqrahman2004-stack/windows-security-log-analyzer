from collections import Counter

logs = [
    "SUCCESS user=ashfaq",
    "FAILED user=rahul",
    "FAILED user=rahul",
    "FAILED user=rahul",
    "SUCCESS user=ashfaq",
    "FAILED user=amal",
]

failed_users = []

for log in logs:
    if "FAILED" in log:
        user = log.split("user=")[1]
        failed_users.append(user)

print("=== Security Log Analyzer ===")
print("Total logs:", len(logs))
print("Failed login attempts:", len(failed_users))

print("\nFailed attempts by user:")

counts = Counter(failed_users)

for user, count in counts.items():
    print(f"{user}: {count}")

print("\nSuspicious activity:")

for user, count in counts.items():
    if count >= 3:
        print(f"WARNING: {user} has {count} failed attempts!")