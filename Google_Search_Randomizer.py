from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, static_url_path='')


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
