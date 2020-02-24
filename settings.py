#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

"""Application settings such as API keys are stored here."""

# World of Tanks API Settings
WOT_APPLICATION_ID = str(os.environ.get("WOT_APPLICATION_ID"))
WOT_REGION = str(os.environ.get("WOT_REGION"))
LOCALE = str(os.environ.get("LOCALE"))

# Discord API Settings
DISCORD_BOT_TOKEN = str(os.environ.get("DISCORD_BOT_TOKEN"))

# API Connection Errors
NOT_FOUND_ERROR = "Could not find a character with that name. \
  Type `!garage help` for a list of valid commands. :hammer_pick:"
CONNECTION_ERROR = "There was an issue establishing a connection to the Wargaming API. \
  Please try again. :electric_plug:"
CREDENTIAL_ERROR = "There was an error generating the auth token. \
  Either the Blizzard auth API was not reachable or your Wargaming API credentials are not correct. :anger:"
UNKNOWN_ERROR = "An unknown error occurred while attempting to retrieve this character. \
  If this error continues to persist please create a bug report on Github: https://github.com/chasinggreg/wot-garage-bot/issues :hotsprings:"
