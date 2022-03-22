from flask import Flask,render_template,request
from flask.helpers import flash
import db, os, re
app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config["MONGO_DBNAME"] = 'DB1'



@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        Id = request.form.get('Id')
        Question = request.form.get('Question')
        user = db.User()
        user.Id = Id
        user.Question = Question
        user.save()
        flash("Created Successfully")
    return render_template('create.html')
@app.route('/Read',methods=['POST',"GET"])
def read():
    users = db.User.objects()
    return render_template('read.html',users=users)

@app.route('/Read1',methods=['POST',"GET"])
def read1():
    users = db.User.objects()
    return render_template('read1.html',users=users)
@app.route('/Read2',methods=['POST',"GET"])
def read2():
    users = db.User.objects()
    return render_template('read2.html',users=users)
@app.route('/Read3',methods=['POST',"GET"])
def read3():
    users = db.User.objects()
    return render_template('read3.html',users=users)
@app.route('/Read4',methods=['POST',"GET"])
def read4():
    users = db.User.objects()
    return render_template('read4.html',users=users)
@app.route('/Read5',methods=['POST',"GET"])
def read5():
    users = db.User.objects()
    return render_template('read5.html',users=users)
@app.route('/Read6',methods=['POST',"GET"])
def read6():
    users = db.User.objects()
    return render_template('read6.html',users=users)
@app.route('/Read7',methods=['POST',"GET"])
def read7():
    users = db.User.objects()
    return render_template('read7.html',users=users)
@app.route('/Read8',methods=['POST',"GET"])
def read8():
    users = db.User.objects()
    return render_template('read.html',users=users)
@app.route('/Read9',methods=['POST',"GET"])
def read9():
    users = db.User.objects()
    return render_template('read9.html',users=users)

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
        Id = request.form.get('Id')

        user = db.User.objects(Id=Id)
        user.delete()
        users1 = db.User.objects()
        flash("Deleted Successfully")
    return render_template('delete.html',res=users1)
@app.route('/Update',methods=['POST',"GET"])
def update():
    users = db.User.objects()
    if request.method == "POST":
        Id = request.form.get('Id')
        user = db.User.objects(Id=Id)
        user.update(Id=Id)
        user1 = db.User.objects()
        flash("Updated Successfully")
    return render_template("update.html",res=users)    




if __name__ == "__main__":
    app.run(debug=True) 
