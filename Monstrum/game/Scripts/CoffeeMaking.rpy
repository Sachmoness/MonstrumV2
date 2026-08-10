# -------------------------------
# Backgrounds
# -------------------------------
image bg_coffeeStation = "images/Backgrounds/Coffee_Making/BG_Coffee Station.jpg"


# -------------------------------
# Props
# -------------------------------
image coffee_station_idle = "images/Props/Coffee_Making/Interactable/Coffee Machine_Idle.png"
image coffee_station_hover = "images/Props/Coffee_Making/Interactable/Coffee Machine_Hover.png"
image coffee_beans = "images/Props/Coffee_Making/Inventory/coffeeBeans.png"
image inventory_bar = "images/Props/Coffee_Making/Inventory/inventoryBar.png"
image inventory_Arrow_Idle = "images/Props/Coffee_Making/Inventory/inventoryArrow_Idle.png"
image inventory_Arrow_Hover = "images/Props/Coffee_Making/Inventory/inventoryArrow_Hover.png"
image jug = "images/Props/Coffee_Making/Inventory/Jug.png"
image monstrum = "images/Props/Coffee_Making/Inventory/Monstrum.png"
image mug_empty = "images/Props/Coffee_Making/Inventory/mugEmpty.png"
image mug_full = "images/Props/Coffee_Making/Inventory/mugFull.png"

# ------ Image Groups -------------
image inventoryBar_group:
    "inventory_bar"
    "coffee_beans" 
    "jug" 
    "mug_empty"

default inventory_bar_visible = False

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
    #add "inventory_bar"
    #add "inventory_Arrow_Idle"
    #add "coffee_beans"
    #add "jug"
    add "monstrum"
    #add "mug_empty"

    if inventory_bar_visible:
        add "inventory_bar" at truecenter
        add "coffee_beans" xalign 0.36 yalign 0.5
        add "jug" xalign 0.5 yalign 0.5
        add "mug_empty" xalign 0.64 yalign 0.5

    imagebutton:
        idle "inventory_Arrow_Idle"
        hover "inventory_Arrow_Hover"
        xpos 20
        ypos 20
        xanchor 0.0
        yanchor 0.0
        focus_mask True
        action ToggleVariable("inventory_bar_visible")

    imagebutton:
        idle "coffee_station_idle"
        hover "coffee_station_hover"
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        focus_mask True
        action [Hide("CoffeeMachine"), Show("CoffeeMachine", at_list=[truecenter])]

    

