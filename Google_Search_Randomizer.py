#sources: https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask
#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
#https://productforums.google.com/forum/#!topic/websearch/pywUIBP6C20
from flask import Flask, redirect, url_for, request, render_template
import random

app = Flask(__name__, static_url_path='')

#http://www.google.com/search?q=variable&btnl

@app.route('/usenumber/ <number>')
def usenumber(number):
    linelist = []
    randolist = []
    counter = int(number)
    with open('words.txt', 'rt') as wordfile:
        for line in wordfile:
            linelist.append(line)
        while counter != 0:
            testvar = random.choice(linelist).rstrip()
            randolist.append(testvar)
            counter = counter - 1
    test = '+'.join(randolist)
    return redirect("http://www.google.com/search?sourceid=navclient&btnI=1&q=%s" % (test), code=302)



@app.route('/SelectedNumber', methods=['POST'])
def SelectedNumber():
      value = request.form['selnum']
      return redirect(url_for('usenumber', number=value))


#root of web server and gots to template (login.html)
@app.route('/')
def root():
   return render_template('index.html')

#main
if __name__ == '__main__':
   app.run(debug = True)