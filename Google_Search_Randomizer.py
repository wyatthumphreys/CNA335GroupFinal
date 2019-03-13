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
            testvar = random.choice(linelist)
            randolist.append(testvar)
            counter = counter - 1
            test = randolist[0]
            return test


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
