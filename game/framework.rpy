init python:
    import random

    from db_names_male   import db_names_male
    from db_names_female import db_names_female
    from db_hobby        import db_hobby
    from utils           import list_to_menuitems

    HOBBIES_MIN     = 3
    HOBBIES_MAX     = 3
    AGE_MIN         = 18
    AGE_MATURE      = 35
    AGE_MAX         = 55
    PHOTOS_COUNT_MY = 49
    PHOTOS_COUNT_MM = 22
    PHOTOS_COUNT_FY = 64
    PHOTOS_COUNT_FM = 16
    PHOTOS_PREFIX_MY = "my"
    PHOTOS_PREFIX_MM = "mm"
    PHOTOS_PREFIX_FY = "fy"
    PHOTOS_PREFIX_FM = "fm"
    PHOTO_WIDTH = 512
    PHOTO_HEIGHT = 512

    class Profile():
        def __init__(self, gender, name, age, hobbies, photo):
            self.gender = gender
            self.name = name
            self.hobbies = hobbies
            self.age = age
            self.photo = photo

        def get_name(self):
            return self.name

        def get_photo(self):
            return self.photo

        def get_photo_filename(self):
            return "{wo_ext}.jpg".format(wo_ext=self.photo)

        def to_string(self):
            return u"Пол: {gender}, Имя: {name}, Возраст: {age}\nИнтересы: {hobbies}\n".format(
                gender=self.gender,
                name=self.name,
                age=self.age,
                hobbies=", ".join(self.hobbies)
            )

        @staticmethod
        def generate(pref_gender, pref_age):
            if pref_gender == "both":
                gender = random.choice([u"Муж", u"Жен"])
            else:
                gender = pref_gender

            if pref_age == "young":
                age = random.randrange(AGE_MIN, AGE_MATURE, 1)
            else:
                age = random.randrange(AGE_MATURE, AGE_MAX + 1, 1)
            if (gender == u"Муж"):
                name = random.choice(db_names_male)
                if (age < AGE_MATURE):
                    photo_prefix = PHOTOS_PREFIX_MY
                    photo_num = random.randrange(1, PHOTOS_COUNT_MY + 1, 1)
                else:
                    photo_prefix = PHOTOS_PREFIX_MM
                    photo_num = random.randrange(1, PHOTOS_COUNT_MM + 1, 1)
            else:
                name = random.choice(db_names_female)
                if (age < AGE_MATURE):
                    photo_prefix = PHOTOS_PREFIX_FY
                    photo_num = random.randrange(1, PHOTOS_COUNT_FY + 1, 1)
                else:
                    photo_prefix = PHOTOS_PREFIX_FM
                    photo_num = random.randrange(1, PHOTOS_COUNT_FM + 1, 1)

            photo = "{photo_prefix}{photo_num}".format(
             photo_prefix=photo_prefix, photo_num=photo_num)

            hobbies = []
            for i in range(random.randrange(HOBBIES_MIN, HOBBIES_MAX + 1, 1)):
                hobbies.append(random.choice(db_hobby))

            return Profile(gender, name, age, hobbies, photo)

    class Displayable():
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.anchor_x = width / 2
            self.anchor_y = height / 2

        def get_displayable(self):
            return self.displayable

        def draw(self, width, height, st, at, renpy_render, x, y):
            render_object = renpy.render(self.displayable, width, height, st,
             at)
            pos = (
                int(x - self.anchor_x),
                int(y - self.anchor_y)
            )
            renpy_render.blit(render_object, pos)

    class Primitive(Displayable):
        def __init__(self, color, width, height):
            super(Primitive, self).__init__(width, height)
            red = color & 0xFF0000 >> 16
            green = color & 0x00FF00 >> 8
            blue = color & 0x0000FF
            renpy_color = "#{red:02X}{green:02X}{blue:02X}".format(red=red,
             green=green, blue=blue)
            self.displayable = Solid(renpy_color, xsize=width, ysize=height)

    class Sprite(Displayable):
        def __init__(self, filename, width, height):
            super(Sprite, self).__init__(width, height)
            self.displayable = im.Scale(filename, width, height)

    class DisplayablesKeeper():
        def __init__(self):
            self.displayables = []

        def add(self, *displayables):
            for displayable in displayables:
                self.displayables.append(displayable.get_displayable())

        def get_displayables(self):
            return self.displayables

