from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable= False)
    author = db.Column(db.String(200), nullable= False)
    description = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.title}-{self.author}"

@app.route("/")
def home():
    todo = Todo(title="Play Pubg", author="Neeraj", description="We will play at 9 sharp")
   
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)

if __name__ == "__main__":
    app.run(debug=True)