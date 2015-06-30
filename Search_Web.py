import urllib
import csv

wordsfile = csv.DictReader(open("words.csv"))


#Search for every word in the words list in every URL in the links list. Print both word and the URL if found

for word in wordsfile:
	curr_word = word['search_word']

	linksfile = csv.DictReader(open("links.csv"))

	for link in  linksfile:
		curr_link = link['url']
		site = urllib.urlopen(curr_link).read()

        	if curr_word in site:
			print(curr_word,"-> present in :",link)
