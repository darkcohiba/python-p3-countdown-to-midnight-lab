# def countdown(num):
#     '''counts down from number and prints "HAPPY NEW YEAR!"'''
#     for i in range(num, 0, -1):
#         print(f"{i} SECOND(S)!")
#     print("HAPPY NEW YEAR!")

def countdown(num):
    i = num
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
    print("HAPPY NEW YEAR!")

    


countdown(10)