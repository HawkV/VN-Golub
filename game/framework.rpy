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

        def to_string(self):
            return u"Пол: {gender}, Имя: {name}, Возраст: {age}\nИнтересы: {hobbies}\n".format(
                gender=self.gender,
                name=self.name,
                age=self.age,
                hobbies=", ".join(self.hobbies)
            )

        @staticmethod
        def generate():
            gender = random.choice([u"Муж", u"Жен"])
            age = random.randrange(AGE_MIN, AGE_MAX + 1, 1)
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

