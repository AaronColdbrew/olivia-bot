from features import contains_phrase, send_message


async def repost_link(message):
    url = message.embeds[0].to_dict()['fields'][2]['value']
    await send_message(message, url)