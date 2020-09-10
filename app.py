from flask import Flask ,render_template,redirect,url_for,request
app=Flask(__name__)
# @app.route("/redirect/<username>")
# def welcome(username):
# #return "<h1>Welcome to your first flask webpage</h1>"
#     #return render_template("web.html")
#     return "welcome %s" %username
@app.route("/<username>")
def welcome(username):
    return render_template("web.html", name=username)
@app.route("/aboutus")
def about():
    return "<h2> Go to Our youtube channel</h2>"

@app.route("/contactus")
def contact():
    return "<h3> Click to our Mail Id and Send your queries</h3>"

# @app.route("/profile")
# def profile():
#     return "<h4>See Our Facebook page and get the whole Employees details</h4>"

# how to pass variables

# @app.route("/profile/<username>")
# def profile(username):
#     return "Welcome %s" %username

# @app.route("/loginpage",methods=["post"])
# def login():
#     if request.method=="post":
#         name=request.form("nm")
#         return redirect(url_for('redirect',username=name))

if __name__=="__main__":
    app.run()













