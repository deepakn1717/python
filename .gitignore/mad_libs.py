### fills the mad words###

print "Game Started!"

name = raw_input("what is your name ?")

adjectives1 = raw_input("Enter an Adjective")
adjectives2 = raw_input("Enter an Adjective")
adjectives3 = raw_input("Enter an Adjective")

verbs1 = raw_input("Enter an Verb")
verbs2 = raw_input("Enter an Verb")
verbs3 = raw_input("Enter an Verb")

nouns1 = raw_input("Enter a noun")
nouns2 = raw_input("Enter a noun")
nouns3 = raw_input("Enter a noun")
nouns4 = raw_input("Enter a noun")

animal = raw_input("enter a name of animal")
food = raw_input("enter the name of food")
fruit = raw_input("enter a name of fruit")
number = raw_input("enter a number")
superhero = raw_input("enter a super hero name")
country = raw_input("eanter a name of country")
dessert = raw_input("enter the name of dessert")
year = raw_input("enter a year")


#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."
print STORY % (adjectives1,name,verbs1,adjectives2,nouns1,nouns2,animal,food,verbs2,nouns3,fruit,adjectives3,name,verbs3,number,name,superhero,superhero,name,country,name,dessert,name,year,nouns4)




