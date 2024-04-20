
from flask import Flask, render_template, request,redirect, url_for, jsonify,send_file



app = Flask(__name__)


groups = {}

@app.route("/", methods=['GET'])
def home():
    # Retrieve values from the form submission or use defaults
    group_size = request.args.get('groupsize-input', default="4")
    subject = request.args.get('subjects', default="").upper()
    difficulty = request.args.get('difficulty', default="").upper()

    # Print to console for debugging
   

    matching_groups = {
        name: details
        for name, details in groups.items()
        if details['Subject'].upper() == subject
           and details['Difficulty'].upper() == difficulty
           and str(details['GroupSize']) == group_size  # Ensure the group size is compared as a string
    }


    
    # Assuming 'groups' is a dictionary you've defined elsewhere that holds group details
    return render_template('home.html', groups=matching_groups, subject=subject, difficulty=difficulty)

@app.route("/join")
def join():
    return render_template('index.html')


@app.route("/create")
def create_group():
    
    groupName = (request.args.get('groupName'))
    subject = (request.args.get('subjects'))
    difficulty = (request.args.get('difficulty'))
    groupSize = (request.args.get('groupsize-input'))
    description = (request.args.get('paragraph'))
   
    if  groupName and description:  
            
    
        groups[groupName] = {
            "Subject": subject,
            "Difficulty": difficulty,
            "GroupSize": groupSize,
            "Description": description
        }

    if not groupName or not description:  
        error_message = "Please fill in all the fields."
        return render_template('create.html', error_message=error_message)




    return render_template('create.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)