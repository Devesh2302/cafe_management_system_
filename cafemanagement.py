Cafe={
    "pizza":200,
    "burger":60,
    "coffee":80,
    "hot chocolate":100,
    "sandwitch":60
}
pizza={
    "margeretta":100,
    "onion capsicum":150,
    "corn and onion":150,
    "farmhouse":300
    }

print("Welcome to our Cafe")
print("Menu:")
for item,price_items in Cafe.items():
   print(f"{item.title()}:{price_items}")
order_list=[]
total_bill=0

item1=input("Enter the item you want to add:").lower().strip()

if item1 =="pizza":
    print("select yoyr Pizza type:")
    for pizzatype, price_pizza in pizza.items():
       print(f"{pizzatype.title()}:{price_pizza}")
    pizza_type= input("pizza type:").lower().strip()
    if pizza_type in pizza:
       quantity=int(input(f"How many units of {item1} you want :"))
       order_total= pizza[pizza_type]* quantity
       total_bill += order_total
       order_list.append((pizza_type.title(),pizza[pizza_type],quantity,order_total))
       print(f"your order for {pizza_type.title()} has been added, and your total is {total_bill}")
    else:
       print("sorry this pizza is currently not available")
       exit()
else:
    quantity= int(input(f"how Many units of {item1} you want to add:"))
    order_total= Cafe[item1]*quantity
    total_bill+=order_total
    order_list.append((item1.title(),Cafe[item1],quantity,order_total))
    print(f"your oder",item1,"has been added. Your total is:",total_bill)



order2=input("Do you want any thing more to be added(yes/no):")    
if(order2=="No" or order2=="no"):
  print("Your order total=",order_total)

else:  
  print("Select your item:")
  for item, price_items in Cafe.items():
    print(f"{item.title()}:{price_items}")
  item2=input("Enter your second item:").lower().strip()

  if item2 =="pizza":
    print("select yoyr Pizza type:")
    for pizzatype, price_pizza in pizza.items():
       print(f"{pizzatype.title()}:{price_pizza}")
    pizza_type= input("pizza type:").lower().strip()

    if pizza_type in pizza:
       quantity= int(input(f"how Many units of {item2} you want to add:"))
       order_total= pizza[pizza_type]*quantity
       total_bill+=order_total
       # append is used to add items in the end of the list( it is a build in python list method)
       order_list.append((pizza_type.title(),pizza[pizza_type],quantity,order_total))
       print(f"your order for {pizza_type.title()} has been added")
       print(f"Your total bill is {total_bill}")
    else:
       print("sorry this pizza is currently not available")
       exit()
 
  else:
    quantity= int(input(f"how Many units of {item2} you want to add:"))
    order_total= Cafe[item2]*quantity
    total_bill+=order_total
    order_list.append((item2.title(),Cafe[item2],quantity,order_total))
    print(f"your oder",item2,"has been added.")
def bill():
   name= input("NAME:")
   P_no= int(input("Contact No:"))
   print("\n============Final Bill==============")
   print(f"Name:{name}")   
   print(f"P_no:{P_no}")
   print("{:<20} {:<10} {:<10} {:<10}".format("Item","pr","Qty","total"))
    #:<20 means left-align the text and take up 20 character spaces.
    #This prints the column headers: Item, Price, Qty, Total.
   print("-"*50)
   for name,pr,Qty,total in order_list:
    print(f"{name:<20} {pr:<10} {Qty:<10} {total}")
   print("-"*50)
   print(f"{'Total Bill:':<42} ₹{total_bill}")

bill()
print("Thank you." \
" Your order will be ready soon.")