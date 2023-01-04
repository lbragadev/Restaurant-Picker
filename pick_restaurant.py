"""Cli to pick a random restaurant that matches the set of parameters provided."""
import click

from restaurant import *
    
@click.command()
@click.option('--price', type=click.Choice(["cheap", "moderate", "expensive"]), help='price type of restaurant ["cheap", "moderate", "expensive]', required=False)
@click.option('--speed', type=click.Choice(["slow", "moderate", "fast"]), help='speed of service and experience', required=False)
@click.option('--ambiance', type=click.Choice(["simple", "moderate", "fancy"]), help='the ambiance of the restaurent IE: laid back, bougie', required=False)
@click.option('--nutrition', type=click.Choice(["healthy", "moderate", "unhealthy"]), help='how healthy?', required=False)
@click.option('--ethnicity', type=click.Choice(["filipino", "mexican", "italian", "american", "thai", "korean", "japanese", "chinese", "vietnamese", "mediterranean"]), help='the ethnic origin of the cuisine', required=False)
@click.option('--list', type=bool, help='do you want to display list of restaurants or one randomly selected. (True for List, False for randomly selected)', required=False, default=False)
def pick_restaurant(price: Price, speed: Speed, ambiance: Ambiance, nutrition: Nutrition, ethnicity: Ethnicity, list: bool):
    """Prints a random restaurant that satisfies the cli parameters.

    Args:
      price: Price range
      speed: Speed of service and experience
      ambiance: Indoor setting of the place
      nutrition: nutritional rating of a meal here on average
      ethnicity: Ethnic origin of the cuisine
      list: print list of restaurants or select one randomly

    Returns: None

    """
    restaurants = []

    #for each restaurant check if restaurant doesn't meet specified criteria skip and dont add to list
    for i in get_restaurants():
        if price != None and i.price.name != price:
            continue
        if speed != None and i.speed.name != speed:
            continue
        if ambiance != None and i.ambiance.name != ambiance:
            continue
        if nutrition != None and i.nutrition.name != nutrition:
            continue
        if ethnicity != None and i.ethnicity.name != ethnicity:
            continue
        else:
            restaurants.append(i)

    #if no restaurants meets the criteria print message end return
    if len(restaurants) < 1:
        click.echo("No restaurant found matching criteria!")
        return

    #print restaurants list
    if list:
        for i in restaurants:
            click.echo(i.get_details())
        return

    #return random restaurant that meets criteria
    result = restaurants[randint(0, len(restaurants)-1)]
    click.echo(result.get_details())

if __name__ == '__main__':
    pick_restaurant()
