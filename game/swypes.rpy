init python:
    class SwypeDisplayable(renpy.Displayable):
        def __init__(self, filename, width, height):
            renpy.Displayable.__init__(self)

            self.avatar = Sprite(filename, width, height)

            self.displayables_keeper = DisplayablesKeeper()

            self.displayables_keeper.add(
                self.avatar
            )

            self.oldtime = None

        def visit(self):
            return self.displayables_keeper.get_displayables()

        def render(self, width, height, st, at):
            renpy_render = renpy.Render(width, height)

            if self.oldtime is None:
                self.oldtime = st

            delta_time = st - self.oldtime
            self.oldtime = st

            self.avatar.draw(width, height, st, at, renpy_render, 640, 260)

            renpy.redraw(self, 0)

            return renpy_render

        def event(self, ev, x, y, st):
            raise renpy.IgnoreEvent()

    def like():
        global liked
        liked = True
        renpy.jump("like")

screen comp_avatar():
    default swype_displayable = SwypeDisplayable(
     comp_profile.get_photo_filename(), 400, 400)
    add swype_displayable

    imagebutton:
      auto "dislike_%s.png"
      action Jump("generate_profile")
      yalign 0.5
      xalign 0.05

    imagebutton:
      auto "like_%s.png"
      action Function(like)
      yalign 0.5
      xalign 0.95

label swypes:
    scene bg
label generate_profile:
    python:
        global liked
        liked = False
    hide screen comp_avatar
    $ comp_profile = Profile.generate(player_preference_gender,
     player_preference_age)
    $ comp_char = Character(comp_profile.get_name())

    # $ comp_avatar = Image(comp_profile.get_photo())
    # $ renpy.show(comp_profile.get_photo())
    # show comp_avatar:
    #     xzoom 0.5 yzoom 0.5
    show screen comp_avatar
label choose_like_dislike:
    $ service(comp_profile.to_string())

    python:
        global liked
        if not liked:
            renpy.jump("choose_like_dislike")

label like:
    service "Лайк"

    jump swypes_end
