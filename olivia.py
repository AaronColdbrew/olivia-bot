import discord.client
from discord.ext import commands, tasks

# Data
from features import *
from src import olivia_strings as strings

# Privileged Intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.messages = True

# Resources
bot_key = strings.bot_key

# Load client
client = commands.Bot(command_prefix=strings.prefixes, intents=intents)


# Wake up bot and set status
@client.event
async def on_ready():
    change_status.start()
    print(f'{bot_key.capitalize()} just woke up.')


# If there isn't a specific command for a given keyword, ignore it.
@client.event
async def on_command_error(ctx, error):
    print(f"{ctx.author.display_name} triggered {error}.")
    if isinstance(error, discord.ext.commands.CommandNotFound):
        return
    raise error


# Pings bot to confirm that it's online.
@client.command()
async def ping(ctx):
    await send_message(ctx.message, strings.ping)


# Reboots the bot - only can be done by administrator or developer.
@client.command()
async def reboot(ctx):
    await reboot(ctx, bot_key)


# Command to list all commands/bring up help menu.
@client.command()
async def commands(ctx):
    await send_message(ctx.message, get_commands(await authorize_user(ctx.message.author)))

# Bot posts a sound file.
@client.command()
async def talk(ctx):
    await sound(ctx.message)


# Bot posts an image file.
@client.command()
async def insta(ctx):
    await image(ctx.message)

# Loop that randomly selects a status for the bot.
@tasks.loop(minutes=15)
async def change_status():
    await get_random_activity(client, strings.watching, strings.playing, strings.listening)


# == MESSAGE HANDLING ==
@client.event
async def on_message(message):
    # Bot should not respond to itself.
    if message.author == client.user:
        return

    # Process links.
    if message.channel.id == entity('gallery') and is_karl(message.author.id):
        await repost_link(message)

    # Check to see if the message contains direct commands.
    await client.process_commands(message)

    # Bot reacts to messages.
    await reaction(message)

    # Bot responds to users.
    await respond_to_user(message)


# Bot reacts or responds to various triggers.
async def reaction(message):
    if contains_phrase(message, strings.react_triggers):
        await react(message, random.choice(strings.reacts))

    if message.author.display_name == "Karl The Seagull":
        await react(message, random.choice(['👀', '💗', '♥️', '😍', '💙']))


# Bot responds to user.
async def respond_to_user(message):
    # Check if message contains any trigger phrases.
    if contains_phrase(message, strings.greetings_trigger) or contains_phrase(message, strings.greetings_trigger) or \
            contains_phrase(message, strings.what_trigger) or contains_phrase(message, strings.how_trigger) or \
            contains_phrase(message, strings.welcome_trigger) or contains_phrase(message, strings.sorry_trigger):

        odds = random.randint(0, 10)
        if 0 <= odds <= 5:
            await send_message(message, random.choice(strings.responses))
        elif 6 <= odds <= 8:
            await image(message)
        else:
            await sound(message)


client.run(token(bot_key))
