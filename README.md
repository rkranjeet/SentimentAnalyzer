# SentimentAnalyzer
## A python Script to Scrap Reviews from [cnet.com](https://www.cnet.com/) and Finding customer's Sentiment
### Features
  * Scrap's Multiple web pages and parses relavent data.(Here review of Mobile phones are scraped).
  * Determine's A statement(Review) is positive, negative or neutral.
  * Graphically(By PyChart) Compares Customer's Sentiment's over Different Brands (In our case Review's of Samsung and Apple are compared).
### Tech Stack Used
  * Requests - To Make HTTPS Get Request for Web Pages.
  * BeautifulSoup - To Parse HTML from HTTPS response collected.
  * TextBlob - To Determine Sentiment of Reviews in the Form of Polarity. 
  * matplotlib - For Graphical Representation.
