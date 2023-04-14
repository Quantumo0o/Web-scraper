from flask import Flask, render_template, request,jsonify, session
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging
import pymongo
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)

app = Flask(__name__)
count = 0

@app.route("/", methods = ['GET'])
def homepage():
    
    return render_template("index.html")

@app.route("/review" , methods = ['POST' , 'GET'])
def index():
    global flipkartPage
    global count
    global searchString
    global page
    if request.method == 'POST':
        if request.method == 'POST' and 'next' in request.form:
            count += 1
        else:
            count = 0
            page = 0
        
        if count==0:
            searchString = request.form['content'].replace(" ","")


        try:
            if (count==0 or count==8)  and searchString != "":
                count=0
                flipkart_url = "https://www.flipkart.com/search?q=" + searchString + "&page=" + str(page)
                page=page+1
                uClient = uReq(flipkart_url)
                flipkartPage = uClient.read()
                uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[count]

            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            #prodRes = requests.get(productLink)
            prodRes1 = uReq(productLink)
            prodRes = prodRes1.read()
            prodRes1.close()
            #prodRes.encoding='utf-8'
            prod_html = bs(prodRes, "html.parser")
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})
            productprice = prod_html.find_all('div',{'class':"_30jeq3 _16Jk6d"})[0].text
            productname = prod_html.find_all('span',{'class':"B_NuCI"})[0].text
            
            img_tag = prod_html.find_all('div', {'class': '_1BweB8'})[0].div.img['src']

            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            
            reviews = []
            
            
            for commentbox in commentboxes:
                try:
                    #name.encode(encoding='utf-8')
                    name = commentbox.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

                except:
                    name="no name"
                    logging.info("name")
                
                try:
                    #rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text


                except:
                    rating = 'No Rating'
                    logging.info("rating")

                try:
                    #commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text

                except:
                    commentHead = 'No Comment Heading'
                    logging.info(commentHead)
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    #custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text
                except Exception as e:
                    logging.info(e)
                    custComment = 'No Comment'

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                        "Comment": custComment}
                
                reviews.append(mydict)
                x= searchString + "," + name+","+rating+","+commentHead+","+custComment
                fw.write(x + '\n')
            

                
            logging.info("log my final result {}".format(reviews))

            
            #client = pymongo.MongoClient("mongodb+srv://username:password@cluster0.ln0bt5m.mongodb.net/?retryWrites=true&w=majority")
            #db =client['scrapper_eng_pwskills']
            #coll_pw_eng = db['scraper_pwskills_eng']
            #coll_pw_eng.insert_many(reviews)
            
            return render_template('index.html', reviews=reviews[0:(len(reviews)-1)],productname=productname, price=productprice, img_tag=img_tag)
            
        except Exception as e:
            logging.info(e)
            print(e)
            message= 'Please Enter Product'
            print(message)
            return render_template('index.html',message=message)
        
    else:
        return render_template('index.html')


if __name__=="__main__":
        app.run(debug=True,host="0.0.0.0")
