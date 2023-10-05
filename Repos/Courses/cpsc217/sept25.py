
end_loop = False
while not end_loop:
    age = int(input("Enter you age: "))
    if age < 0:
        print("Age cannot be negative")
    else:
        end_loop = True
    
if age < 18:
        print("You're too young")
else:
        print("You're an adult")

