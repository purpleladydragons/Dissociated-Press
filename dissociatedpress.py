#TODO:
#Make it work properly with chunksize > 1
	#Right now, it just uses first word in chunk


import random
import re
import string

original = "In terms of making a contribution to the world, the post was definitely a success. It generated a great conversation and I think people will run with the idea and figure out how to improve upon it. It also gave my new project a little bump. Though the massive spike of traffic is gone, I continue to get a few hundred visitors a day which is great. It has had an impact on organic traffic thanks to some new inbound links."

def dissoc(text, chunksize, chunks):
	new = []
	newstring = ""
	words = text.split()
	start = random.randint(0,len(words)-chunksize)
	end = start + chunksize
	seed = words[start:end]
	for x in range(chunks):
		new.append(seed)
		seed = find_matches(words,seed,chunksize)
	for sublist in new:
		for word in sublist:
			newstring += word+" "
	return newstring

def find_matches(words,seed,chunksize):
	"""find all occurrences of seed"""
	i = -1
	occurs = []

	
	#Make seed a findable part of words
	#Just make it 1-word compatible for now


	try: #this is not running, it seems that seed is not in words; why?
		while(True):
			i = words.index(seed[0],i+1)
			occurs.append(i)
	except ValueError:
		pass

	if len(occurs) <= 1:
		start = random.randint(0,len(words)-chunksize)
		end = start + chunksize
		seed = words[start:end]

	else: #intention: randomly choose one of the occurrences, and then use next chunksize words as new seed
		start = random.randint(0,len(occurs)-1)	#randomly chooses assigns an index in occurs
		seed = occurs[start] #seed is now the index number of an occurrence
		start = seed+chunksize #start is the chunksize index after the previous seed
		end = start + chunksize #end is next chunksize index
		seed = words[start:end] #seed is words from start to end
	return seed

print dissoc(original,2,30)

"""original = original.split()
seed = original[2:4]
print original.index(seed)"""
