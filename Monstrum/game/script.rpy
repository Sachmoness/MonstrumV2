# The script of the game goes in this file.
# The game starts here.

label start:

    play music music_intro_ambient loop volume 0.1

    play sound dia_intro_eyes_open
    "You open your eyes to darkness."

    stop sound fadeout 1
    play sound dia_intro_blindfolded
    "You've been blindfolded and can hear chanting voices resonating around you."

    stop sound fadeout 1

    jump intro

    # Game end.
    return
