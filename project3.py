## Project One

#def calculate_discount(price, discount_percent):
    #if discount_percent >= 20:
        #discounted_price = price * (1 - discount_percent / 100)
   # return discounted_price
#else:
    #return price
#print (calculate_discount(200, 15))

## Project Two
num_one=float(input("Enter price: ")) #num_one is price
num_two= float(input("Enter discount_percent: ")) #num_two is discount percent
if num_two>=20:
    result=num_one*(1-num_two/100)
    print("Enter result:", result)
else:
    print("The answer is:", num_one)