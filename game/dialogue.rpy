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
    # $ choises = db_dialogue[current_index]

    $ choice = renpy.display_menu(choises)

    python:
        for choice_data_iter in db_dialogue[current_index]:
            if choice_data_iter["text"] == choice:
                choce_data = choice_data_iter
                break

    $ answer_index = random.randrange(0, len(choce_data["answers"]), 1)
    $ fake += choce_data["answers"][answer_index]["fake"]
    $ comp_char(choce_data["answers"][answer_index]["text"])
    python:
        if "nextIndex" in choce_data["answers"][answer_index]:
            current_index = choce_data["answers"][answer_index]["nextIndex"]
        else:
            current_index += 1

    jump question

    jump dialogue_end
