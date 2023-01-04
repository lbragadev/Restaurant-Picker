#TODO

#set up requirements.txt

#add click dependency
    #import CLICK 
    #use click cli

# design restaurant class
# create restaurant objects
# implement pick restaurant method
# implement add restaurant method
# implement delete restaurant method


#TODO
#pick_cheap_restaurants
#pick_healthy_restaurants
#pick_special_occasion_restaurants

#pick_restaurant(cheap=True)
#pick_restaurant(cheap=True, healthy=True)
#


from restaurant import *


def pick_restaurant():
        #for each restaurant
            #
        print("PICKING RESTAURANT")

def main():
    # restaurant_list = get_restaurants()
    # print(f"restaurant_list:{restaurant_list}")
    print(pick_cheap_restaurant().name)
    print("END!")

if __name__ == "__main__":
    main()
