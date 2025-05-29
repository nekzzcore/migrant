from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Student {}>'.format(self.name)

def seed_data():
    students = [
        Student(name='Алексей', gender='Мужской', age=18, hair_color='<Брюнет', eye_color='Серо-голубой'),
        Student(name='АРина', gender='Женский', age=19, hair_color='Брюнетка', eye_color='Зелёный'),
        Student(name='Потап', gender='Мужской', age=21, hair_color='Черный', eye_color='зелёный'),
        Student(name='Новелла', gender='Женский', age=19, hair_color='Блонд', eye_color='Голубой'),
        Student(name='Левелап', gender='Мужской', age=20, hair_color='Черный', eye_color='Карий')
    ]
    db.session.bulk_save_objects(students)
    db.session.commit()
    print("база данных заполнена")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
