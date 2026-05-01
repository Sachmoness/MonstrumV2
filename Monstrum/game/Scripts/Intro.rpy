image flame_atl:
    "images/Props/Candles 1.png"
    pause 0.1
    "images/Props/Candles 2.png"
    pause 0.1
    repeat

image Book = "images/Props/Book/Book.png"



# -------------------------------
# Screens
# -------------------------------
screen name_input_screen():

    modal True

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)

        vbox:
            spacing 15
            xalign 0.5

            text "What is your name?" xalign 0.5

            input:
                value VariableInputValue("player_name")
                length 20
                xalign 0.5

            textbutton "Confirm":
                xalign 0.5
                action Return()

# -------------------------------

label intro:

    show flame_atl zorder 2 with dissolve

    "You attempt to sit up but realize you've been tied down to a table. The metal feels cold against your skin."

    scene bg_cafeDark with dissolve
    show flame_atl zorder 2 with dissolve
    show Cultists zorder 1 with dissolve

    Player "!!!"

    scene bg_cafeDark at scene_shake
    show flame_atl zorder 2
    show Cultists zorder 1

    pause 1

    show MF_Robed zorder 1 with dissolve

    pause 0.6

    menu:

        "Who are you?":
            jump choice1_passive

        "Where am I?":
            jump choice1_neutral

        "What the fuck!?":
            jump choice1_aggressive

label choice1_passive:

    $ menu_flag = True

    MF "You who heeded the call. Answer the questions or enter the void."

    jump choice1_done


label choice1_neutral:

    $ menu_flag = True

    MF "You who heeded the call. Answer the questions or enter the void."

    jump choice1_done


label choice1_aggressive:

    $ menu_flag = False

    MF "You who heeded the call. Answer the questions or enter the void."

    jump choice1_done

label choice1_done:

    Player "...What? What the hell is this! What do you freaks want from me?"

    MF "Do you heed the call?"

    show Book zorder 3 with dissolve

    "They hold up a large book with a blood red cover. The title, scrawled in black ink says 'Monstrum'."

    stop sound fadeout 3

    "You recognize the cover. It was the journal your mentor sent you before they vanished."

    "You begin to struggle."
    
    scene bg_cafeDark at scene_shake
    play sound sfx_Ominous
    show MF_Robed zorder 3
    show Cultists
    show flame_atl zorder 2 with dissolve

    Player "Give that back it's mine!"

    MF "Your personal belongings will be returned to the void should you not heed the call. Should you heed the call, they will be returned."

    Player "..."

    MF "Then we proceed."

    Player "..."

    MF "To heed the call, you must answer the following questions faithfully and honestly. Indicate your understanding of the prior statement."

    pause 0.6

    menu:

        "Stay Silent":
            jump choice2_passive

        "Fine...":
            jump choice2_neutral

        "Bite me.":
            jump choice2_aggressive
            

label choice2_passive:

    MF "Your compliance has been acknowledged."

    jump question_one


label choice2_neutral:

    MF "Your compliance has been acknowledged."

    jump question_one


label choice2_aggressive:

    MF "Your petulance has been acknowledged. We proceed."

    jump question_one


label question_one:

    MF "What is your name?"

    call screen name_input_screen

    $ player_name = player_name.strip().title() or "You"
    play sound sfx_memory

    MF "Question two."

    MF "How did you receive THE CALL?"