import os 


def greet(text):
    return f"Hello {text}!"

with open('train/name.txt', 'r') as f:
    names = f.read().splitlines()

for name in names:
    print(greet(name))