# noinspection PyPackageRequirements
import os
import sys

import discord
import random

DEV_ID = int(open("id/dev_id.txt", "r").readline())
OLIVIA_TOKEN = open("./id/olivia_token.txt", "r").readline()
OLIVIA_ID = int(open("./id/olivia_id.txt", "r").readline())
KARL_ID = int(open("./id/karl_id.txt", "r").readline())
MAIN_GUILD_ID = int(open("./id/main_guild_id.txt", "r").readline())
ART_CHAT_ID = int(open("id/art_channel_id.txt", "r").readline())


# Reboots a given bot when prompted by an authorized user.
async def restart(ctx, bot='Olivia'):
    bot = bot.capitalize()
    if await authorize_user(ctx.message.author):
        print(f"{ctx.message.author} rebooted {bot}.")
        await ctx.send(f" :computer:  {bot} is rebooting.")
        os.execv(sys.executable, ['python3'] + sys.argv)
    else:
        await ctx.send(
            f" :computer:  Only admins can reboot {bot}!")


# Given a key, returns a bot token (string).
def token(key):
    if key == 'olivia':
        return OLIVIA_TOKEN
    else:
        return False


# Asked for a key, returns a commonly requested Discord ID (integer).
def entity(key):
    if key == 'dev':
        return DEV_ID
    elif key == 'olivia':
        return OLIVIA_ID
    elif key == 'karl':
        return KARL_ID
    elif key == 'dev':
        return DEV_ID
    elif key == 'main':
        return MAIN_GUILD_ID
    elif key == 'gallery':
        return ART_CHAT_ID
    else:
        return False


# Checks whether a message's author's ID is Olivia's ID.
def is_olivia(author_ID):
    if author_ID == OLIVIA_ID:
        return True
    return False


# Checks whether a message's author's ID is Karl's ID.
def is_karl(author_ID):
    if author_ID == KARL_ID:
        return True
    return False


# Authorizes a user as either the developer or an administrator.
async def authorize_user(user):
    if user.id == DEV_ID or user.guild_permissions.administrator:
        return True
    else:
        return False


# Returns a string list of all the bot's commands.
def get_commands(admin):
    command_list = f"==OLIVA BOT COMMANDS ==\n\n" \
                   f"Ping Oliva with `Olivia ping`\n" \
                   f"List commands with `Olivia commands`\n\n" \
                   f"Get a seagull picture with `Olivia insta`\n\n" \
                   f"Hear a seagull sound with `Olivia talk`\n\n" \
                   f"**Conversation Triggers**:\n" \
                   f"Hi / Hello / Hey Olivia.\n" \
                   f"Thanks / Thank you Olivia.\n" \
                   f"Sorry/ My bad Olivia. \n\n"

    unimplemented_features = f"Get a random OFMD screencap with `Olivia screencap`\n\n" \
                             f"Get a fanfic rec with `Olivia fic`\n\n" \
                             f"Get an art rec with `Olivia art`\n\n"

    admin_commands = f"\n\n**ADMIN Commands**:\n" \
                     f"Reboot bot with `Olivia reboot`\n"

    if admin:
        return command_list + admin_commands
    else:
        return command_list
