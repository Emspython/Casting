# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1 
# 1 Create a variable leek_price with an integer value of 2.
# 2 Cast this into a string and use the +-operator to print a string like this one, only with the correct price in it:

leek_price = 2
Leek_string = f'Leek is {leek_price} euro per kilo.'
print (Leek_string)

# Part 2 
# 1 We got an order for four leeks! Store the string 'leek 4' in a variable.
# 2 Use find and slicing to extract the number from this string.
# 3 Cast it into an integer.
# 4 Use this and leek_price to compute the sum total and store it in sum_total. Print out the value for this variable.

Order_leek = 'leek 4'
Leek_amount = Order_leek[Order_leek.find(' ')+1:]
Total_order = int(Leek_amount)
Total_amount = Total_order * leek_price
print(Total_amount)

#Part 3
# 1 Create one variable for the broccoli price and one for the order.
# 2 Compute the total price for this order.
# 3 Use the +-operator to assemble and print a string that looks like the following:

Broccoli_price = 2.34
Broccoli_order = 1.6
Total_price_broccoli = 2.34*1.6

print(str(Broccoli_order)+'kg broccoli costs ' + str(round(Total_price_broccoli,2))+'e')
