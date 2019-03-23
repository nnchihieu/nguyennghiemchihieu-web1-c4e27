from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about_me')
def about_me():
    about_mes = {
        "name" : "Nguyễn Nghiêm Chí Hiếu",
        "yob" : "2000",
        "school" : "PTIT",
        "hobbies" : "soccer, anime, kpop",
        "gender" : "male"}
    return render_template("am.html", about_me = about_mes)

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)


if __name__ == '__main__':
  app.run(debug=True)
 