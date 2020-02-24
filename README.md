# World of Tanks Garage Discord Bot

[![Build Status](https://travis-ci.org/chasinggreg/wot-garage-bot.svg?branch=master)](https://travis-ci.org/chasinggreg/wot-garage-bot) [![Issues](https://img.shields.io/github/issues/chasinggreg/wot-garage-bot.svg)](https://github.com/chasinggreg/wot-garage-bot/issues)

With this bot you're able to lookup your [World of Tanks](http://worldoftanks.com/) stats or the stats and clan of other players with a command within [Discord](https://discordapp.com/).

## Installation Steps :minidisc: 

1. Visit the [World of Tanks API website](https://developers.wargaming.net/applications/) and sign up for an API client id/secret.
2. Visit the [Discord API website and create an application](https://discordapp.com/developers/applications/). You'll need to create a bot user and retrieve the [bot token](https://discordapp.com/developers/docs/intro#bots-and-apps) it provides.
3. Invite the bot user to your server using the following URL by replacing the `YOUR_CLIENT_ID` portion with the one found within your [Discord API settings](https://discordapp.com/developers/applications/): `https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENT_ID_HERE&scope=bot&permissions=0`
4. Click the button below and enter the required fields to deploy the bot to [Heroku](http://heroku.com). If the required tokens were provided correctly the bot should appear online within Discord and begin responding to commands. 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/chasinggreg/wot-garage-bot/master)

---

If you'd like to run the application outside of [Heroku](http://heroku.com) you can add the required [configuration options](#configuration-file_folder) as environment variables and then run the following commands using [Python](https://www.python.org/) and [Pip](https://pypi.org/project/pip/).

```
# Install & Run
$ pip install -r requirements.txt
$ python app.py

# Tests
$ python tests.py
```

## Configuration :file_folder: 


## Commands :computer: 
The following commands are accepted by the bot.

```
# Command list/help
!garage help
```

## FAQ :speech_balloon: 
Here's a list of frequently asked questions. Please review the [contribution guide](https://github.com/chasinggreg/wot-garage-bot/blob/master/.github/CONTRIBUTING.md) if you'd like to support the project.
```
Q: Can I look up players stats in multiple Regions?
A: Yes, NA is the default region, however you can add region prefix before the player name to look up a player on another region server. (example: EU Kalfalgold)
```
