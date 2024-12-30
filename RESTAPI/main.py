from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Universe!</p>"

@app.route("/armstrong/<int:n>")
def is_armstrong(n):
    copy_n=n
    total = 0
    for digit in str(n):
        total += int(digit) ** len(str(n))
    if total==copy_n:
        result={
            "Number":copy_n,
            "Armstrong":"True",
            "Server IP":"122.23.1.3"
        }
    else:
        result={
            "Number":copy_n,
            "Armstrong":"False",
            "Server IP":"122.23.1.3"  
        }
    return jsonify(result)    

if __name__=="__main__":
    app.run(debug=True)
