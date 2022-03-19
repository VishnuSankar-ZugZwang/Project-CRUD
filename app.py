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
        Question = request.form.get('Question')
        user = db.User()
        user.name = name
        user.email = email
        user.Id = Id
        user.Question = Question
        user.save()
        flash("Created Successfully")
    return render_template('create.html')
@app.route('/Read',methods=['POST',"GET"])
def read():
    users = db.User.objects()
    return render_template('read.html',users=users)
@app.route('/View',methods=['POST',"GET"])
def view():
    users = db.User.objects()
    return render_template('view.html',users=users)

@app.route('/list',methods=['POST',"GET"])
def list():
    users = db.User.objects()
    return render_template('list.html',users=users)
@app.route('/Delete',methods=['POST',"GET"])
def delete():
    users1 = db.User.objects()
    if request.method  == "POST":
        name = request.form.get('name')
        user = db.User.objects(name=name)
        user.delete()
        users1 = db.User.objects()
    return render_template('delete.html',res=users1)
@app.route('/Update',methods=['POST',"GET"])
def update():
    users = db.User.objects()
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        Id = request.form.get('Id')
        user = db.User.objects(name=name,email=email,Id=Id)
        user.update(name=name,email=email,Id=Id)
        user1 = db.User.objects()
        flash("Updated Successfully")
    return render_template("update.html",res=users)    




if __name__ == "__main__":
    app.run(debug=True) 
