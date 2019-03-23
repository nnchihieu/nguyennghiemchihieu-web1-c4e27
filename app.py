from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello c4e27'

@app.route('/say-hi/<name>')
def sayhi(name):
    return 'Hi' + name

@app.route('/say-hi/<sum>/<int:a>/<int:b>')
def sum(a, b):
    return str(a+b)

@app.route('/poem')
def poem():
    poems = [
        {
        "title" : "Thơ con cóc",
        "content" : "Hôm nay trăng lên cao quá",
        "author" : "Huế",
        "gender" : "female",
        },
        {
        "title" : "Thơ con ếch",
        "content" : "Để thằng bán đồ giữ mất tuổi thanh xuân",
        "author" : "Trường",
        "gender" : "male",
        },
    ]


    return render_template("poem.html",
                            poems=poems)
    

if __name__ == '__main__':
  app.run(debug=True)
 