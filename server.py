from flask import Flask, render_template
app = Flask(__name__)


@app.route( '/', methods=['GET'] )
def index():
    return render_template( 'index.html', valY= 8,valX= 8, color1="red", color2="black")

@app.route( '/4', methods=['GET'] )
def line4():
    return render_template( 'index.html', valY= 4,valX= 8, color1="red", color2="black")

@app.route('/<num>/<num2>') 
def multiplyTable(num, num2):
    print (num)
    print (num2)
    return render_template( 'index.html', valY= int(num),valX= int(num2), color1="red", color2="black")

@app.route('/<num>/<num2>/<color1>') 
def color1(num, num2, color1):
    print (num)
    print (num2)
    print (color1)
    return render_template( 'index.html', valY= int(num),valX= int(num2), color1=color1, color2="black")

@app.route('/<num>/<num2>/<color1>/<color2>') 
def color2(num, num2, color1, color2):
    print (num)
    print (num2)
    print (color1)
    print (color2)
    return render_template( 'index.html', valY= int(num),valX= int(num2), color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)