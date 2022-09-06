import test

string = "irawiT hsotiraP"
reversedString = ""

s = test.Stack()
for char in string:
    s.push(char)

while not s.is_empty():
    reversedString += s.pop()

print(reversedString)
