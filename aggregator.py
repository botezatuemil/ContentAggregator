from bs4 import BeautifulSoup
import requests, lxml, html5lib, feedparser, re
import praw
import time
import smtplib
from email.message import EmailMessage


reddit = praw.Reddit(
    client_id = 'UcrUFaWeSgDdNg',
    client_secret = 'LBUDzGudjPXWfTPgxwl4LfV1UJME2A',
    user_agent = 'redditPythonScrapper',
    username = 'IohannesMatrix',
    password = 'quoraforlife14!'
)

def emaillog(msg):
    conn = smtplib.SMTP('smtp.gmail.com', 587)  # define the object
    print(conn.ehlo())  # make the connection to the server
    print((conn.starttls()))  # encrypt the email
    print(conn.login('btzemil@gmail.com', 'emil14pro'))
    conn.sendmail('btzemil@gmail.com', 'btzemil@gmail.com', msg)
    conn.quit()

def concatenateContent(articles, myMessage, numberPosts, arguments, CYAN, CYANEND):
    for i in range(numberPosts):
        for j in range(arguments):
                if j == 0:
                    articles[i][j] = CYAN + articles[i][j] + ' Likes: ' + articles[i][j + 1] + CYANEND + '\n'
                else:
                    articles[i][j] = articles[i][j] + '\n'
        del articles[i][1]

        
    for i in range(numberPosts):
        message = '\n'.join(articles[i])
        myMessage.append(message)

    myMessage = '\n\n'.join(myMessage)

    return myMessage


class towardsDataScience:
    def hotarticles(self):

        URL = 'https://towardsdatascience.com/tagged/python'

        source = requests.get(URL).text

        soup = BeautifulSoup(source, 'lxml')

        post = 0
        numberPosts = 5
        myMessage = []
        arguments = 4
        articles = []

        CYAN = '\033[96m'
        RED = '\033[93m'
        CYANEND = '\033[0m'
        REDEND = '\033[0m'

        Subject = RED + 'See the hottest 5 python articles from towardsDataScience!' + REDEND + '\n'
        myMessage.append(Subject)

        for article in soup.find_all('div', class_='n p'):
            if post < numberPosts:
                try:
                    headline = article.h1.a.text
                    summary = article.p.text
                    link = article.find('a', href=True)
                    likes = article.find('button').text
                    articles.append([headline, likes, summary, link['href']])

                except:
                    continue
                post += 1
            else:
                break
        
        myMessage = concatenateContent(articles, myMessage, numberPosts, arguments, CYAN, CYANEND)
        #print(myMessage)
        return myMessage

    def toparticles(self):
        URL = 'https://towardsdatascience.com/tagged/python'

        source = requests.get(URL).text

        soup = BeautifulSoup(source, 'lxml')

        post = 0
        numberPosts = 5
        articles = []
        arguments = 4
        myMessage = []

        CYAN = '\033[96m'
        RED = '\033[93m'
        CYANEND = '\033[0m'
        REDEND = '\033[0m'

        Subject = RED + 'See the top 5 python articles from towardsDataScience!' + REDEND + '\n'

        myMessage.append(Subject)

        for article in soup.find_all('div', class_='n p'):
            if post < numberPosts:
                try:
                    headline = article.h1.a.text 

                    summary = article.p.text 

                    link = article.find('a', href=True)
            
                    likes =  article.find('button').text
                    
                    articles.append([headline, likes, summary, link['href']]) 

                except:
                    continue
                post += 1
            else:
                break
        
        def sort(articles):
            articles.sort(key=lambda x : x[1], reverse=True)
            return articles

        sort(articles) 

        myMessage = concatenateContent(articles, myMessage, numberPosts, arguments, CYAN, CYANEND)
        #emailAggregator.append(myMessage)
        #print(myMessage)
        return myMessage


class freeCodeCamp():
    def hotarticles(self):

        URL = 'https://www.freecodecamp.org/news/'      

        source = requests.get(URL).content

        soup = BeautifulSoup(source, 'lxml')

        post = 0
        numberPosts = 5
        myMessage = []

        CYAN = '\033[96m'
        RED = '\033[93m'
        CYANEND = '\033[0m'
        REDEND = '\033[0m'

        Subject = RED + 'See the top 5 python freecodecamp articles' + REDEND + '\n'

        myMessage.append(Subject)

        for article in soup.find_all('article'):  
            if post < numberPosts: 
                try:  
                    link = article.find('a', href=True)
                    myMessage.append(CYAN + 'https://www.freecodecamp.org' + link['href'] + CYANEND)
                except:
                    continue
                post += 1
            else:
                break
        
        myMessage = '\n\n'.join(myMessage)
        #emailAggregator.append(myMessage)
        #print(myMessage)
        return myMessage
    
class Reddit():

    def learnprogramming(self):

        numberPosts = 5
        post = 0
        arguments = 3
        myMessage = []
        articles = []

        CYAN = '\033[96m'
        RED = '\033[93m'
        CYANEND = '\033[0m'
        REDEND = '\033[0m'
        
        Subject = RED + 'See the top 5 posts from learnprogramming!' + REDEND + '\n'

        myMessage.append(Subject)

        for submission in reddit.subreddit('learnprogramming').top('day'):
            if post < numberPosts:
                articles.append([str(submission.title), str(submission.score), str(submission.url)])
                #print(str())
                #myMessage.append((str(submission.title)) + ' Karma: ' + (str(submission.score)) + '\n' +  (str(submission.url)) + '\n\n')
                post += 1
            else:
                break

        myMessage = concatenateContent(articles, myMessage, numberPosts, arguments, CYAN, CYANEND)
        # print(myMessage)
        return myMessage

    
    



if __name__ == "__main__":

    body = (towardsDataScience().hotarticles() + '\n').encode('utf-8').strip()
   
    #emailAggregator = emailAggregator + towardsDataScience().toparticles() + '\n'
    #freeCodeCamp().hotarticles()
    #Reddit().learnprogramming()
    #print(emailAggregator)
    emaillog(body)