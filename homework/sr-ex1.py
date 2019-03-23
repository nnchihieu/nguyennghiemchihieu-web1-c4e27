from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi1/<int:weight>/<int:height>')
def bmi1(weight, height):
    height = height/100
    bmi = weight/(height*height)
    if (bmi < 16):
        return ("bmi: " + str(bmi) + "=> Severely underweight")
    elif (bmi < 18.5):
        return ("bmi: " + str(bmi) + "=> Underweight")    
    elif (bmi < 25):
        return ("bmi: " + str(bmi) + "=> Normal")
    elif (bmi < 30):
        return ("bmi: " + str(bmi) + "=> Overweight")
    else:
        return ("bmi: " + str(bmi) + "=> Obese")    


@app.route('/bmi2/<int:weight>/<int:height>')
def bmi2(weight, height):
    height = height/100
    bmi = weight/(height*height)
    if (bmi < 16):
        cond = ("bmi: " + str(bmi) + "=> Severely underweight")
    elif (bmi < 18.5):
        cond = ("bmi: " + str(bmi) + "=> Underweight")    
    elif (bmi < 25):
        cond = ("bmi: " + str(bmi) + "=> Normal")
    elif (bmi < 30):
        cond = ("bmi: " + str(bmi) + "=> Overweight")
    else:
        cond = ("bmi: " + str(bmi) + "=> Obese")   
    return render_template('bmi.html', cond = cond) 

if __name__ == '__main__':
  app.run(debug=True)
 