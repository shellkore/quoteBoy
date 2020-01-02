# quoteBoy
An app to fetch quotes from web.

## Description
Generally while posting in facebook, we need some good quote to put in caption.
By using this web-app you can get a random quote for the requested tag.
The longer length quotes are filtered out as they can't be used for post.


### API

`http://quoteboy.herokuapp.com/quote?tag='<YOUR_TAG>'`

## RUN IN LOCAL MACHINE

Install requirements

`pip install -r requirements.txt`
    
 run quoter.py
 
`python quoter.py`
 
 To save a json file for multiple tags
 
`python save_in_file.py`

on running this file, you will get a json file having quotes of the tag you mentioned in the format:
```
{<tag>:
     {  
        "quote_id":<quoteID>,
        "content":<quoteText>,
        "author":<authorName>
    }
 }
 ```

## RUN APP IN LOCAL MACHINE

run app.py 

`python app.py`

Task list:

- [X] create a flask app.
- [ ] increase the number of sites to scrape from.
- [X] create API.
- [X] deploy the web-app.
- [ ] create firefox or chrome extension.

Anyone who wants to work on this project can create an issue to the corresponding task from Task list.
Please create an issue for any bug or any additional feature.

>mayTheGitBeWithYou
