from flask import Flask, redirect, url_for, request, render_template
import random

app = Flask(__name__, static_url_path='')

linelist=[]
randolist=[]
counter=4

#http://www.google.com/search?q=variable&btnl

@app.route('/usenumber', methods=['POST'])
def usenumber(counter, linelist, randolist):
    with open('words.txt', 'rt') as wordfile:
        for line in wordfile:
            linelist.append(line)
        while counter != 0:
            testvar = random.choice(linelist)
            randolist.append(testvar)
            counter = counter - 1
            print(randolist)
            

@app.route('/SelectedNumber', methods=['GET'])
def SelectedNumber():
       user = request.args.get('szip')
       return redirect(url_for('searchzipcode', searchZIP=user))


#root of web server and gots to template (login.html)
@app.route('/')
def root():
   return render_template('index.html')

#main
if __name__ == '__main__':
   app.run(debug = True)
