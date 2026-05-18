name = "wan"
print("What is your name?")
# name = input()
if name == "wan":
    print("Hello, Wan!")
elif name == "bob":
    print("Hello, Bob!")
else:
    print("Hello, Stranger!")

banana = 5
i = 0
while i < banana:
    print("Banana: {}".format(i))
    i += 2

    if i == 8:
        print("Banana is 8!")
        continue

    if i ==8:
        print("Banana is {}".format(i))
        break

lst =[]

for i in range (1, 101):
    lst.append(i)

print(lst)

lst3= []

lst3 = [i for i in range  (1, 101)]
print(lst3)

students = {
    "id01" : {"name": "Wan" , "age" : 25},
    "id02" : {"name": "Bob" , "age" : 30},
    "id03" : {"name": "Alice" , "age" : 28}
}
print(students)
print(students["id01"])
print(students["id01"]["name"])
