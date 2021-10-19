
string = "string is reversed"

revers = ""
for step in range(len(string)-1,-1,-1):
    revers += string[step]
print(revers)



def stringreverRecurciver(array):
    if len(array) == 1:
        return array[0]
    return array[len(array)-1] + stringreverRecurciver(array[:len(array)-1])


hello = "hello world"
print(stringreverRecurciver(hello))
