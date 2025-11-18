import random
import datetime
import sys

# Probability tuning for 8–15 commits/day
# (You can adjust 0.55 - 0.85 range if needed)
if random.random() > random.uniform(0.55, 0.85):
    print("Skipping this run ─ randomness check failed.")
    sys.exit(0)

# Random commit messages
COMMIT_MESSAGES = [
    "🌱 Updated growth logs",
    "🔧 Minor data tweak",
    "📝 Auto-update stats",
    "🌿 Log refresh",
    "✨ Routine maintenance",
    "📌 Randomized update",
    "🔄 Automated contribution",
    "🧪 Experiment log update",
    "📈 Stats bumped",
    "🌻 Auto-grow update",
    "🌲 Plant cycle refreshed"
]

selected_message = random.choice(COMMIT_MESSAGES)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
random_number = random.randint(1000, 9999)

content = f"{timestamp} | Rand: {random_number} | Msg: {selected_message}\n"

with open("activity_log.txt", "a") as f:
    f.write(content)

print("Update complete:", content)