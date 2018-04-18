import random
header = "Fill out these questions to generate your own silly mad libs story instantly online! This mad lib only has nouns, verbs, and adjectives so it can be used with Kindergarten common core classes. (Hint: a Verb is  an action. A noun is a person/place/thing. An adjective describes a  person/place/thing.)"

body = "Photo Shoot!"
prompt = "Please enter "

def get_inputs():
    animals = input(prompt + "Animals: ")
    feeling = input(prompt + "a Feeling: ")
    things = input(prompt + "Things (plural) seperated by commas: ")
    professional = input(prompt + "a Professional (like 'Baker'): ")
    clothing = input(prompt + "a Piece of Clothing: ")
    #things2 = input(prompt + "Things (plural): ")
    person = input(prompt + "a Person: ")
    place = input(prompt + "a Place: ")
    verb = input(prompt + "a Verb (ending in 'ing'): ")
    food = input(prompt + "a Food: ")

    list_of_things = things.split()
    rand_int_in_list = random.randint(1, len(list_of_things)) - 1
    things2 = list_of_things.pop(rand_int_in_list)
    things = "".join(list_of_things)

    output = "Say '{food},' the photographer said as the camera flashed! {person} and I had gone to {place} to get our photos taken today. The first photo we really wanted was a picture of us dressed as {animals} pretending to be {professional}. When we saw the proofs of it, I was a bit {feeling} because it looked different than in my head. (I hadn't imagined so many {things2} behind us.) However, the second photo was exactly what I wanted. We both looked like {animals} wearing {clothing} and {verb} --exactly what I had in mind!"

    print(output.format(animals = animals, feeling = feeling, things = things, professional = professional, clothing = clothing, things2 = things2, person = person, place = place, verb = verb, food = food))

def game():
    continue_play = 'c'
    print(header)
    print(body)
    while continue_play == 'c':
        get_inputs()
        continue_play = input("Would you like to (c)ontinue or (q)uit?: " )

game()
