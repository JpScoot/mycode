challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

#["goggles", "eyes"] counts as index 2 of challenge list, "eyes" is now index 1 of the new list 
a= challenge[2][1]
b= challenge[2][0]
c= challenge[3]

print(f"My {a}! The {b} do {c}!")

a=trial[2]["goggles"]
b=trial[2]["eyes"]
c=trial[3]
print(f"My {a}! The {b} do {c} ")




