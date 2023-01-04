import click

from restaurant import *


@click.command()
@click.option('--price', type=click.Choice(["cheap", "moderate", "expensive"]), prompt='price type of restaurant ["cheap", "moderate", "expensive]', required=False)
@click.option('--speed', type=click.Choice(["slow", "moderate", "fast"]), prompt='speed of service and experience', required=False)
@click.option('--ambiance', type=click.Choice(["simple", "moderate", "fancy"]), prompt='the ambiance of the restaurent IE: laid back, bougie', required=False)
@click.option('--nutrition', type=click.Choice(["healthy", "moderate", "unhealthy"]), prompt='is it healthy for you?', required=False)
@click.option('--ethnicity', type=click.Choice(["filipino", "mexican", "italian", "american", "thai", "korean", "japanese", "chinese", "vietnamese", "mediterranean"]), prompt='the ethnic origin of the cuisine', required=False)
def pick_restaurant_prompted(price: Price, speed: Speed, ambiance: Ambiance, nutrition: Nutrition, ethnicity: Ethnicity):
    restaurants = []

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


    if len(restaurants) < 1:
        click.echo("No restaurant found!")
        return
    result = restaurants[randint(0, len(restaurants)-1)]
    click.echo(result.get_details())
    
if __name__ == '__main__':
    pick_restaurant_prompted()
