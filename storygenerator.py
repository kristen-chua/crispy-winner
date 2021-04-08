#https://dev.to/mindninjax/how-to-build-a-random-story-generator-using-python-1oah
import random

#elements
when = ['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos arrived']
who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America']
where = ['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ']
what = ['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance']
sequencewords = ['Next','Then','Afterward','Meanwhile']
verb = ['went under','ran through','had fun at','went shopping in']
conclusions = ['finally', 'in conclusion', 'in the end', 'thus', 'to conclude']
#capitalizes conclusions
conclusions = [conclusion.capitalize() for conclusion in conclusions]

#story starter
print(random.choice(when)+', ' + random.choice(who) + ' went to ' + random.choice(where) + ' ' + random.choice(what) + '.')
#story body
i=0
for i in range(0,6):
	print(random.choice(sequencewords)+', '+random.choice(who)+' ',random.choice(verb)+' '+random.choice(where)+' '+random.choice(what)+'.')	
	i=i+1

#how do I make it so that the sequencewords and actions do not repeat?
#A: use random.shuffle instead of random.choice
#add conclusion sentence
print(random.choice(conclusions) + ', ' + random.choice(who) + ' went to ' + random.choice(where) + ' ' + random.choice(what) + '.')
