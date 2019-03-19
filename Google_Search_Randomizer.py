#sources: https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask
#https://github.com/dwyl/english-words
#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
#https://productforums.google.com/forum/#!topic/websearch/pywUIBP6C20
from flask import Flask, redirect, url_for, request, render_template
import random
import time

app = Flask(__name__, static_url_path='')

#http://www.google.com/search?q=variable&btnl



@app.route('/SelectedNumber', methods=['POST'])
def SelectedNumber():
     value = request.form['selnum']
     if int(value) > 5:
         return "This value is larger than 5!"
     else:
       return redirect(url_for('FirstPage', value=value))


@app.route('/FirstPage/<value>')
def FirstPage(value):
   return render_template('loader.html', value=value)



@app.route('/load/<value>')
def load(value):
   value = int(value)
   return redirect(url_for('usenumber', value=value))


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



#root of web server and gots to template (login.html)
@app.route('/')
def root():
  return render_template('index.html')



#main
if __name__ == '__main__':
  app.run(debug = True)