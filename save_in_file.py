#!/usr/bin/env python

import mechanicalsoup
import json
import random
import time
import string

delay_in_seconds= 0.5
browser = mechanicalsoup.StatefulBrowser()


baseGoodReadsURL = "https://www.goodreads.com/quotes/tag/"

# tagList = ['success','achievements','academic','sports','school','excellence']

def generateQuoteID(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

quoteDict = {
	
}

def quoteDictGenerator(tagRequested):
    quoteList = []
    tag = tagRequested
    browser.open(baseGoodReadsURL+tag)
    page = browser.get_current_page()
    quoteListObject = page.find_all("div",attrs = {"class": "quoteText"})
    # s = str(quoteList[1].contents[0])
    cnt = 0
    for quote in quoteListObject:
        quoteText = quote.contents[0].strip()
        author = quote.find("span",attrs = {"class":"authorOrTitle"})
        authorName = author.text.strip()
        quoteID = generateQuoteID()
        if(len(quoteText)<200):
            cnt+=1
            quoteobj = {
                "quote_id":quoteID,
                "content":quoteText,
                "author":authorName
            }
            if tag not in quoteDict.keys():
                quoteDict[tag]=[]
                
            quoteDict[tag].append(quoteobj)

    print("No. of quotes fetched on {tag} = {count}".format(tag=tag,count=cnt))

def main():
    tagListString = input("Enter your prefered tags (seperate them by ',' )")
    tagList = tagListString.split(',')

    for tag in tagList:
        quoteDictGenerator(tag)

    quoteJSONobj = json.dumps(quoteDict)

    with open('quotes.json','w') as jsonFile:
        json.dump(quoteJSONobj,jsonFile)

    print("File successfully created with tags {}".format(tagListString))



if __name__=='__main__':
	start_time = time.time()
	main()
	# quote = quotePicker(tagList[0])
	# print(quote)
	elapsed_time = time.time() - start_time
	print("elapsed_time =",elapsed_time)