init python:
    def like():
        global liked
        liked = True
        renpy.jump("like")

    def dislike():
        renpy.jump("dislike")

screen comp_avatar_swype():
    default avatar_displayable = AvatarDisplayable(
     comp_profile.get_photo_filename(), 400, 400)
    add avatar_displayable

    imagebutton:
      auto "dislike_%s.png"
      action Function(dislike)
      yalign 0.5
      xalign 0.05

    imagebutton:
      auto "like_%s.png"
      action Function(like)
      yalign 0.5
      xalign 0.95

label dislike:
    # $ player_say = random.choice([u"Ужас", u"Так, следующий профиль.", u"Не, не мое это.", u"Листаем дальше."])
    # $ player(player_say)
    jump generate_profile

label swypes:
    scene bg
label generate_profile:
    python:
        global liked
        liked = False
    hide screen comp_avatar_swype
    $ comp_profile = Profile.generate(player_preference_gender,
     player_preference_age)
    $ comp_char = Character(comp_profile.get_name())

    show screen comp_avatar_swype
label choose_like_dislike:
    $ service(comp_profile.to_string())

    python:
        global liked
        if not liked:
            renpy.jump("choose_like_dislike")

label like:
    hide screen comp_avatar_swype
    $ player(u"Так, ну, вроде, выглядит прилично. Как раз то, что мне нужно.")

    jump swypes_end
