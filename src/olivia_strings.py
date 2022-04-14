from itertools import cycle
from features import *

prefixes = ["Olivia ", "olivia ", "OLIVIA ", "Liv ", "LIV ", "liv "]
bot_key = 'olivia'
ping = "*flap flap* Squawk! :heart:"

# Activities
watching = cycle(
    ['Buttons moonbathe', 'the sea', 'the waves',
     'Karl balance on Buttons', 'the moon', 'out for enemies'])
playing = cycle(
    ['with someting shiny', 'cards with Buttons'])
listening = cycle(
    ['to the waves', 'pirate shanties', 'the song of revenge', 'Frenchie sing', 'Karl',
     'Stede and Ed \'flirt\''])

# Responsiveness

react_triggers = ["karl", "buttons", "moonbathe", "moon", "seagull", "seagulls", "the revenge", "mr. buttons", "caw caw", "squawk", "birds"]
reacts = ['🪶', '🐠', ' 🌊', '🦑', '🦀', '🐳', '⛵', '⚓', '🐚', '🐙']

responses = ['Caw! Caw!', '*flap flap*', 'SQWUAAACK!', "KEOH!", 'Keoh!', 'Squawk!', '🪶', '🍟?' '🎶', ' ✨ 🌕 ✨ ']

greetings_trigger = ["hiya olivia", "hiya, olivia", 'hello olivia', 'hello, olivia.',
                     'hello, olivia!', 'hello olivia', 'hello olivia.', 'hello olivia!',
                     'hey olivia', 'hey olivia.', 'hey olivia!', 'hey, olivia',
                     'hey, olivia.', 'hey, olivia!', 'hi, olivia', 'hi, olivia.',
                     'hi, olivia!', 'hi olivia', 'hi olivia.', 'hi olivia.']

what_trigger = ['what\'s up, olivia', 'whats up olivia',
                'what\'s the word, olivia', 'whats the word, olivia',
                'what\'s the word olivia', 'whats the word olivia',
                'what\'s up, olivia', 'what\'s up olivia', 'whats up, olivia',
                'whats up olivia',
                'what are you doing, olivia', 'what are you doing olivia',
                'what\'re you doing, olivia',
                'what\'re you doing olivia',
                'what\'s happening, olivia', 'whats happening olivia',
                'what\'s going on, olivia', 'what\'s going on olivia',
                'whatcha doin\', olivia', 'whatcha doin\' olivia',
                'whatcha all doin\', olivia', 'whatcha all doin\' olivia',
                "what are you up to, olivia", "what are you up to olivia",
                "what\'re you up to, olivia", "what\'re you up to olivia"]

how_trigger = ['how are you, olivia', 'how are you olivia', 'how\'re you, olivia',
               'how\'re you olivia', 'how are you doing, olivia',
               'how are you doing olivia', 'how\'re you doing, olivia',
               'how\'re you doing olivia', 'how\'re you doin, olivia',
               'how\'re you doin\' olivia',
               'how are you doin, olivia', 'how are you doin\' olivia',
               'how\'re you doin olivia',
               'how\'s it going, olivia', 'how\'s it going olivia',
               'hows it going, olivia', 'hows it going olivia',
               'how\'s your day going, olivia', 'how\'s your day going olivia',
               'hows your day going, olivia', 'hows your day going olivia',
               'how is your day going, olivia',
               'how is your day going olivia', 'how\'s it going olivia',
               'how\'re things going over there, olivia',
               'how\'re things going over there olivia',
               'how are things going over there, olivia',
               'how are things going over there olivia',
               'how is your day goin, olivia', 'how is your day goin olivia',
               'how\'re things goin over there, olivia',
               'how\'re things goin over there olivia',
               'how are things goin over there, olivia',
               'how are things goin over there olivia',
               'how is your day goin\', olivia', 'how is your day goin\' olivia',
               'how\'re things goin\' over there, olivia',
               'how\'re things goin\' over there olivia',
               'how are things goin\' over there, olivia',
               'how are things goin\' over there olivia', 'how you doin olivia',
               'how you doin, olivia', 'how you doing olivia', 'how you doing, olivia']

welcome_trigger = ['thanks, olivia', 'thanks, olivia.', 'thanks, olivia!', 'thanks olivia',
                   'thanks olivia.', 'thanks olivia!',
                   'thank you olivia', 'thank you olivia.', 'thank you olivia!',
                   'thank you, olivia', 'thank you, olivia.', 'thank you, olivia!']


sorry_trigger = ['sorry, olivia', 'sorry, olivia.', 'sorry olivia', 'sorry olivia.',
                 'my bad olivia', 'my bad olivia.',
                 'my bad, olivia', 'my bad, olivia.']

