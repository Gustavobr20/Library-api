from db import db
from flask import Flask


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    status = db.Column(db.String(10), nullable=False)

    def __init__(self, title, status):
        self.title = title
        self.status = status

    def __repr__(self):
        return f'BookModel(title={self.title}, status={self.status})'

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
        }

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
