screen comp_avatar_dialogue():
    default avatar_displayable = AvatarDisplayable(
     comp_profile.get_photo_filename(), 400, 400)
    add avatar_displayable


label dialogue:
    show screen comp_avatar_dialogue
    service "Начните диалог с собеседником"

    jump dialogue_end
