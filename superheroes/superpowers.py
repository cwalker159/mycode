#!/usr/bin/python3

import classinfo

# parts 1 and 2
name= classinfo["all"][2]["carl"]
power= classinfo["all"][2]["transformation"]

print(name, "has the power of", power)

# part 3
for x in classinfo["all"]:
    name= x["name"]
    skill= x["skill level"]
    power= x["super power"]
    animal= x["spirit animal"]

    # Mario, a <wondrous> <alpaca> of a programmer, possesses a <structure weakening> factor for moonlighting as a superhero!
    print(f"{name}, a {skill} {animal} of a programmer, possesses a {power} factor for moonlighting as a superhero!")
