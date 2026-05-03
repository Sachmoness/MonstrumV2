screen mirror_click():

    imagebutton:
        auto "images/Props/Mirror/overlay_mirror_%s.png"
        xpos -5
        ypos -10
        focus_mask True
        action Jump("mirror_scene")


label mirror_scene:


    hide screen mirror_click

    scene bg_Mirror with dissolve
    play sound dia_Stare
    "You stare into the mirror."

    show charImage with dissolve
    play sound dia_You
    "Yep, that's you."
    play sound dia_Looklike
    "That's what you look like."
    play sound dia_Haircut
    "You probably need a haircut..."

    pause 0.6


    menu:

        "I think I need a whole new face...":
            jump mirror_passive

        "That's one good looking amorphous blob.":
            jump mirror_neutral

        "Ugh. I hate looking at myself.":
            jump mirror_aggressive


label mirror_passive:
    
    play sound dia_Face
    "Your mentor always liked your face."
    play sound sfx_memory


    jump mirror_done


label mirror_neutral:

    "That's the spirit."

    "There's no sexier outfit than confidence."

    jump mirror_done


label mirror_aggressive:
    
    play sound dia_standStraight
    "It's not that bad. Just... I don't know... stand up straighter?"

    jump mirror_done


label mirror_done:

    Player "Whatever."

    "Alright it's time to start your shift. Let's go clean the counter."

    pause 0.5
