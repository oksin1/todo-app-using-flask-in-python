from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")
#the above command represents where the html file is stored as we can see in the folders

todoa = [{"task":"Sample Todo", "done":False}]



@app.route("/") #it's gonna do what it has to 
def index():
    return render_template("index.html", todoa=todoa)


@app.route("/add",methods=["POST"])
def add():
    todo  = request.form['todo']
    todoa.append({"task":todo,"done":False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET","POST"])
def edit(index):
    todo = todoa[index]
    if request.method =="POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)
    

@app.route("/check/<int:index>")
def check(index):
    todoa[index]['done'] = not todoa[index]['done']
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del todoa[index]
    return redirect(url_for("index")) 

if __name__=='__main__': # for the function
    app.run(debug=True) # to run the program in the debug mode