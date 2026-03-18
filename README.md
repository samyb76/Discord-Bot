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

> ⚠️ Never share your token or API key publicly. Consider using environment variables or a `.env` file to keep them secure.

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

## Configuration

To get your credentials:

* **Discord Bot Token** → [Discord Developer Portal](https://discord.com/developers/applications)
* **OpenWeatherMap API Key** → [openweathermap.org](https://openweathermap.org/api) (free tier available)

---

## Author

Samy BOUSSAD
