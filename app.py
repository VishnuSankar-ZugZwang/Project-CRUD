from flask import Flask,render_template,request
from flask.helpers import flash
import db, os, re
app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config["MONGO_DBNAME"] = 'DB1'



@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        Id = request.form.get('Id')
        Question = request.form.get('Questions')
        user = db.User()
        user.name = name
        user.email = email
        user.Id = Id
        user.Question = Question
        user.save()
        flash("Created Successfully")
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True) 
