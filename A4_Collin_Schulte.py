#function and while loop based menu to make a calculator to conver a variety of values
#set choice variables
FEET_TO_METERS = 1
METERS_TO_FEET = 2
CONVERT_TO_CELSIUS = 3
CONVERT_TO_FAHRENHEIT =4
QUIT = 0
#define program as a function
def main():
#intitalize choice
    choice = 7
#detect choice and loop menu
    while choice != QUIT:
        display_menu()
        choice = int(input("please select a number from the menu: "))
        if choice == FEET_TO_METERS:
            ft = int(input("please enter a distance in feet: "))
            print(ft,"feet is",F2M(ft), "meters")
        elif choice == METERS_TO_FEET:
            m = int(input("please enter a distance in meters"))
            print(m,"meters is",M2F(m), "feet")
        elif choice == CONVERT_TO_CELSIUS:
            f = float(input("please enter a temperature in fahrenheit: "))
            print(f,"degrees fahrenheit is",F2C(f), "degrees celsius")
        elif choice == CONVERT_TO_FAHRENHEIT:
            c = float(input("please enter a temperature in celsius: "))
            print(c,"degrees celsius is",C2F(c), "degrees fahrenheit")
        else:
            print("error make another choice")
#define display menu           
def display_menu():
    print("    menu")
    print("1. convert feet to meters")
    print("2. convert meters to feet")
    print("3. convert fahrenheit to celsius")
    print("4. convert celsius to fahrenheit")
    print("0. quit")
#define feet to meters function
def F2M(ft):
    return ft * 0.3048
#define meters to feet function
def M2F(m):
    return m * 3.2808399
#define fahrenheit to celsius function
def F2C(f):
    return(f-32) * 5/9
#define celsius to fahrenheit function
def C2F(c):
    return(c * 1.8) + 32
    


main()


