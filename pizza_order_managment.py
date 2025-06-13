menu={
    'pizza':120,
    'pasta':320,
    'noodles':100,
    'burger':150,
    'coffee':110,
     }

print("Welcome To Our Cafe")
print("pizza: 120\npasta:320\noodles:100\nburger:150\ncoffee:110")
order_total=0
item_1=input("Please Enter Your Order= ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your {item_1} has been ordered")
else:
    print(f"ordered{item_1} is not avilable yet")
another_order=input("Do you want to ordered somthing else (Yes/No)")
if another_order=="yes":
    item_2=input("Enter Your second ordered")
    if item_2 in menu:
        order_total+=menu[item_2]
    else:
        print(f"ordered {item_2} is not avilable yet.please enter somthing diffrent")



print(f"thank you for ordering here is your beel {order_total}RS")    
#input=("Please Enter Your Order")
menu={
    'pizza':120,
    'pasta':320,
    'noodles':100,
    'burger':150,
    'coffee':110,
     }

print("Welcome To Our Cafe")
print("pizza: 120\npasta:320\noodles:100\nburger:150\ncoffee:110")
order_total=0
item_1=input("Please Enter Your Order= ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your {item_1} has been ordered")
else:
    print(f"ordered{item_1} is not avilable yet")
another_order=input("Do you want to ordered somthing else (Yes/No)")
if another_order=="yes":
    item_2=input("Enter Your second ordered")
    if item_2 in menu:
        order_total+=menu[item_2]
    else:
        print(f"ordered {item_2} is not avilable yet.please enter somthing diffrent")



print(f"thank you for ordering here is your beel {order_total}RS")    
#input=("Please Enter Your Order")
