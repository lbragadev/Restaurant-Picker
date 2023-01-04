# Restaurant-Picker
Simple Project that picks a restaurant for you. This project is tailored specifically for my use. The restaurants are located in Irvine/Orange County area.

## About The Project
Have you ever spent time wondering where to eat? Have you ever asked your significant other "Where should we eat?" only to get the response, "I'm down for anything:)". Do you want to save time picking a restaurant? If you said yes to any of the questions, Then that is exactly why im building this project to save time and pick restaurants based on your liking. Waste less time deciding, and pick a restaurant with ease :)
<br />
![](https://github.com/lbragadev/Restaurant-Picker/blob/main/whatdoyouwant.gif)



## Design Choices

My goal with building this project is to build something fast, simple to run and maintain but is flexible to change and new features.

## Dependencies
To install dependencies run command shown below;

```bash
pip3 install -r requirements.txt
```

## How to Run
Sample commands
```bash
python pick_restaurant.py --price "cheap" --nutrition "healthy"
python pick_restaurant.py --ethnicity "mexican"
python pick_restaurant.py --price "expensive" --ambiance "fancy"
```

Alternatively you can use the pick_restaurant_prompted.py script instead to get prompted for each parameter
```bash
python pick_restaurant_prompted.py
```

For more info about the cli
```bash
python pick_restaurant.py --help
python pick_restaurant_prompted.py --help
```
### Built With
- Python
