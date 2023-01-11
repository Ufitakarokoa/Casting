# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

#part-1 
leek_price = 2
print ("Leek is " + str(leek_price) + " euro per kilo.")
#part-2
leek_order='Leek 4'
leek_find= leek_order.find(" ")
leek_slice= leek_order[leek_find +1:]
leek_slice_cast=int(leek_slice)
sum_total=leek_price * leek_slice_cast
print(sum_total)
#part-3
Broccoli_cost_kg=2.34
broccoli_order_kg=1.6
total_price_order= Broccoli_cost_kg * broccoli_order_kg
total_price_rounded=round(total_price_order,2)
print((str(broccoli_order_kg)) + "kg broccoli costs " + (str(total_price_rounded)+"e"))
