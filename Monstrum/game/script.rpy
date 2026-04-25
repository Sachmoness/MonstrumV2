# The script of the game goes in this file.
# The game starts here.

label start:

    play music music_intro_ambient loop volume 0.1

    play sound dia_intro_eyes_open
    "You open your eyes to darkness."

    play sound dia_intro_blindfolded
    "You've been blindfolded and can hear chanting voices resonating around you."

    #Add flame animation here
    "You attempt to sit up but realize you've been tied down to a table. The metal feels cold against your skin."

    jump intro

    # Game end.
    return
