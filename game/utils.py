def list_to_menuitems(list):
    menuitems = []
    for item in list:
        menuitems.append((item, item))

    return menuitems
