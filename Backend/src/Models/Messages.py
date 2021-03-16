from src.extension import db
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body=db.Column(db.Text,nullable=False)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow,index=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',back_populates='messages')
