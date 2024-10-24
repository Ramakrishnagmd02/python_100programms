

def number_index(name:str)->str:
    index_number = int(input("please enter nunber"))
    for i in range(len(name)):
        if i == index_number:
            return name[i]
 
name = "ramakrishna"
print(number_index(name))   



def number_find(name: str,index: int)->str:
    if 0<= index < len(name):
        return  name[index]      
name = "ramakrishna"
index = 4 
result = number_find(name,index)
print(type(result)) 

