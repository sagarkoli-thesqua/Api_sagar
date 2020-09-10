
from flask import Flask,jsonify
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome here for creating your first RestApi"

@app.route("/armstrong/<int:n>")
def armstrong(n):
    sum = 0
    order= len(str(n))
    copy_n=n
    while(n>0):
        digit=n%10
        sum+=digit**order
        n=n//10
    if(sum==copy_n):
        print(f"{copy_n} is an armstrong number")
        result={
           "Number" : copy_n,
           "Armstrong":True,
           "Server ip" :"128.45.1"
        }
    else:
        result={
            "Number":copy_n,
            "Armstrong":False,
            "Server ip":"125.25.1"
        }
    return jsonify(result)
    

if __name__=="__main__":
    app.run(debug=True)