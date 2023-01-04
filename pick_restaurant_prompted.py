"""This Cli prompts the user a set of parameters to be provided and then picks a random restaurant matching the set of parameters."""
import click

from restaurant import *


@click.command()
@click.option('--price', type=click.Choice(["cheap", "moderate", "expensive", "any"]), prompt='price type of restaurant ["cheap", "moderate", "expensive]')
@click.option('--speed', type=click.Choice(["slow", "moderate", "fast", "any"]), prompt='speed of service and experience')
@click.option('--ambiance', type=click.Choice(["simple", "moderate", "fancy", "any"]), prompt='the ambiance of the restaurent IE: laid back, bougie')
@click.option('--nutrition', type=click.Choice(["healthy", "moderate", "unhealthy", "any"]), prompt='is it healthy for you?')
@click.option('--ethnicity', type=click.Choice(["filipino", "mexican", "italian", "american", "thai", "korean", "japanese", "chinese", "vietnamese", "mediterranean", "any"]), prompt='the ethnic origin of the cuisine')
@click.option('--result-type', type=click.Choice(['List', 'Random']), prompt='do you want a random selection or display list of restaurants')
def pick_restaurant_prompted(price: Price, speed: Speed, ambiance: Ambiance, nutrition: Nutrition, ethnicity: Ethnicity, result_type: str):
    """Prints a random restaurant that satisfies the cli parameters.

    Args:
      price: Price range
      speed: Speed of service and experience
      ambiance: Indoor setting of the place
      nutrition: nutritional rating of a meal here on average
      ethnicity: Ethnic origin of the cuisine
      result_type: print list of restaurants or select one randomly

    Returns: None

    """
    restaurants = []

    #for each restaurant check if restaurant doesn't meet specified criteria skip and dont add to list
    for i in get_restaurants():
        if price != None and i.price.name != price and price != "any":
            continue
        if speed != None and i.speed.name != speed and speed != "any":
            continue
        if ambiance != None and i.ambiance.name != ambiance and ambiance != "any":
            continue
        if nutrition != None and i.nutrition.name != nutrition and nutrition != "any":
            continue
        if ethnicity != None and i.ethnicity.name != ethnicity and ethnicity != "any":
            continue
        else:
            restaurants.append(i)

    #if no restaurants meet the criteria print message end return
    if len(restaurants) < 1:
        click.echo("No restaurant found matching criteria!")
        return

    #print restaurants list
    if result_type == "List":
        for x in restaurants:
            click.echo(x.get_details())
        return

    #return random restaurant that meets criteria
    result = restaurants[randint(0, len(restaurants)-1)]
    click.echo(result.get_details())
    
if __name__ == '__main__':
    pick_restaurant_prompted()
