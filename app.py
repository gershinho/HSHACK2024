
from flask import Flask, render_template, request,redirect, url_for, jsonify,send_file

import sqlite3


app = Flask(__name__)

conn = sqlite3.connect('study_groups.db', check_same_thread=False)
c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS studygroup (
#               name TEXT,
#               subject TEXT,
#               difficulty TEXT,
#               size INTEGER,
#               description TEXT
#               )""")


conn.commit()





@app.route("/", methods=['GET'])
def home():

    c.execute("SELECT * FROM studygroup")
    rows = c.fetchall()
    
    print()
    print()
    print(rows)
    print()
    print()

    
    # Retrieve values from the form submission or use defaults
    group_size = request.args.get('groupsize-input', default="4")
    subject = request.args.get('subjects', default="").upper()
    difficulty = request.args.get('difficulty', default="").upper()

    
    c.execute("SELECT name, subject, difficulty, size, description FROM studygroup")

    rows1 = c.fetchall()

    all_groups = {}
    for group in rows1:
        group_name = group[0]
        all_groups[group_name] = {
            "Subject": group[1],
            "Difficulty": group[2],
            "GroupSize": group[3],
            "Description": group[4]
        }
  


       # Query the database for matching groups
    c.execute("""
        SELECT * FROM studygroup
        WHERE upper(subject) = ?
        AND upper(difficulty) = ?
        AND size = ?
    """, (subject, difficulty, group_size))
    rows2 = c.fetchall()
   


    
    matching_groups = {}
    for matching_group in rows2:
        group_name = matching_group[0]
        matching_groups[group_name] = {
            "Subject": matching_group[1],
            "Difficulty": matching_group[2],
            "GroupSize": matching_group[3],
            "Description": matching_group[4]
        }
  

    


    
    # Assuming 'groups' is a dictionary you've defined elsewhere that holds group details
    return render_template('home.html', groups=matching_groups, all_groups = all_groups, subject=subject, difficulty=difficulty)

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
        c.execute("INSERT INTO studygroup VALUES (?, ?, ?, ?, ?)",
                      (groupName, subject, difficulty, groupSize, description))
        conn.commit()
         
        
    
      

    if not groupName or not description:
        
        error_message = "Please fill in all the fields."
        return render_template('create.html', error_message=error_message)




    return render_template('create.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)