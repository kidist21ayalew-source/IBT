#Quation No 1
#city =["Addis Abbeba","Adama", 'Disse','Hawassa', "Addis Abbeba", "Disse"]

#print(set(city))


#Quation N2
#grocery ={"Onion": 100, "Potato":30, "Avocado": 150, "Mango":220, "Appel": 850}

#for item, price in grocery. items() :
 #   print(f"{item}:{price} ETB")


#Quation N3
#price = [100, 250, 400, 80]

#with_tax = [price +(price * 0.15) for price in price]
#print(with_tax)



#Quation No4
#prices =[100, 250, 400, 80]
#low_price =[price for price in prices if price < 200]
#print(low_price)


#Quation No5

with open("names.txt", "w") as file:
    file.write("Kidist\n")
    file.write("Ayalew\n")
    file.write("Hasset\n")
     
with open ("names.txt","r")as file:
    for line in file:
         print(line.strip())
    

      


# #quation No 3
# prices =[100, 250, 400, 80]
# with_tax =[(price + (price * 0.15)) for price in prices]
# print(with_tax)












 