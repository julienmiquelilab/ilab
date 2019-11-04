from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xxxxxxxxxxxxxxx'
app.config['MYSQL_DB'] = 'bank'
mysql = MySQL(app)
@app.route('/', methods=['GET', 'POST'])
def index():
        return "hello ilabs geeks ! "
@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == "POST":
                details = request.form
                firstName = details ['fname']
                cur = mysql.connection.cursor()
                #cur.execute("INSERT INTO users(name) VALUES (%s)", [firstName])
                #mysql.connection.commit()
                cur.execute("SELECT COUNT(*) from users where name= (%s)",[firstName] )
                result=cur.fetchone()
                
                cur.close()
                if str(result) == '(0,)':
                        return 'unknown user : ' +  firstName
                        
                return 'Welcome : ' +  firstName + ' ' + str(result)
                 
        return render_template('index.html')
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80)
