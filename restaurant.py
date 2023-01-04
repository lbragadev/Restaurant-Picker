from enum import Enum
from typing import List
from random import *

class Price(Enum):
    cheap = 1
    moderate = 2
    expensive = 3

class Speed(Enum):
    slow = 1
    moderate = 2
    fast = 3

class Ambiance(Enum):
    simple = 1
    moderate = 2
    fancy = 3

class Nutrition(Enum):
    healthy = 1
    moderate = 2
    unhealthy = 3

class Ethnicity(Enum):
    filipino = "filipino"
    mexican = "mexican"
    italian = "italian"
    american = "american"
    thai = "thai"
    korean = "korean"
    japanese = "japanese"
    chinese = "chinese"
    vietnamese = "vietnamese"
    mediterranean = "mediterranean"


class Restaurant:
    """A Class to represent a restaurant.
    ...

    Attributes
    ----------
    name : str
        name of the restaurant
    address : str
        address of the restaurant
    price : Price
        price range of a meal
    speed : Speed
        speed of experience
    ambiance : Ambiance
        interior experience, decoration, vibe of the place
    nutrition : Nutrition
        nutritional rating of a meal here on average
    ethnicity : Ethnicity
        ethnic origin of a meal here

    Methods
    -------
    get_details():
        Prints all the restaurant's attributes.
    """

    def __init__(self, name, address, price, speed, ambiance, nutrition, ethnicity):
        self.name = name #name
        self.address = address # address
        self.price = price #cheap, moderate, expensive
        self.speed = speed  #slow, moderate, fast
        self.ambiance = ambiance #simple, casual, fancy
        self.nutrition = nutrition #true, false
        self.ethnicity = ethnicity #ethnic
    def get_details(self):
        string = ("\n\nname: {}, address: {}, price: {}, speed: {}, ambiance: {}, nutrition: {}, ethnicity: {}\n\n"\
        .format(self.name, self.address, self.price, self.speed, self.ambiance, self.nutrition, self.ethnicity))
        return string

restaurant_list = []

def create_restaurants():
    """Creates a list of restaurant objects and appends it to the restaurant_list object above.
    Args: None
    Returns: None
    """
    restaurants = [

        #Fast and simple
        ("Jollibee", "test address", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.unhealthy, Ethnicity.filipino),
        ("In-n-Out", "test address", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.unhealthy, Ethnicity.american),
        ("Mitsuwa", "test address", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.healthy, Ethnicity.japanese),
        ("Taqueria Hoy", "test address", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.mexican),
        ("Taqueria Ayutla Oaxaca", "test address", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.mexican),
        ("Grill City", "test address", Price.cheap, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.filipino),
        ("Kebab Shop", "test address", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.healthy, Ethnicity.mediterranean),
        ("Pom and Olive", "test address", Price.cheap, Speed.moderate, Ambiance.simple, Nutrition.healthy, Ethnicity.mediterranean),
        ("Brodard", "test address", Price.cheap, Speed.fast, Ambiance.moderate, Nutrition.healthy, Ethnicity.vietnamese),
        ("Yuk daejang", "test address", Price.cheap, Speed.moderate, Ambiance.moderate, Nutrition.moderate, Ethnicity.korean),

        #Casual
        ("Gerry's Grille", "test address", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.filipino),
        ("Tender greens", "test address", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.healthy, Ethnicity.american),
        ("Coco Ichibanya", "test address", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.japanese),
        ("A&J", "test address", Price.moderate, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.chinese),
        ("Taco Stand", "test address", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.mexican),
        ("Siam Station", "test address", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.thai),
        ("Tang 190", "test address", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.korean),
        ("Hop Doddy", "test address", Price.moderate, Speed.slow, Ambiance. moderate, Nutrition.moderate, Ethnicity.american),
        ("Etcetera", "test address", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.japanese),
        ("Nana San", "test address", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.japanese),
        ("Northern Cafe", "test address", Price.moderate, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.chinese),

        #Sitdown
        ("Gurume Sushi", "test address", Price.expensive, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.japanese),
        ("Cucina Enoteca", "test address", Price.expensive, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.italian),
        ("Yard House", "test address", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.american),
        ("Houstons", "test address", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.american),
        ("North Italia", "test address", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.italian),
        ("Urth Caffe", "test address", Price.expensive, Speed.slow, Ambiance.simple, Nutrition.healthy, Ethnicity.american),
        ("Ini Restorante", "test address", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.italian),

        #Special Occasion
        ("Baekjeong", "test address", Price.expensive, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.korean),
        ("Capital Grille", "test address", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.american),
        ("Mastros", "test address", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.american),

    ]
    for i in restaurants:
        restaurant_list.append(Restaurant(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

create_restaurants()

def get_restaurants() -> list[Restaurant]:
    return restaurant_list

#TODO
#pick_cheap_restaurants
#pick_healthy_restaurants
#pick_special_occasion_restaurants

#pick_restaurant(cheap=True)
#pick_restaurant(cheap=True, healthy=True)
#