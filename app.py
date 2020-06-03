from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def convert_Roman():
number=request.form['integer']
    dict={1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L",40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    roman=""
    for key in dict.keys():
        count=number//key
        roman+=dict[key]*count
        number-=key*count
    return roman
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)