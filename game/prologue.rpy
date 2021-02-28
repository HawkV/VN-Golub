# Declare characters used by this game.
define player = Character(_("Я"), color="#c8c8ff")

init python:
    def set_player_hobby(hobby):
        global player_hobby
        player_hobby = hobby
        renpy.jump("hobby_chosen")

screen select_hobby():
    frame:
        xalign 0.5
        yalign 0.3

        hbox:
            vbox:
                for hobby in db_hobby[0:5]:
                    textbutton hobby action Function(set_player_hobby, hobby)
            vbox:
                for hobby in db_hobby[5:10]:
                    textbutton hobby action Function(set_player_hobby, hobby)
            vbox:
                for hobby in db_hobby[10:15]:
                    textbutton hobby action Function(set_player_hobby, hobby)

label prologue:
    scene bg alone

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

    scene bg default
    service "Сайт знакомств \"В совместной изоляции\" приветствует вас!"

    $ player_name = renpy.input(u"Пожалуйста, введите имя")
    $ player_name = player_name.strip() or u"Одиночка"

    service "Добро пожаловать, [player_name], заполните анкету!"

    menu:
        "Выберите свой пол"

        "Мужчина":
            $ player_gender = u"Муж"

        "Женщина":
            $ player_gender = u"Жен"

    python:
        global player_hobby
        player_hobby = None
label choose_hobby:
    show screen select_hobby
    service "Выберите свои интересы из списка"

    python:
        global player_hobby
        if player_hobby is None:
            renpy.jump("choose_hobby")
label hobby_chosen:
    hide screen select_hobby

    menu:
        "Выберите возрастную категорию партнера"

        "Юные и неопытные":
            $ player_preference_age = "young"

        "Опытные и зрелые":
            $ player_preference_age = "mature"

    menu:
        "Кого ищете?"

        "Мужчину":
            $ player_preference_gender = u"Муж"

        "Женщину":
            $ player_preference_gender = u"Жен"

        "Не важно":
            $ player_preference_gender = "both"

    service "Анкета заполнена, спасибо! Листайте анкеты, выбирайте \
            понравившегося человека и, если Вы тоже понравитесь ему, \
            переходите к диалогу!"

    service "Также Вы всегда можете подкорректировать свои запросы в окне \
            \"Фильтры\"."

    service "На этом все, удачи!"

    $ player_profile = Profile("player", player_name, 18, [player_hobby], None)
    $ player = Character(player_profile.get_name())

    player "Ну-с, посмотрим."

    jump prologue_end
