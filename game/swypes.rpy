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

            self.avatar.draw(width, height, st, at, renpy_render, 640, 360)

            renpy.redraw(self, 0)

            return renpy_render

        def event(self, ev, x, y, st):
            raise renpy.IgnoreEvent()

screen comp_avatar():
    default swype_displayable = SwypeDisplayable(comp_profile.get_photo_filename(), 200, 200)
    add swype_displayable

label swypes:
label generate_profile:
    $ comp_profile = Profile.generate(player_preference_gender,
     player_preference_age)
    $ comp_char = Character(comp_profile.get_name())

    # $ comp_avatar = Image(comp_profile.get_photo())
    # $ renpy.show(comp_profile.get_photo())
    # show comp_avatar:
    #     xzoom 0.5 yzoom 0.5
    show screen comp_avatar
    $ service(comp_profile.to_string())


    jump swypes_end
