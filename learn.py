from flask import Flask
from flask_restful import Api,Resource,reqparse,requests

app=Flask(__name__)
api=Api(app)

# lets create the object of names and access it
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
#         return {"name":name,"test":test}

# class Helloworld(Resource):
#     def get(self,name):
#         return names[name]
videos={}
video_put_args=reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of the video is required" , required=True)
video_put_args.add_argument("views", type=int, help="views of the video is required" , required=True)
video_put_args.add_argument("likes", type=int, help="likes of the video is required" , required=True)

def abort_if_video_id_desnt_exist(video_id):
    if video_id not in videos:
        abort(404,message="video could not find.....")

def abort_if_video_id_exist(video_id):
    if video_id in videos:
        abort(409,message="this video is already created")

class video(Resource):
    def get(self,video_id):
        abort_if_video_id_desnt_exist(video_id)
        return videos[video_id]

    def put(self,video_id):
        abort_if_video_id_exist(video_id)
        args=video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id],201 # here 201 is telling that your vides is created successfully
    
    def delete(self,video_id):
        abort_if_video_id_desnt_exist(video_id)
        del videos[video_id]
        return '',204



api.add_resource(video,'/video/<int:video_id>')
# api.add_resource(Helloworld,'/home/<string:name>/<int:test>')
#api.add_resource(Helloworld,'/home/<string:name>')
if __name__=='__main__':
    app.run(debug=True)