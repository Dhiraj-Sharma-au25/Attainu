print("welcome to calculation world!")
def calculator_project():

    num_1 = int(input("Enter first number"))
    num_2 = int(input("Enter second number"))
    oprator  = input("you can choose only +,-,*,/")

    if oprator == "+":
        result = num_1 + num_2
    elif oprator == "-":
        result = num_1 - num_2
    elif oprator == "*":
        result = num_1 * num_2
    elif oprator == "/":
        result = num_1 / num_2
    else:
        print("wrong value!!!")
    print(result)



cnt = "y"
while cnt == "y" :
    res = calculator_project()
    print(res)
    cnt = input("for next calculation!!! press'y':")
    print(cnt)

