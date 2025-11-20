import random
import datetime
import sys

# --- Commit chances (for 10–15 commits/day) ---
# Action runs 24 times/day (every hour)
# Commit probability tuned to ~45% chance per run
# if random.random() > 0.40:
#     print("Skipping this run — randomness.")
#     sys.exit(0)

# --- Large commit message list ---
COMMIT_MESSAGES = [
    "🌱 Growth update",
    "🔧 Small maintenance change",
    "✨ Auto polished data",
    "🌿 Routine plant cycle log",
    "📝 Daily stat bump",
    "📈 Log refresh",
    "🧪 Auto experiment log",
    "🌻 New growth pattern",
    "🌾 Updated vegetation data",
    "📌 Minor adjustments",
    "🍃 Background update",
    "🔄 Automated sync",
    "🌲 Forest cycle tweak",
    "🟩 Data regen",
    "🟦 Hourly log refresh",
    "🟪 Automated patch",
    "🟥 Auto commit pulse",
    "🌤️ Daily climate marker",
    "🔥 System heartbeat",
    "💧 Water cycle updated",
    "🌙 Night cycle patch",
    "⭐ Auto graph bump",
    "🌡️ Temp fluctuation note",
    "🌬️ Airflow update",
    "🍀 Model micro-update",
    "⚙️ Scheduled maintenance",
    "📊 Data reshuffle",
    "🚀 Automated update",
    "🔍 Micro tweak",
    "🧰 Minor fix",
    "♻️ Cycle refresh",
    "📜 Background log update",
    "🌼 Bloom cycle refreshed",
    "🧿 Regenerated pattern",
    "🔋 Activity tick",
    "🏷️ System auto-note",
    "✨ Small refinement",
    "🪴 Greenhouse log",
    "🌏 Daily rotation mark",
    "🕒 Hourly cycle mark",
    "📚 Data line added",
    "📘 Log increment",
    "🧠 Pattern check",
    "🔭 Micro observation log",
    "📡 Auto signal update",
    "🎯 Update triggered",
    "🎲 Randomized commit",
    "🧩 Auto patch piece",
    "🔐 Automated safe change",
    "📦 Routine update",
    "🌋 Cycle spike record",
]

selected_message = random.choice(COMMIT_MESSAGES)

# --- Generate log entry ---
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
random_number = random.randint(100000, 999999)

entry = f"{selected_message}\n"

# --- Write to log file ---
with open("activity_log.txt", "a") as f:
    f.write(entry)

print("Committed:", entry)
