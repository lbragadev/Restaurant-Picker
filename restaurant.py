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
    cuban = "cuban"
    peruvian = "peruvian"
    hawaiian = "hawaiian"


class Restaurant:
    """A Class to represent a restaurant.
    ...

    Attributes
    ----------
    name : str
        name of the restaurant
    description : str
        description of the restaurant
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

    def __init__(self, name, description, price, speed, ambiance, nutrition, ethnicity):
        self.name = name #name
        self.description = description # description
        self.price = price #cheap, moderate, expensive
        self.speed = speed  #slow, moderate, fast
        self.ambiance = ambiance #simple, casual, fancy
        self.nutrition = nutrition #true, false
        self.ethnicity = ethnicity #ethnic
    def get_details(self):
        string = ("\nname: {}, description: {}, price: {}, speed: {}, ambiance: {}, nutrition: {}, ethnicity: {}\n"\
        .format(self.name, self.description, self.price, self.speed, self.ambiance, self.nutrition, self.ethnicity))
        return string

restaurant_list = []

def create_restaurants():
    """Creates a list of restaurant objects and appends it to the restaurant_list object above.
    Args: None
    Returns: None
    """
    restaurants = [

        #Fast and simple
        ("Jollibee", "chicken joy? say less", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.unhealthy, Ethnicity.filipino),
        ("In-n-Out", "Fast, cheap, always delicious burger.", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.unhealthy, Ethnicity.american),
        ("Chik Fil A", "solid chicken sandwich", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.unhealthy, Ethnicity.american),
        ("Mitsuwa", "fast delicious japanese food", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.healthy, Ethnicity.japanese),
        ("Taqueria Hoy", "yummy yummy tacos", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.mexican),
        ("Taqueria Ayutla Oaxaca", "tacos from a truck hit different", Price.cheap, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.mexican),
        ("Grill City", "service is hit or miss but the food reminds me of the phillipines", Price.cheap, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.filipino),
        ("Kebab Shop", "fast, delicious healthy, but not really cheap lol", Price.moderate, Speed.fast, Ambiance.simple, Nutrition.healthy, Ethnicity.mediterranean),
        ("Pom and Olive", "Kebab?", Price.cheap, Speed.moderate, Ambiance.simple, Nutrition.healthy, Ethnicity.mediterranean),
        ("Brodard", "Awesome vietnamese food, lots of choices, spring rolls are top tier", Price.cheap, Speed.fast, Ambiance.moderate, Nutrition.healthy, Ethnicity.vietnamese),
        ("Yuk daejang", "solid korean food", Price.cheap, Speed.moderate, Ambiance.moderate, Nutrition.moderate, Ethnicity.korean),
        ("Ike's Sandwiches", "Best sandwiches to me", Price.moderate, Speed.fast, Ambiance.moderate, Nutrition.moderate, Ethnicity.american),
        ("Pho Ba Co", "decent Pho", Price.moderate, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.vietnamese),
        ("Raising Canes", "chicken tenders!", Price.moderate, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.american),
        ("Dave's Hot Chicken", "nashville hot chicken sandwich.", Price.moderate, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.american),

        #Casual
        ("Gerry's Grille", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.filipino),
        ("Tender greens", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.healthy, Ethnicity.american),
        ("Coco Ichibanya", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.japanese),
        ("A&J", "test description", Price.moderate, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.chinese),
        ("Taco Stand", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.mexican),
        ("Siam Station", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.thai),
        ("Tang 190", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.korean),
        ("Hop Doddy", "test description", Price.moderate, Speed.slow, Ambiance. moderate, Nutrition.moderate, Ethnicity.american),
        ("Etcetera", "test description", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.japanese),
        ("Nana San", "test description", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.japanese),
        ("Northern Cafe", "test description", Price.moderate, Speed.fast, Ambiance.simple, Nutrition.moderate, Ethnicity.chinese),
        ("Tanakaya", "test description", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.healthy, Ethnicity.japanese),
        ("Bella Cuba", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.cuban),
        ("Ai Pono Cafe", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.hawaiian),
        ("Ramen Zetton", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.japanese),
        ("Kittakata Ramen Ban Nai", "test description", Price.moderate, Speed.moderate, Ambiance.simple, Nutrition.moderate, Ethnicity.japanese),

        #Sitdown
        ("Gurume Sushi", "test description", Price.expensive, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.japanese),
        ("Cucina Enoteca", "test description", Price.expensive, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.italian),
        ("Yard House", "test description", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.american),
        ("Houstons", "test description", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.american),
        ("North Italia", "test description", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.italian),
        ("Urth Caffe", "test description", Price.expensive, Speed.slow, Ambiance.simple, Nutrition.healthy, Ethnicity.american),
        ("Ini Restorante", "test description", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.italian),
        ("Inka mama", "test description", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.peruvian),
        ("Zip KBBQ", "test description", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.korean),
        ("Honda Ya", "japanese izakaya", Price.moderate, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.japanese),

        #Special Occasion
        ("Baekjeong", "test description", Price.expensive, Speed.slow, Ambiance.moderate, Nutrition.moderate, Ethnicity.korean),
        ("Capital Grille", "test description", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.american),
        ("Mastros", "test description", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.american),
        ("Habana", "test description", Price.expensive, Speed.slow, Ambiance.fancy, Nutrition.moderate, Ethnicity.cuban),

    ]
    for i in restaurants:
        restaurant_list.append(Restaurant(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

create_restaurants()

def get_restaurants() -> list[Restaurant]:
    """Returns a list of restaurants.
    Args: None
    Returns: List of restaurants
    """
    return restaurant_list
