#Webpage that asks for user's input (a number between 1-5), and brings up a loading page. The redirects the user to the random webpage based on a set of random words that were picked.
#CNA 335, Winter 2019
#Ian Hardgrave, Wyatt Humphreys


#sources: https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask
#https://github.com/dwyl/english-words
#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
#https://productforums.google.com/forum/#!topic/websearch/pywUIBP6C20
#https://www.youtube.com/watch?v=1PipslRY0bc
#https://stackoverflow.com/questions/44962932/how-to-use-rowcount-in-mysql-using-python
#http://stackoverflow.max-everyday.com/2017/09/python-mysql-connector-internalerror-unread-result-found/
#https://stackoverflow.com/questions/1082580/how-to-build-jars-from-intellij-properly
#https://stackoverflow.com/questions/4871051/getting-the-current-working-directory-in-java
#https://stackoverflow.com/questions/235855/how-do-i-stretch-a-background-image-to-cover-the-entire-html-element
#http://bouncejs.com
#https://css-tricks.com/redirect-web-page/
#https://www.geeksforgeeks.org/global-local-variables-python/
#https://www.youtube.com/watch?v=Li9k7zhUPhA


from flask import Flask, redirect, url_for, request, render_template
import random
import time

app = Flask(__name__, static_url_path='')

#http://www.google.com/search?q=variable&btnl


#gets user input from index.html and puts into "value" variable, redirects to "FirstPage" with variable "value"
@app.route('/SelectedNumber', methods=['POST'])
def SelectedNumber():
     value = request.form['selnum']
     if int(value) > 5:
         return "This value is larger than 5!"
     else:
       return redirect(url_for('FirstPage', value=value))

#loads loader.html with variable "value"
@app.route('/FirstPage/<value>')
def FirstPage(value):
   return render_template('loader.html', value=value)


#is redirected to by loader.html and redirects to "usenumber" with variable "value"
@app.route('/load/<value>')
def load(value):
   value = int(value)
   return redirect(url_for('usenumber', value=value))

#takes variable "value" and searches word.txt a the number of words (represented by "value")
#puts words into list and then puts words from list into google link with I'm Feeling Lucky filter
@app.route('/usenumber/<value>')
def usenumber(value):
   time.sleep(3)
   linelist = []
   randolist = []
   counter = int(value)
   with open('words.txt', 'rt') as wordfile:
       for line in wordfile:
           linelist.append(line)
       while counter != 0:
           testvar = random.choice(linelist).rstrip()
           randolist.append(testvar)
           counter = counter - 1
   test = '+'.join(randolist)
   return redirect("https://www.google.com/search?&btnI=1&q=%s" % (test), code=302)



#root of web server and gots to template (index.html)
@app.route('/')
def root():
  return render_template('index.html')



#main
if __name__ == '__main__':
  app.run(debug = True)