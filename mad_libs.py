# Write a Mad Lib program. Find a paragraph from a news article or a review (a short one) and paste it into your script into a variable. Change it to be an f-string and then choose a few words that you will let the user replace. For each of these words:

# Identify the type of word it is (noun, adverb, adjective, etc.) and create a variable to hold that submitted word. If you have more than one of one type, just append a number to the variable name.

# Replace the word in the string with that variable using the proper f-string syntax.

# Write an input prompt for eeach variable, asking the user for a word of that type.

# Print out the snippit with the chosen words filled in. Enjoy the hilarity!


# libs = [ input('noun >'), input('noun >'), input('noun >'), input('noun >'), input('noun >') input('noun >'), input('noun >'), input('adjective >'), input('adjective >'), input('adjective >'), ainput('verb >'), input('verb >'), input('verb >')]

print(f"""
Eric {input('noun >')}
ByEric RalphPosted on April 1, 2019
SpaceX CEO Elon Musk has proposed an {input('adjective >')} approach to conducting a {input('adjective >')} survey of the Solar System’s major outer {input('noun >')}, {input('noun >')}, and {input('noun >')}, requiring a stripped-down {input('noun >')} with a minimalist payload of Starlink satellites modified for interplanetary {input('noun >')} and {input('adjective >')} {input('noun >')}.

To {input('verb >')} this arrangement, it sounds like an {input('adjective >')} variant of {input('noun >')} would have to be {input('verb >')} and {input('verb >')}, cutting as much extraneous {input('noun >')} as possible to put as much energy as {input('adverb >')} possible into its payloads. Outer {input('noun >')} – those lying beyond the Solar System’s main {input('noun >')} belt – are a minimum of 400 million miles (~650 million km) from Earth and stretch out to bodies like 2014 MU69 at 4+ billion miles (6.8+ billion km) beyond {input('noun >')} orbit. To travel those truly absurd distances, the time-to-destination can often be measured in decades, a timeframe that is physically impossible to shrink without hugely powerful rockets like BFR. Even then, SpaceX would face major hurdles to pull off Musk’s impromptu mission design.
""")
