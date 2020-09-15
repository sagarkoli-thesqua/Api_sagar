from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse

app=Flask(__name__)
api=Api(app)

names ={
     "Sagar":{
           "name":"Sagar koli",
           "Age" :23,
           "Salary":50000,
           "Education":"B.Tech"
     },
     "yeshwant":{
         "name":"yeshwant Singh",
         "Age" :25,
         "Salary":60000,
         "Education":"B.Tech"
     },
     "Arun":{
         "Name":"Arun Kumar Shokeen",
         "Age" :24,
         "Salary":50000,
         "Education":"B.Tech"
     }
    }
# class Helloworld(Resource):
#     def get(self,name):
#         return names[name]

    # def post(self):
    #    #some_json=request.get_json()
    #     return {'you sent':"this is my file"},201

videos={}
video_put_args=reqparse.RequestParser()
video_put_args.add_argument("name" ,type="str",help="name of the video is required" , required=True)
video_put_args.add_argument("likes" ,type="int",help="likes of the video is required" , required=True)
video_put_args.add_argument("views" ,type="int",help="views of the video is required" , required=True)

def abort_if_video_id_deosnt_exist(video_id):
    if video_id not in videos:
        abort(404,message="could not find video")

def abort_if_video_id_exist(video_id):
    if video_id in videos:
        abort(409,message="video is already exist")

class video(Resource):
    def get(self,video_id):
        abort_if_video_id_deosnt_exist(video_id)
        return videos[video_id]
    
    def put(self,video_id):
        args=video_put_args.parse_args()
        abort_if_video_id_exist(video_id)
        videos[video_id]=args
        return videos[video_id],201

    def delete(self,video_id):
        abort_if_video_id_deosnt_exist(video_id)
        del videos[video_id]
        return '',204

#api.add_resource(Helloworld,'/helloworld/<string:name>')
api.add_resource(video,'/video/<int:video_id>')

if __name__=='__main__':
   app.run(debug=True)
