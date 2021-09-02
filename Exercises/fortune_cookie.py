#Write a fortune cookie generator that prints out a random fortune when it is run.
import random

fortunes = ["You will find love", "You will become rich", "You will find love"]
fortune = random.choice(fortunes)
print(fortune)
