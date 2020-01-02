#!/usr/bin/env python

import mechanicalsoup
import json
import random
import time

#delay_in_seconds= 0.5
browser = mechanicalsoup.StatefulBrowser()

baseGoodReadsURL = "https://www.goodreads.com/quotes/tag/"

#tagList = ['success','achievements','academic','sports','school','excellence']


def quoteLister(tagRequested):
	quoteList = []
	tag = tagRequested
	browser.open(baseGoodReadsURL+tag)
	page = browser.get_current_page()
	quoteListObject = page.find_all("div",attrs = {"class": "quoteText"})
	# s = str(quoteList[1].contents[0])
	cnt = 0
	for quote in quoteListObject:
	    quoteText = quote.contents[0]
	    if(len(quoteText)<200):
	        cnt+=1
	        quoteList.append(quoteText)

	print("No. of quotes fetched on {tag} = {count}".format(tag=tag,count=cnt))

	return quoteList

def main():
	choiceTag = 'y'
	while(choiceTag != 'n'):
		requestedTag = input('Enter the tag whose quote you want: ')
		currentQuoteList = quoteLister(requestedTag)
		choice = 'y'
		while(choice != 'n'):
			currentQuote = random.choice(currentQuoteList)
			print(currentQuote)
			choice = input('Another Quote? (y/n): ')
		choiceTag = input('want quote from another tag? (y/n): ')

	print('Thanks!!!')


if __name__=='__main__':
	start_time = time.time()
	main()
	#quote = quotePicker(tagList[0])
	# print(quote)
	elapsed_time = time.time() - start_time
	print("elapsed_time =",elapsed_time)