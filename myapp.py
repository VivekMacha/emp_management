from flask import *
from DBM import addEmp,selectAllEmp,deleteEmp,selectEmpById,updateEmp,deleteEmp,name_pass
app=Flask(__name__,static_url_path='/static')

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/log",methods=["POST"])
def ulog():
    email=request.form["email"]
    password=request.form["passw"]
    d=name_pass()
    if((email,password)in d):
        return redirect("/emplist")
    else:
        return redirect("/reg")

@app.route("/home")
def home():
    return render_template("home.html")
   
@app.route("/reg")
def register():
    return render_template("register.html")

@app.route("/emplist")
def emplist():
    d=selectAllEmp()
    return render_template("info.html",elist=d)

@app.route("/addEmp",methods=["POST"])
def add_emp():
    ids=request.form["id"]
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    password=request.form["pass"]

    t=(ids,name,contact,email,password)
    addEmp(t)

    return redirect("/home")

@app.route("/update")
def update():
    
    return render_template("update.html")

@app.route("/updateEmp",methods=["POST"])
def update_emp():
    
    name=request.form["name"]
    contact=request.form["contact"]                 
    email=request.form["email"]                 
    passw=request.form["passw"]
    ids=request.form["id"]

    t=(name,contact,email,passw,ids)
    updateEmp(t)

    return redirect("/emplist")

@app.route("/deleteEmp")
def delete():
    ids=request.args.get('id')
    deleteEmp(ids)
    return redirect("/emplist")
if(__name__=="__main__"):
    app.run(debug=True)


















