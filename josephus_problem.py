import math
while True:
    try:
        no_of_soilders=int(input("Enter no of soilders:\n"))
        print("No of soilders:",no_of_soilders)
        l=no_of_soilders-math.pow(2,int(math.log(no_of_soilders,2)))
        winning_no=int(2*l+1)
        print(f"The person on {winning_no} position is alive!")
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)
# Sooo:
#     n=2^(a)+l
#     a is largest power of 2 which is less than n
#     now 2l+1=the position of last manm standing 