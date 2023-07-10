from flask import Flask,make_response,request
import json
app = Flask(__name__)

posts=[]

@app.route('/',methods=['GET'])
def index():
    response=make_response("Instagram")
    return response

@app.route('/createpost',methods=['POST'])
def create_post():
    post=request.get_json()
    posts.append(post)
    return 'Successfully created post!'

@app.route('/post',methods=['GET'])
def get_post():
    return json.dumps(posts)

@app.route('/delete/<id>',methods=['DELETE'])
def delete_post(id):
    for post in posts:
        if post["id"] == int(id):
            posts.remove(post)
            return 'Successfully deleted post!'
        else:
            return 'Error deleting post'

if __name__ == '__main__':
    app.run(port=8080)
