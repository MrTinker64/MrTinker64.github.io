from classes import *

# Things:
remote_controller = Thing('RC', 'aka Remote Controller - A circuit board with some 3D printed handholds, two small joysticks, and a fat antenna. You wonder what is it for?')
flashlight = Thing('Flashlight', 'Pretty standard flashlight. Looks like there\'s a sensor so it will automatically turn on when dark.')
telescope_manual = Thing('Manual', 'Instruction manual for how to operate the telescope.')
snacks = Thing('Snacks', 'Animal crackers, but they are shaped like +, -, ÷, x.\n           - M&M\'s with little punctuation marks on each one.\n           - Cheez-its shaped like triangles, circles, hexagons, and all sorts of shapes in addition to squares.')
note = Thing('Note', 'A thank you note addressed to Mrs. G. Most of it is fluffy niceties, but you notice the guest talked at unusual length about layout of this estate. They must have been an architect as well.')

# Keys:
gear_key = Key('Gear Key', 'A gear-shaped item that looks like it might unlock something.')

# Places:
path = Outside_Place('Path','A straight and narrow gravel path leading into the woods with rays of sunlight streaming through the trees.\nYou make out two large circular buildings 30 feet away, one on each side of the path.', 'The tree tops, previously full of sunlight, are now dark and mysterious in the night.\nA straight and narrow gravel path, lined with lights, leads into the woods.\nYou make out two large circular buildings 30 feet away, one on each side of the path.', [])
observatory = Place('Observatory','A round room about 25 feet in diameter with a large telescope in the middle.\nOn the wall you see a chart with instructions for how to see various celestial bodies at night.', [flashlight, telescope_manual])
workshop = Place('Workshop','Another circular room 25 feet in diameter. The walls are lined with shelves full of part way finished projects and different tools.\nA remote controller is lying in the middle of a work table near you.', [remote_controller])

dining_room = Place('Dining Room','You stand in the middle of a long room full of ornate carvings.\nIt\'s about 30 feet wide, 15 in either direction, and is 10 ft across. There is a long dinner table taking up nearly the entire length of the room.\n\nTwo locked boxes sit on the table in front of you.\nOne with 💰 engraved on it and the other 🏠.\nBoth have 4 dials all set to 0.\n\nTo your right is the kitchen, the left is a bedroom, ahead is a beautiful lake, and behind you is a path into the woods.', [])
kitchen = Place('Kitchen','A clean, modern looking kitchen that is a 10x10 foot square with a door to your left. You check the cupboard and find some snacks.', [snacks])
pantry = Place('Pantry','The pantry is an isosceles right triangle with one short edge flush with the kitchen and the other on your left.\nThe shelves are full with dried and canned goods like flour, sugar, pickles, pears, etc. Amongst all the food you see a little glimmer of metal.', [gear_key])
guest_bedroom = Place('Guest Bedroom','A huge bedroom, similar in size to the dining room, with a queen bed, night table, dresser, and lounge chair. On the night table you see a piece of paper. The room goes 15ft in either direction and 10ft back with the dresser and lounge chair on one side and the bed with night stand on the other.', [note])

lake = Outside_Place('Lake','A path leads out about 10 feet to the center of an oval shaped lake laying perpendicular to you.\nHowever, lake might be a generous term as it is only 30 feet across and 50 feet wide.\nOn the far side of the lake is what looks like an artist\'s studio, also 50 feet wide.\nAs you walk along the path around the lake, you see something in the middle of the glittering lake.\nAs you squint against the glare, it looks like a little toy boat.', 'You walk into the cool night air onto a path that leads out about 10 feet to the center of an oval shaped lake laying perpendicular to you.\nHowever, lake might be a generous term as it is only 30 feet across and 50 feet wide.\nOn the far side of the lake is what looks like an artist\'s studio, also 50 feet wide.\nAs you walk along the path around the lake, you see something in the middle of the lake, glittering in the starlight.\nAs you squint against the moon\'s glare, it looks like a little toy boat.', [])
arch_studio = Place('Studio','Such a large space for architecture emphasizes the love Mrs. G had for it.\nStanding in the center of the long space you are overwhelmed by the volume of cutting mats, sketches, and miniature buildings.\nOne set of miniature buildings looks like the alphabet when viewed from above.\nThough the room is long, the back wall is only 10ft away making for a narrow space.\nYou can just make out another door. It\'s on the far right edge of the back wall, leading away from the lake.', [])
storage_closet = Place('Closet','A messy, dusty room full of shelves overflowing with pens, paper, foamcore, rulers, and old models.\nOne of the models looks vaguely like a number, but has been crushed out of shape. This room is also 10 ft wide.\nThe back wall is 20 ft away, to it\'s left you see a door which seems to be magically free of all the dust and clutter inhabiting the rest of the room.', [])
zendo = Place('Zendo','The room is spacious, forming a 20x20 ft square. The walls to your right and across from you have floor to ceiling windows.\nInside the room, to your left is a lowered 10x10 ft garden. Between the windows and the garden is a 2nd door leading back to the Studio.\nThe wooden floors are completely empty save for a small round cushion sitting on a mat in the corner formed by the widnows.\nIt feels very peaceful here.', [])

# Exits:
# eight
path.add_exits([observatory, dining_room, workshop])

# one
dining_room.add_exits([kitchen, lake, guest_bedroom])
pantry.add_exits([kitchen])

# zero
lake.add_exits([arch_studio])

# nine
zendo.add_oneway_exits([arch_studio])
storage_closet.add_exits([arch_studio, zendo])


# Locked places
workshop.locked = True

# Player:
me = Player('Heir',dining_room)