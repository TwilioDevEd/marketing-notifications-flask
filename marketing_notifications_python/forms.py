from flask_wtf import Form
from werkzeug.datastructures import MultiDict
from wtforms import TextField
from wtforms.validators import DataRequired


class SendMessageForm(Form):
    message = TextField('Message', validators=[DataRequired(message="Message is required")])
    imageUrl = TextField('Image URL', validators=[DataRequired("Image URL is required")])

    def reset(self):
        blankData = MultiDict([('message', ''), ('imageUrl', '')])
        self.process(blankData)
