# Honkbot
Honkbot is a simple Discord bot for sending gifs in chat.
It also tracks whether a user owes another game.

Honkbot is written with [interactions.py](https://discord-py-slash-command.readthedocs.io/en/latest/), a Python Discord API.

### Python Setup
This project requires Python >=3.10.
1. Build virtual env: `python -m venv venv`
2. Activate: `venv\scripts\activate`
3. Install requirements.txt: `pip install -r requirements.txt`
4. In `venv\scripts\`, add env variable "API_TOKEN" to `activate.bat` and `Activate.ps1`

### Docker setup:
1. From project directory: `docker build -t honk:[version]`
2. `docker run -d --name honk honk:[version]`, where "--name" is the container name, followed by the image.
