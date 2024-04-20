from flask import Flask, render_template, request,jsonify,send_file


app = Flask(__name__)


@app.route("/")
def home(): 
    price = int(request.args.get('groupsize-input', 50000000))
    distance = int(request.args.get('dist-input', 500))
    difficulty = (request.args.get('subject'))
    subject = (request.args.get('difficulty'))
    print(difficulty)
    print(subject)
    return render_template('home.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)