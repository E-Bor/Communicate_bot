def categories_view(dictionary, category):
    dic = dictionary.copy()
    cat = category
    for i in cat:
        dic = dic[i]
    if isinstance(dic, str):
        return dic
    if isinstance(dic, dict):
        return list(dic.keys())


