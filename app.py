
from flask import Flask, render_template, request,redirect, url_for, jsonify,send_file

import sqlite3


app = Flask(__name__)

try:
    conn = sqlite3.connect('study_groups.db', check_same_thread=False)
    c = conn.cursor()
except Exception as e:
    print(f"Database connection failed: {e}")
    exit(1)









@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        data = request.form
        group_size = data.get('groupsize-input')
        subject = data.get('subjects')
        difficulty = data.get('difficulty')
        
        # Query the database for matching groups
        conn = sqlite3.connect('study_groups.db', check_same_thread=False)
        c = conn.cursor()
        c.execute("""
            SELECT * FROM studygroup
            WHERE upper(subject) = ?
            AND upper(difficulty) = ?
            AND size = ?
        """, (subject.upper(), difficulty.upper(), group_size))
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
        
        # Close cursor and connection after fetching results
        c.close()
        conn.close()
        
        
        return render_template('group_list.html', groups=matching_groups)
    
    else:  # For GET requests or initial page load
        conn = sqlite3.connect('study_groups.db', check_same_thread=False)
        c = conn.cursor()
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
        
        # Close cursor and connection after fetching results
        c.close()
        conn.close()
        
        # Render home.html with all groups
        return render_template('home.html', groups=all_groups)

    

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