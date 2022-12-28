# more compact way of using list

A = [2,4,6]
B = [3,5,7]
cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)


#choose to show only those movies from a list that are released above year 2000
movies = [("The avaiator", 2004),("spirited way", 2001),("rear window", 1954)]

movies_released_after_2000 = [title for (title,year) in movies if year > 2000]
print(movies_released_after_2000)