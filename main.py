import os
import subprocess
from dotenv import load_dotenv

# Load .env
load_dotenv()

TOKEN = os.environ.get("GITHUB_TOKEN")
USER = os.environ.get("GITHUB_USER")
REPO = os.environ.get("GITHUB_REPO")

# Git remote URL
remote_url = f"https://{TOKEN}@github.com/{USER}/{REPO}.git"

# Git buyruqlari
commands = [
    "git init",
    "git branch -M main",
    f"git remote remove origin || true",
    f"git remote add origin {remote_url}",
    # Faqat kerakli fayllarni qo‘shish
    "git add Github_codes_dalate.py Tg_user_management.py pyproject.toml uv.lock",
    'git commit -m "Upload Telegram_bot files safely"',
    "git push -u origin main --force"
]

for cmd in commands:
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
