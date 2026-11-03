"""
no thanks! competion bot base
functions:
    print()
    - Used for if you wnat to put a message for your bot to say mid-turn (eg. for seeing its 'thinking' process)
    - Dont print more than 200 chars on one turn (any non-alfanumeric charecter counts for 100)
    - Dont print bad words/phrases
    play(takeCard: bool, message: str=None)
    - Done at the end of a turn if takeCard is true it will do the action of taking the current card 
    - If takeCard is false it will do the action of saying No thanks!, unless the bot has no chips to use 
    - message is an optional message you can put for your bot to 'say' when it runs this function, will print a generic message if not given
    - Don't put bad words/phrases in message

varibles:
    chipsInPot - gets the number of chips in the pot (int)
    currentCard - gets the current cards number (int)
    botCount - gets the current amount of players (int)
    botName - set a custom name for your bot also don't put bad words/phrases as your name (can be used multiple times, str)
    botChips - the amount of chips your bot currently has (int)
    botInventory - the current inventory of every card your bot has (list of ints)
"""

def run_turn():
    global play, chipsInPot, currentCard, botCount, botName, botChips, botInventory