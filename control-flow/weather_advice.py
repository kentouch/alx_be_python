#
#
#
#
#### Pseudo code ####

# BEGIN

# INPUT: weather (Ask the user the weather)
# if weather is "sunny":
#       OUTPUT: "wear a t-shirt and sunglasses"
# elif weather is "rainy":
#       OUTPUT: "Don't forget your umbrella and a raincoat"
# elif weather is "cold":
#       OUTPUT: "Make sure to wear a warm coat and a scarf"
# else:
#       OUTPUT: "Sorry, I don't have recommendations for this weather."


# END


weather = input("What's the weather like today?(sunny/rainy/cold): ")

# check if weather inputed is 'sunny'
if weather.lower() == "sunny":
     print("Wear a t-shirt and sunglasses")

# check if weather inputed is rainny
elif weather.lower() == "rainy":
     print("Don't forget your umbrella and a raincoat.")
# check if weather inputed is cold
elif weather.lower() == "cold":
     print("Make sure to wear a warm coat and a scarf.")
 
else:
     print("Sorry, I don't have specific recommendations for this.")
