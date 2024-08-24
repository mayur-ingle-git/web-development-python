from flask import Flask, render_template, jsonify

app = Flask(__name__)

projects = [
  {
    'id': 1,
    'title': 'Portfolio Website',
    'description': 'This is the first project',
    'image': 'static/images/pic1.jpg'
  },
  {
    'id': 2,
    'title': 'Voice Assistant',
    'description': 'This is the first project',
    'image': 'static/images/pic1.jpg'
  },
  {
  'id': 3,
  'title': 'Investment Predictions',
  'description': 'This project inclides web-scrapping using Beautiful soup',
  'image': 'static/images/pic1.jpg'
  }

]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         projects=projects)

@app.route("/projects")
def list_projects():
  return jsonify(projects)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  