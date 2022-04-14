# == FILE HANDLER ==
# These functions handle serving files.

# noinspection PyPackageRequirements
import os
import sys
from os import listdir
from os.path import isfile, join

import discord
import random

from discord.ext.commands import bot

emoji_set = ['🪶', '🐠', ' 🌊', '🦑', '🦀', '🐳', '⛵', '⚓', '🐚', '🐙']


# Given a path to an image directory, returns a random file from this directory in the form of
# a tuple: (path, name).
def serve_file(type='image'):
    path = "./src/"
    valid_formats = []
    if type == 'image':
        path = path + 'images/'
        valid_formats = ['.jpg', 'jpeg', '.png', 'webp', '.gif']
    elif type == 'sound':
        path = path + 'sounds/'
        valid_formats = ['.mp3', '.wav', '.mp4']

    files = [f for f in listdir(path) if isfile(join(path, f))]

    # Remove all files from the collection that are not in an appropriate format.
    for file in files:
        extension = file[-4:]
        if extension not in valid_formats:
            files.remove(file)

    file_name = random.choice(files)
    file_path = path + file_name

    return file_path, file_name


# Serves a sound.
async def sound(message):
    path, name = serve_file('sound')
    await message.channel.send(f"{random.choice(emoji_set)}  {random.choice(emoji_set)}  {random.choice(emoji_set)}",
                               file=discord.File(path, filename='seagull.mp3'))


# Plays a sound.
async def playSound(client, message):
    path, name = serve_file('sound')
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=message.guild)
    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio(path), after=None)


# Serves an image.
async def image(message):
    path, name = serve_file('image')
    await message.channel.send(f"{random.choice(emoji_set)}  {random.choice(emoji_set)}  {random.choice(emoji_set)}",
                               file=discord.File(path, filename=name))
