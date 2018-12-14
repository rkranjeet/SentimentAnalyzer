
# coding: utf-8

# In[2]:


import time
import csv
import requests
from textblob import TextBlob
from  bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# In[3]:


def percentage(part,whole):
    return 100*float(part)/float(whole)
def piechart(positive,neutral,negative,n_reviews,company):
    labels = ['Positive ['+str(positive)+'%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
    sizes = [positive, neutral, negative]
    colors = ['yellowgreen', 'gold', 'red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('How people are reacting on '+company+' Phones '+'by Analysing '+str(n_reviews)+' No of Reviews')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
positive = [0,0]
negative = [0,0]
neutral  = [0,0]
n_Apple = 0
n_Samsung = 0              


# In[8]:



for i in range(1,10):
    if(i==1):
        url="https://www.cnet.com/topics/phones/products/?filter=manufacturer_samsung_manufacturer_apple"
        csv_file = open('appleVSsamsung.csv','w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Product","Review","Polarity"])
    else:
        url='https://www.cnet.com/topics/phones/products/'+str(i)+'/?filter=manufacturer_samsung_manufacturer_apple'
    try:
        web_site = requests.get(url,verify=False)
    except Exception as e:
         None
    time.sleep(5)
    content = BeautifulSoup(web_site.content,'html.parser')
    blocks = content.find_all('div',class_='itemInfo')
    time.sleep(2)
     
    for review in blocks:
        #list_review = [review.a.text.strip(),review.p.text,str(format(TextBlob(review.p.text).sentiment.polarity,'.2f')).strip()]
        try:
            name_p = review.a.h3.text.strip()
            review_p = review.p.text
            polarity_p = TextBlob(review_p).sentiment.polarity
            if 'Apple' in name_p:
                if polarity_p==0:
                    neutral[0]+=1
                elif polarity_p<0.2:
                    negative[0]+=1
                elif polarity_p>0.2:
                    positive[0]+=1
                n_Apple+=1
            else:
                if polarity_p==0:
                    neutral[1]+=1
                elif polarity_p<0.2:
                    negative[1]+=1
                elif polarity_p>0.2:
                    positive[1]+=1
                n_Samsung+=1 
            csv_writer.writerow([name_p,review_p,polarity_p])
        except Exception:
            None
csv_file.close()
print(n_Apple+n_Samsung)
Apple_pos = format(percentage(positive[0],n_Apple),'.2f')
Apple_neg = format(percentage(negative[0],n_Apple),'.2f')
Apple_neu = format(percentage(neutral[0],n_Apple),'.2f')

Samsung_pos = format(percentage(positive[0],n_Samsung),'.2f')
Samsung_neg = format(percentage(negative[0],n_Samsung),'.2f')
Samsung_neu = format(percentage(neutral[1],n_Samsung),'.2f')
piechart(Apple_pos,Apple_neu,Apple_neg,n_Apple,'Apple')
piechart(Samsung_pos,Samsung_neu,Samsung_neg,n_Samsung,'Samsung')


