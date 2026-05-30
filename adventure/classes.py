# A "simple" adventure game.

WIN_MESSAGE_MONEY = """
*******************************************************************

Congratulations! You have unlocked your inheritance of $100 million.

*******************************************************************


"""

WIN_MESSAGE_ESTATE = """
******************************************************************

Congratulations! You have unlocked your inheritance of the estate. 

******************************************************************


"""

class Player:
    def __init__(self, name, place):
        """Create a player object."""
        self.name = name
        self.place = place
        self.backpack = []
        self.wonMoney = False
        self.wonEstate = False
        self.night_time = False

    def look(self):
        in_word = "in"
        if self.place.name == "Lake":
            in_word = "at"
        if self.place.name == "Path":
            in_word = "on"
        print(f'You are currently {in_word} the ' + self.place.name, end=". ")
        if self.place.name == 'Closet':
            if not any(item.name == 'Flashlight' for item in self.backpack):
                print("The room is too dark to see in, the only light coming from the door to the Studio you just walked through.")
                return
            else:
                print("The room is too dark to see in and the only light bulb has broken.\n\nLuckily, you picked up the flashlight from earlier.\nYou turn on your flashlight and it illuminates:\n")
        else:
            print("You take a look around and see:")
        if isinstance(self.place, Outside_Place) and self.night_time:
            print(self.place.night_description)
        else:
            print(self.place.description)
        if self.place.name == 'Observatory':
            print()
            if self.night_time:
                print("Now that it is the early morning you are able to look through the telescope at the celestial objects listed on the wall.\nEventually you see an odd pattern emerging in the objects you're looking at.\nFirst there are a variety of thin or cigar-shaped galaxies reminding you of a 1.\nFurther down the list you see lots of double star clusters and binary stars which all look like an 8.")
            else:
                print("Unfortunately you can't use the telescope right now because it is daytime.")
        if self.place.name == 'Lake' and any(item.name == 'RC' for item in self.backpack):
            print()
            print("You use the remote controller to drive the toy boat over to you. Sitting inside is a notepad with some scribbled numbers.\nThough it has been partially damaged by the water you can make out part of the code --27.")
        print()
        self.place.look()

    def go_to(self, location):
        """Go to a location if it's among the exits of player's current place and it is unlocked."""
        if type(location) != str:
            print('Location has to be a string.')
            return
        destination = self.place.get_neighbor(location)
        if destination is not self.place:
            if destination.locked:
                print(destination.name + ' is locked! You need to unlock it first.')
            else:
                secret_door = self.place.name == "Zendo" and destination.name == "Studio"
                if secret_door:
                    print("You walk through a secret door...\n")
                self.place = destination
                self.look()
                if secret_door:
                    print("\n\nDid you notice you just came through a secret door?\n")


    def take(self, thing):
        """Take a thing if thing is at player's current place
        """
        if type(thing) != str:
            print('Thing should be a string.')
            return
        if thing == "Rc":
            thing = "RC"
        if thing in self.place.things:
            item = self.place.take(thing)
            self.backpack.append(item)
            print('You take the ' + item.name + '.')

        else:
            print(thing + ' is not here.')

    def check_backpack(self):
        """Print each item with its description and return a list of item names.
        """
        if not self.backpack:
            print('Your backpack is empty.')
        else:
            for item in self.backpack:
                print(item.name, '-', item.description)
            print("\nNot all items need to be used. Some will automatically change the room description and others are just for fun :)")


    def unlock(self, place):
        """If player has a key, unlock a locked neighboring place.
        """
        if type(place) != str:
            print("Place must be a string")
            return
        key = None
        for item in self.backpack:
            if isinstance(item, Key):
                key = item
                break
        if key is None:
            print("You don't have a key.")
            return
        if place not in self.place.exits:
            print("Can't find " + place + " nearby.")
            return
        destination = self.place.exits[place][0]
        if key.use(destination):
            self.backpack.remove(key)
        
    def keycode(self, code):
        if type(code) != str:
            print("Code must be a string")
            return
        if len(code) != 4:
            print("Code must be 4 digits")
            return
        if code == '1827':
            self.wonMoney = True
            print(WIN_MESSAGE_MONEY)
            if not self.wonEstate:
                print("Keep playing to get the estate.\n\n")
        elif code == '9018':
            self.wonEstate = True
            print(WIN_MESSAGE_ESTATE)
            if not self.wonMoney:
                print("Keep playing to get $100 million.\n\n")
        else:
            print("Unfortunately that is not the correct code")
            
    def meditate(self):
        self.night_time = True
        print("At first you sit uncomfortably on the cushion, unsure of what to do.\nAs you slow down and focus on your breathing the world starts to\n\nfade away\n\nYou open your eyes and notice it\'s now dark out. Through the window you see stars twinkling up above.")


class Thing:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, place):
        print("You can't use a {0} here".format(self.name))



class Key(Thing):
    def use(self, place):
        if place.locked:
            place.locked = False
            print("Unlocked " + place.name)
            return True
        else:
            print(place.name + " is already unlocked")
            return False



class Place:
    def __init__(self, name, description, things):
        self.name = name
        self.description = description
        self.things = {thing.name: thing for thing in things}
        self.locked = False
        self.exits = {}

    def look(self):
        print()
        print('Things:')
        if not self.things:
            print('nothing in particular')
        else:
            for thing in self.things.values():
                print('   ', thing.name, '-', thing.description)
        self.check_exits()

    def get_neighbor(self, exit):
        if type(exit) != str:
            print('Exit has to be a string.')
            return self
        elif exit in self.exits:
            exit_place = self.exits[exit][0]
            return exit_place
        else:
            print("Can't go to {} from {}.".format(exit, self.name))
            print("Try looking around to see where to go.")
            return self

    def take(self, thing):
        return self.things.pop(thing)

    def check_exits(self):
        print()
        print('You can go to:')
        for exit in self.exits:
            print('   ', exit)

    def add_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)
            place.exits[self.name] = (self, self.description)
            
    def add_oneway_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)
            
class Outside_Place(Place):
    def __init__(self, name, description, night_description, things):
        super().__init__(name, description, things)
        self.night_description = night_description