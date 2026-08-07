# -------------------------------
# Backgrounds
# -------------------------------
image bg_coffeeStation = "images/Backgrounds/Coffee_Making/BG_Coffee Station.jpg"


# -------------------------------
# Props
# -------------------------------
image coffee_station_idle = "images/Props/Coffee_Making/Interactable/Coffee Machine_Idle.png"
image coffee_station_hover = "images/Props/Coffee_Making/Interactable/Coffee Machine_Hover.png"

image CoffeeMachine:
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_1.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_2.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_3.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_4.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_5.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_6.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_7.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_8.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_9.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_10.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_11.png"
    pause 0.1
    "images/Props/Coffee_Making/Coffee Pour/Coffee_Station_12.png"


# --------------------------------
label CoffeMaking_Tutorial:
    call screen CoffeeMakingScreen

    return


# --------- Screen ----------------------
screen CoffeeMakingScreen():
    add "bg_coffeeStation"

    imagebutton:
        idle "coffee_station_idle"
        hover "coffee_station_hover"
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        focus_mask True
        action [Hide("CoffeeMachine"), Show("CoffeeMachine", at_list=[truecenter])]

