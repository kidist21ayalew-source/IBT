
def split_bill(total,people,tip_rate=0.10):
    tip=total*tip_rate
    total_with_tip=total+tip
    per_person =total_with_tip/people
     
    return per_person
#variable
bill_total =1200
#list of  names
number_of_people =4

names =["kidist" ,"Hasset" ,"Dagem" ,"Abigyal"]

#call the function
share= split_bill(bill_total, number_of_people)
for name in names:
    print(name,"should pay" ,round (share,2),"ETB")