from flask import Flask, render_template, jsonify

Jobs = [{
    'id':1,
    'title':'Data Analyst',
    'location': 'Bengaluru',
    'salary': 'rs 10,00,000'
},
{
    'id':2,
    'title':'Data Scientist',
    'location': 'Delhi',
    'salary': 'rs 15,00,000'
},
{
    'id':3,
    'title':'Front end dev',
    'location': 'Remote',
},
{
    'id':4,
    'title':'Backend',
    'location': 'Remote',
    'salary': 'rs 20,00,000'
}

]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', jobs= Jobs)



@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)



if(__name__ == '__main__'):
    app.run(host="0.0.0.0", debug=True)