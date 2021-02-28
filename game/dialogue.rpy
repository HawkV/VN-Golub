init python:
    from db_dialogue import db_dialogue

#     def get_question_index_by_test(choise_data, question):
#         for

screen comp_avatar_dialogue():
    default avatar_displayable = AvatarDisplayable(
     comp_profile.get_photo_filename(), 400, 400)
    add avatar_displayable

label dialogue:
    $ fake = 0
    # show screen comp_avatar_dialogue
    service "Начните диалог с собеседником"

    $ current_index = 0
label question:
    python:
        choises = []
        for choise_data in db_dialogue[current_index]:
            choises.append((choise_data["text"], choise_data["text"]));
        choises.append((u"В чёрный список", u"В чёрный список"));

    $ choice = renpy.display_menu(choises)

    if choice == u"В чёрный список":
        jump swypes

    python:
        for choice_data_iter in db_dialogue[current_index]:
            if choice_data_iter["text"] == choice:
                choce_data = choice_data_iter
                break

    $ answer_index = random.randrange(0, len(choce_data["answers"]), 1)
    $ fake += choce_data["answers"][answer_index]["fake"]
    python:
        if "dating" in choce_data["answers"][answer_index]:
            dating = choce_data["answers"][answer_index]["dating"]
            renpy.jump("maybe_dating")
    $ comp_char(choce_data["answers"][answer_index]["text"])
    python:
        if "nextIndex" in choce_data["answers"][answer_index]:
            current_index = choce_data["answers"][answer_index]["nextIndex"]
        else:
            current_index += 1

    jump question

label maybe_dating:
    $ comp_char(choce_data["answers"][answer_index]["text"])
    if not dating:
        player "Ок, следующий"
        jump swypes

    python:
        if fake < 3:
            renpy.movie_cutscene("video/win.ogv")
        else:
            renpy.movie_cutscene("video/fake.ogv")

    jump dialogue_end
