from extensions import db


class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.String(50), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    method = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    config = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(2), nullable=False)
