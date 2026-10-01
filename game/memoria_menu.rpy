################################################################################
# MEMORIA ZERO
################################################################################

image mz_bg = "gui/main_menu.jpg"
image mz_logo = "gui/logo.png"

transform logo_breath:

    zoom 1.0

    linear 4.0 zoom 1.02

    linear 4.0 zoom 1.0

    repeat


label splashscreen:

    scene black

    with Dissolve(1.5)

    pause 0.5

    show mz_logo at truecenter

    with Dissolve(2.0)

    pause 3.0

    hide mz_logo

    with Dissolve(1.5)

    return