from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def users(username):
    users={
        "hieu" : {
            "name" : "Nguyễn Nghiêm Chí Hiếu",
            "age" : "19",
            "school" : "PTIT",
            "hobbies" : "soccer, anime, kpop",
            "gender" : "male"
            },
        "duy" : {
            "name" : "Phạm Khánh Duy",
            "age" : "19",
            "school" : "PTIT",
            "hobbies" : "soccer, game",
            "gender" : "male"
            },
        "lan" : {
            "name" : "Võ Ngọc Lân",
            "age" : "19",
            "school" : "PTIT",
            "hobbies" : "game",
            "gender" : "male"}
    }   
    if username in users: 
        user=users[username]
        return render_template('user.html',user=user)
    else:
        return "user not found"

if __name__ == '__main__':
  app.run(debug=True)