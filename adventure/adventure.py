from data import *

try:
    import readline
except ImportError:
    pass

###########
# Parsing #
###########

def adv_parse(line):
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No command given')
    command = tokens.pop(0)
    if command == 'go':
        if not tokens or tokens[0] != 'to':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
        return (command + '_to', ' '.join(tokens[1:]))
    elif command == 'check':
        if not tokens or tokens[0] != 'backpack':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS['check backpack']))
        return ('check_backpack', '')
    elif command == 'unlock':
        return ('unlock', ' '.join(tokens))
    elif command == 'keycode':
        if me.place == dining_room: # any(item.name == 'Lockbox' for item in me.backpack) or 
            return ('keycode', ' '.join(tokens))
        else:
            raise SyntaxError("Must be in the room with the lockbox to enter the code")
    elif command == 'meditate':
        if me.place != zendo:
            raise SyntaxError("You are not in the proper headspace to meditate")
        return ('meditate', '')
    else:
        return (command, ' '.join(tokens))

##############
# Evaluation #
##############

def adv_eval(exp):
    operator, operand = exp[0], exp[1]
    if operator not in COMMAND_NUM_ARGS:
        help()
        raise SyntaxError('Invalid command: {}'.format(operator))
    elif operator in SPECIAL_FORMS:
        function = SPECIAL_FORMS[operator]
    else:
        function = getattr(me, operator)

    if COMMAND_NUM_ARGS[operator] == 0:
        function()
    else:
        function(operand.title()) # type: ignore

def help():
    print('There are {} possible commands:'.format(len(COMMAND_FORMATS)))
    for usage in COMMAND_FORMATS.values():
        print('   ', usage)

########
# REPL #
########

def read_eval_print_loop():
    print(WELCOME_MESSAGE)
    if not isinstance(me, Player):
        print('Oh no! You need to create a player at the bottom of data.py to start the game.')
        return

    help()
    while True:
        if me.wonMoney and me.wonEstate:
            print("\nThank you for playing The Architect's Riddle.\n\n\n\n")
            return
        try:
            print()
            line = input('adventure> ')
            print("\n")
            exp = adv_parse(line)
            adv_eval(exp)
        except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
            print('\nGood game. Bye!')
            return
        # If the player input was badly formed or if something doesn't exist
        except SyntaxError as e:
            print('ERROR:', e)

#################
# Configuration #
#################

COMMAND_FORMATS = {
    'look': 'look',
    'go': 'go to [place]',
    'take': 'take [thing]',
    'check backpack': 'check backpack',
    'help': 'help',
    'unlock': 'unlock [place]',
    'keycode': 'keycode [code]',
    'meditate': 'meditate',
}

COMMAND_NUM_ARGS = {
    'look': 0,
    'go_to': 1,
    'take': 1,
    'check_backpack': 0,
    'help': 0,
    'unlock': 1,
    'keycode': 1,
    'meditate': 0,
}

SPECIAL_FORMS = {
    'help': help,
}

WELCOME_MESSAGE = """
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Welcome to The Architect's Riddle

------------------------------------------------------------------------------------------------------------------------

You were left with the following:


Dear Heir,

You will only be receiving this message after I have died.
You are the heir to my expansive estate and my fortune of $100 million.
However, before you can claim these you must unlock the two boxes sitting in front of you.
You might wonder why I have locked your inheritance behind a puzzle.
As an architect and buddhist I have always held the following two beliefs:
 - the world can be seen from many perspectives
 - everything should be done with intent and precision
I must ensure that whomever gains access to the wealth I have accumulated over my life will think the same.

Good luck,

Mrs. G
Renowned architect for the following projects: the Rising Fire house, the Entire Slate building, and the CisAmerica Pyramid

P.S. I will leave you with one hint. An architect\'s best friend is a piece of paper, specifically graph paper for precise drawings.

"""


if __name__ == '__main__':
    read_eval_print_loop()