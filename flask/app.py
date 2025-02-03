# importations
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# other code
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# class of todo to make data structure
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"
    
# endpoints
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("home"))

    allTodo = Todo.query.all()
    return render_template("index.html", todos=allTodo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/delete/<int:sno>')
def delete(sno):
    if sno:
        delete_todo = Todo.query.filter_by(sno=sno).first()
        db.session.delete(delete_todo)
        db.session.commit()
        return redirect(url_for('home'))
    
@app.route('/update/<int:sno>', methods=["GET", "POST"])
def update(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    if request.method == "POST":
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('update.html', todo = todo)

# running the files
if __name__ == "__main__":
    # Initialize the database and create tables
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=80, host="localhost")