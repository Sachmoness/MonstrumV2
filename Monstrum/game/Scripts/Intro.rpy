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

    jump question_two


label question_two:

    pause 0.6

    menu:

        "I was looking for my mentor...":
            jump question_three

        "That book... it showed up one day, and I opened it...":
            jump question_three

        "Online job bulletin post.":
            jump question_three


label question_three:

    MF "Your response has been noted."

    MF "Third question."

    MF "What is the difference between a Machiatto, a Capuccino, and a Latte?"

    pause 0.6

    menu:

        "Huh?":
            jump choice3_passive

        "Uh, milk I think...":
            jump choice3_neutral

        "A macchiato adds an additional splash of milk to a shot of espresso, a cappuccino is equal parts espresso, milk and milk foam, and a latte is mostly milk with espresso.":
            jump choice3_aggressive

            
label choice3_passive:

    MF "Incorrect answer. Correction to your answer: Each are representative of different ratios of milk to coffee."

    Player "Okay..."

    MF "Your answer is sufficient enough to deem you worthy. Though you will require additional training."

    Player "What?"

    hide flame_atl
    hide Cultists
    scene bg_cafeDark at scene_shake
    show Cultists_Turned
    show MF_Robed
    hide Book

    pause 0.6

    Player "!!!"

    jump choice3_done


label choice3_neutral:

    MF "Sufficient. Correction to your answer: Each are representative of different ratios of milk to coffee."

    Player "Okay..."

    MF "Your answer is sufficient enough to deem you worthy. Though you will require additional training."

    Player "What?"

    hide flame_atl
    hide Cultists
    scene bg_cafeDark at scene_shake
    show Cultists_Turned
    show MF_Unrobed
    hide Book

    pause 0.6

    Player "!!!"

    jump choice3_done


label choice3_aggressive:

    MF "..."

    Player "Did I get it right?"

    MF "Your answer is sufficient enough to deem you worthy. Though you will require additional training."

    Player "What?"

    hide flame_atl
    scene bg_cafeDark at scene_shake
    hide Cultists
    show Cultists_Turned
    show MF_Unrobed
    hide book

    pause 0.6

    Player "!!!"

    jump choice3_done



label choice3_done:

    scene bg_Cafe

    stop music fadeout 1.5

    show MF_Unrobed with dissolve

    MF "You're hired. The probation is two weeks. No overtime pay. Clock in is at 9am, Clock out is 5pm."

    MF "You have 30 minutes for your break time, but breaks can only be taken from 1pm-3pm. Questions?"

    Player "..."

    Player "What happened to the guys in robes?"

    MF "Their shift is over so I guess they went home."

    Player "..."

    MF "Here's your employee manual back. You'll find the ratios for orders inside and any other instructions you may need."

    MF "And if you have any other questions..."

    hide MF_Unrobed

    show MF_Disgust at shake_centered

    MF "Figure it out yourself. I'll be in the office."

    Player "Wait!"

    hide MF_Disgust

    show MF_Unrobed at shake_centered

    MF "..."

    Player "What's your name?"

    hide MF_Unrobed

    show MF_Turned

    MF "I find that unreasonably forward of you."


    menu:

        "...?":
            jump choice4_passive

        "Oh... sorry?":
            jump choice4_neutral

        "You find me asking your name.. too forward":
            jump choice4_aggressive


label choice4_passive:

    show MF_Unrobed

    MF "If you must refer to me by name, you may call me MANAGER."

    Player "Okay then... Manager, would you untie me?"

    $ mf_name = "MANAGER"

    MF "That is not my job."

    hide MF_Unrobed
    jump choice4_done


label choice4_neutral:

    show MF_Disgust

    MF "You should be. If you must refer to me by name, you may call me MANAGER."

    Player "Okay then... Manager, would you untie me?"

    $ mf_name = "MANAGER"

    MF "Ugh."

    hide MF_Disgust
    jump choice4_done


label choice4_aggressive:

    show MF_Turned_Shade

    MF "Yes. If you must refer to me, you may call me MANAGER."

    Player "Uh... I never accepted the job."

    $ mf_name = "MANAGER"

    MF "The fact that you are still alive means that you have accepted it, at least until your probation ends. Or you are dismissed."

    Player "Okay... then could you untie me?"

    hide MF_Turned_Shade
    jump choice4_done


label choice4_done:

    show MF_Disgust
    play sound dia_untieYou
    "They do agree to untie you, but they seem pissed off about it the entire time."

    Player "Thanks"

    hide MF_Disgust
    show MF_Turned

    MF "Start by cleaning the counter. I'll be in the office. Do not bother me unless it's an absolute emergency."

    Player "Oh sure."

    hide MF_Turned
    play sound dia_theyLeft
    "Oh...They left before you finished the sentence."

    "You pick up the Monstrum. They just threw it on the ground."
    
    "As you pick it up..."
    play sound dia_theBook
    "...the book begins to whisper to you."
    play sound sfx_memory
    "You recall now, this was the last thing your mentor gifted to you before they disappeared under mysterious circumstances."

    "You can interact with your surroundings."
    play sound dia_tryMirror
    "Try it by clicking the mirror."

    scene bg_Cafe

    call screen mirror_click