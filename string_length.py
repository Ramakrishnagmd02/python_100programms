
# we can pick two ways one is len function and manually check

name = "ramakrishna"

print(len(name))

start_value: int = 0
for i in name:
    start_value += 1
print(start_value)

def strlen(name):
    value: int = 0
    for i in name:
        value +=1
    return value
        
        
words = "ramakrishna"
print(strlen(words))

def strlen(words:str)->int:
    value: int = 0
    for i in name:
        value +=1
    return value

name = "ramakrishna"
print(strlen(name))