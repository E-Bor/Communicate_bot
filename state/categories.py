# def categories_view(dictionary, category):
#     dic = dictionary.copy()
#     cat = category
#     for i in cat:
#         dic = dic[i]
#     if isinstance(dic, str):
#         return dic
#     if isinstance(dic, dict):
#         return list(dic.keys())

def categories_view(category, path, first_dir=None):
    dic = category.copy()
    path = list(map(int, path))
    print(path)
    if not path:
        first_index = list(dic.keys()).index(first_dir)
        first_cat = list(category[first_dir].keys())
        return first_index, first_cat
    for i in path:
        j = list(dic.keys())[i]
        dic = dic[j]
    if isinstance(dic, str):
        return dic
    if isinstance(dic, dict):
        return list(dic.keys())
