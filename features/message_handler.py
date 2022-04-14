# == MESSAGE HANDLER ==
# These functions handle SENDING messages.

# noinspection PyPackageRequirements
import copy
import discord
import random


# Receives a message object and a reaction and instructs the bot to react to that message.
async def add_react(message, react):
    await message.add_reaction(react)


# Receives a message object and sends a response (after checking various parameters).
async def send_message(incoming_message, response, nsfw_content=False):
    if nsfw_content and not incoming_message.channel.is_nsfw():
        print("ERROR: NSFW content triggered in SFW channel.")
        return

    # If the response tags the user, format the tag.
    response = await check_for_user_sentinel(response, incoming_message.author.id)
    await incoming_message.channel.send(response)


# If the '@USER' sentinel is present, replace it with a tag.
async def check_for_user_sentinel(message, user):
    if "@USER" in message:
        user = "<@!" + str(user) + ">"
        return message.replace("@USER", user)
    return message


# Checks whether a given message is included in a list of trigger phrases.
def contains_phrase(message, list_of_phrases):
    for phrase in list_of_phrases:
        if phrase in message.content.lower():
            previous_char_index = message.content.find(phrase) - 1
            # If the phrase is enclosed in quotes, disregard.
            if previous_char_index >= 0 and (
                    message.content[previous_char_index] == '\"' or message.content[previous_char_index] == '\''):
                return False
            return True
    return False


# Replace a word in a message; returns False if this cannot be done.
def replace_name(message, original, new):
    temp_message = copy.copy(message).lower()
    starting_index = temp_message.find(original.lower())
    ending_index = starting_index + len(original)

    if starting_index == -1:
        return False
    else:
        return message[0:starting_index] + new + message[ending_index:]


# Make a word plural.
def pluralizer(integer, unit, plural):
    if integer == 1:
        return f"{integer} {unit}"
    else:
        return f"{integer} {unit}{plural}"
