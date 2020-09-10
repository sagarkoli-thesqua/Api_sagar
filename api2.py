from flask import Flask,jsonify,request

app=Flask(__name__)

# @app.route("/",methods=['GET','POST'])
# def welcome():
#     if(request.method=='GET'):
#         data="hello guys how are you"
#         return jsonify({'data':data})

@app.route("/",methods=['GET','POST'])
def index():
    if(request.method=='POST'):
        some_json=request.get_json()
        return jsonify({'you sent':some_json})

    else:
        return jsonify({'about':'Hello world'})

@app.route("/home/<int:n>",methods=['GET'])
def square(n):
    return jsonify({'square':n**2})


if __name__=='__main__':
    app.run(debug=True) 