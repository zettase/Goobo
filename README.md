# GOOBO BOT README

Welcome to the Goobo Bot documentation! Here's a quick guide to get you started on Windows.

## 1. Installing Dependencies

To install the necessary dependencies for Goobo Bot, use `pip`, the Python package installer. In your Command Prompt (cmd), execute:
```
pip install -r requirements.txt
```
This command installs all the packages listed in the `requirements.txt` file.

## 2. Setting up the Environment Variable

For the Goobo Bot to function properly, set an environment variable named `GOOBO_BOT_TOKEN` with your Discord bot token. Here's how:

In Command Prompt (cmd), enter:
```
setx GOOBO_BOT_TOKEN "Your_Discord_Bot_Token"
```
Replace `Your_Discord_Bot_Token` with your actual Discord bot token.

## 3. Running the Goobo Bot Script

Once you've set up the environment variable and installed the dependencies, run the Goobo Bot script by entering:
```
python goobo_bot.py
```
Ensure you're in the directory containing the `goobo_bot.py` script when you run the command.

**Enjoy using Goobo Bot!**
