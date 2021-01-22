from bs4 import BeautifulSoup
import requests, lxml, html5lib, feedparser, re
import praw
import time
import smtplib

reddit = praw.Reddit(
    client_id = 'your client id',
    client_secret = 'your client',
    user_agent = 'your agent',
    username = 'your username',
    password = 'enter your password'
)

def emaillog(msg):
    conn = smtplib.SMTP('smtp.gmail.com', 587)  # define the object
    print(conn.ehlo())  # make the connection to the server
    print((conn.starttls()))  # encrypt the email
    print(conn.login('email', 'password'))
    conn.sendmail('email', 'email', msg)
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

        CYAN = ''
        RED = ''
        CYANEND = ''
        REDEND = ''

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

        CYAN = ''
        RED = ''
        CYANEND = ''
        REDEND = ''

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
        return myMessage


class freeCodeCamp():
    def hotarticles(self):

        URL = 'https://www.freecodecamp.org/news/'      

        source = requests.get(URL).content

        soup = BeautifulSoup(source, 'lxml')

        post = 0
        numberPosts = 5
        myMessage = []

        CYAN = ''
        RED = ''
        CYANEND = ''
        REDEND = ''

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
        return myMessage
    
class Reddit():

    def learnprogramming(self):

        numberPosts = 5
        post = 0
        arguments = 3
        myMessage = []
        articles = []

        CYAN = ''
        RED = ''
        CYANEND = ''
        REDEND = ''

        Subject = RED + 'See the top 5 posts from learnprogramming!' + REDEND + '\n'

        myMessage.append(Subject)

        for submission in reddit.subreddit('learnprogramming').top('day'):
            if post < numberPosts:
                articles.append([str(submission.title), str(submission.score), str(submission.url)])
                post += 1
            else:
                break

        myMessage = concatenateContent(articles, myMessage, numberPosts, arguments, CYAN, CYANEND)
        return myMessage

    def Python(self):
        numberPosts = 5
        post = 0
        arguments = 3
        myMessage = []
        articles = []

        CYAN = ''
        CYANEND = ''

        Subject = 'See the top 5 posts from Python!' + '\n'

        myMessage.append(Subject)

        for submission in reddit.subreddit('Python').top('day'):
            if post < numberPosts:
                articles.append([str(submission.title), str(submission.score), str(submission.url)])
                post += 1
            else:
                break

        myMessage = concatenateContent(articles, myMessage, numberPosts, arguments, CYAN, CYANEND)
        return myMessage

    def csCareerQuestions(self):
        numberPosts = 5
        post = 0
        arguments = 3
        myMessage = []
        articles = []

        CYAN = ''
        CYANEND = ''

        Subject = 'See the top 5 posts from cscareerquestions!' + '\n'

        myMessage.append(Subject)

        for submission in reddit.subreddit('cscareerquestions').top('day'):
            if post < numberPosts:
                articles.append([str(submission.title), str(submission.score), str(submission.url)])
                post += 1
            else:
                break

        myMessage = concatenateContent(articles, myMessage, numberPosts, arguments, CYAN, CYANEND)
        return myMessage
    
if __name__ == "__main__":
    body = ''
    body = body + Reddit().Python() + '\n\n'
    body = body + Reddit().learnprogramming() + '\n\n'
    body = body + Reddit().csCareerQuestions() + '\n\n'
    body = body + towardsDataScience().toparticles() + '\n\n'
    body = body + towardsDataScience().hotarticles() + '\n\n'
    body = body + freeCodeCamp().hotarticles() + '\n\n'
    
    emaillog(body.encode('utf-8').strip())
