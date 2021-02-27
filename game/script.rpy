# Declare characters used by this game.
define service = Character(_("Сайт знакомств"), color="#c8ffc8")
define player = Character(_("Я"), color="#c8c8ff")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# screen select_hobby():
#     vbox:
#         for hobby in db_hobby:
#             textbutton hobby action Null

# The game starts here.
label start:

    # Start by playing some music.
    # play music "illurock.opus"

    scene bg lecturehall

    # $ profile = Profile.generate()
    # $ prof_char = Character(profile.get_name())
    # $ renpy.show(profile.get_photo())
    # $ prof_char(profile.to_string())

    player "Одиночество похоже на голод. Оно разъедает изнутри и требует \
           заполнить пустоту чем угодно, лишь бы не чувствовать эту тоску, \
           жажду и безысходность."

    player "У меня было множество попыток найти себе пару и все они были \
           неудачными. Кажется, я никогда не найду человека для себя."

    player "Пусть человеку свойственно ошибаться, но меня каждая ошибка \
           приводит в уныние."

    player "Этот сайт знакомств - моя последняя попытка построить отношения, \
           я не выдержу больше провалов."

    player "Говорят, в социальных сетях сейчас полным-полно фейков и нужно \
           быть осторожным, если зовешь кого-то на свидание."

    player "Я боюсь ошибиться снова."

    service "Сайт знакомств \"В совместной изоляции\" приветствует вас!"

    $ player_name = renpy.input(u"Пожалуйста, введите имя")
    $ player_name = player_name.strip() or u"Одиночка"

    service "Добро пожаловать, [player_name], заполните анкету!"

    # service "Выберите свой пол"

    menu:
        "Выберите свой пол"

        "Мужчина":
            $ player_gender = u"Муж"

        "Женщина":
            $ player_gender = u"Жен"

    service "Выберите свои интересы из списка"

    $ choice = renpy.display_menu(list_to_menuitems(db_hobby))
    # show screen select_hobby

    service "Выберите возрастную категорию партнера"

    service "Кого ищете?"

    service "Анкета заполнена, спасибо! Листайте анкеты, выбирайте \
            понравившегося человека и, если Вы тоже понравитесь ему, \
            переходите к диалогу!"

    service "Также Вы всегда можете подкорректировать свои запросы в окне \
            \"Фильтры\"."

    service "На этом все, удачи!"

    player "Ну-с, посмотрим."

    return
