from flask_wtf import Form
from werkzeug.datastructures import MultiDict
from wtforms import TextField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SendMessageForm(Form):
    message = TextField('Message', validators=[DataRequired(message="Message is required")])
    imageUrl = TextField('Image URL', validators=[DataRequired("Image URL is required")])

    def reset(self):
        blankData = MultiDict([('message', ''), ('imageUrl', '')])
        self.process(blankData)


class MessageForm(Form):
    sender = TextField('From')
    body = TextField('Body')
