sampletuple1 = (20,10,30)
# Tuple with single element should end with comma else it is treated as string
sampletuple2 = ("aa")
sampletuple3 = ("aa","bb","cc","xyz@gmail.com")
sampletuple4 = ("aa",)

print (sampletuple1)
print (sampletuple2)
print (sampletuple3)
print(sampletuple4)

# info : Tuples are better to be used when you want to have better memory space as compared to list. 
#Tuples cannot be modified like list - Best use of Tuples are when you are creating config files and you do not want anyone to modify it.
#URLs, enpoints etc are best used as Tuples