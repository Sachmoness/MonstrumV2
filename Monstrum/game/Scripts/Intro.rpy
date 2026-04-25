image flame_atl:
    "images/Props/Candles 1.png"
    pause 0.1
    "images/Props/Candles 2.png"
    pause 0.1
    repeat


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

    show MF Robed zorder 1 with dissolve

    pause 0.6