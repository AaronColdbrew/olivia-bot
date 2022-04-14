# noinspection PyPackageRequirements
import discord
import random


# Given a context, returns the display_name of a random guild member.
def random_user(ctx):
    return random.choice([member.display_name for member in ctx.guild.members])


# Given a context and user's name or display name, searches for a guild member object.
def get_user(ctx, target):
    user = [member for member in ctx.guild.members if
            member.display_name.lower() == target or member.name.lower() == target]
    if len(user) > 0:
        return user.pop()
    else:
        return None












