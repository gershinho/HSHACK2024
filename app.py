
from flask import Flask, render_template, request,redirect, url_for, jsonify,send_file



app = Flask(__name__)


groups = []

@app.route("/")
def home(): 

    groupSize = int(request.args.get('groupsize-input', 50000000))
    difficulty = (request.args.get('subject'))
    subject = (request.args.get('difficulty'))
    print(groupSize)
    print(difficulty)
    print(subject)
    return render_template('home.html', groups=groups)
    

@app.route("/create")
def create_group():
    
    groupName = (request.args.get('groupName'))
    subject = (request.args.get('subjects'))
    difficulty2 = (request.args.get('levels'))
    groupSize = (request.args.get('groupSize'))
    description = (request.args.get('paragraph'))

    if  groupName and description:  
            
    
        groups.append({
                "groupName": groupName,
                "subject": subject,
                "difficulty": difficulty2,
                "groupSize": groupSize,
                "description": description
            })
        print(groupName, subject, difficulty2, groupSize, description)

    if not groupName or not description:  
        error_message = "Please fill in all the fields."
        return render_template('create.html', error_message=error_message)




    return render_template('create.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)