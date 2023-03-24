from pprint import pprint

name_list = [
    "rock",
    "gun",
    "lightning",
    "devil",
    "dragon",
    "water",
    "air",
    "paper",
    "sponge",
    "wolf",
    "tree",
    "human",
    "snake",
    "scissors",
    "fire",
]

half_list = len(name_list)//2
win = dict()
for name in name_list:
    
    win[name] = [name_list[name_list.index(name)-half_list:name_list.index(name)]]

print(name_list[-7])
print(name_list[name_list.index("gun")-half_list:name_list.index("gun")])


# pprint(win)