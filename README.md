# Discord Bot - Python

A simple Discord bot built with Python that can tell jokes and fetch real-time weather information.

---

## Features

* Custom `!help` command listing all available commands
* `!joke` command — sends a random French joke
* `!weather <city>` command — fetches live weather data for any city using OpenWeatherMap

---

## Technologies Used

* Python
* [discord.py](https://discordpy.readthedocs.io/)
* [requests](https://pypi.org/project/requests/)
* [OpenWeatherMap API](https://openweathermap.org/api)

---

## Prerequisites

### 1. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**, give it a name, then click **"Create"**
3. In the left sidebar, click on **"Bot"**
4. Click **"Add Bot"** then confirm with **"Yes, do it!"**
5. Under the bot's username, click **"Reset Token"** and copy your token — you'll need it later

> ⚠️ Never share your bot token. If it leaks, reset it immediately from the portal.

#### Enable Required Intents

Still on the **Bot** page, scroll down to **"Privileged Gateway Intents"** and enable the following:

| Intent | Required | Why |
|---|---|---|
| **Message Content Intent** | ✅ YES | Allows the bot to read message content and detect prefix commands like `!joke` |
| Server Members Intent | ❌ No | Not needed for this bot |
| Presence Intent | ❌ No | Not needed for this bot |

Click **"Save Changes"**.

#### Invite the Bot to Your Server

1. In the left sidebar, go to **"OAuth2"** → **"URL Generator"**
2. Under **Scopes**, check `bot`
3. Under **Bot Permissions**, check at minimum:
   * `Send Messages`
   * `Read Message History`
4. Copy the generated URL at the bottom and open it in your browser to invite the bot to your server

---

### 2. Get an OpenWeatherMap API Key

1. Go to [openweathermap.org](https://openweathermap.org/) and click **"Sign Up"**
2. Fill in the registration form and confirm your email
3. Once logged in, go to your profile → **"My API keys"**  
   (or go directly to [https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys))
4. A default key is automatically generated — copy it
5. Paste it in `bot.py` where it says `API_KEY`

> ⚠️ The free tier allows up to 1,000 API calls/day, which is more than enough for personal use.  
> ⚠️ New API keys can take up to **10 minutes** to become active after creation.

---

## Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/discord-bot.git
cd discord-bot
```

2. Install the required libraries
```bash
pip install discord.py requests
```

3. Set up your credentials

Open `bot.py` and replace the placeholder values:
```python
TOKEN = "Your_Discord_Bot_Token_Here"
API_KEY = "Your_OpenWeatherMap_API_Key_Here"
```

> 💡 For better security, consider using a `.env` file with the `python-dotenv` library instead of hardcoding credentials. Add `.env` to your `.gitignore` so it's never pushed to GitHub.

---

## Usage

Run the bot:
```bash
python bot.py
```

### Commands

| Command | Description |
|---|---|
| `!help` | Displays all available commands |
| `!joke` | Sends a random French joke |
| `!weather <city>` | Shows current temperature and weather for the given city |

**Example:**
```
!weather Paris
→ Paris : 12°C, ciel dégagé
```

---

## Author

Samy BOUSSAD
