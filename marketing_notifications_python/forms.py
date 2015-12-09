from flask_wtf import Form
from wtforms import TextField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SendMessageForm(Form):
    message = TextField(
        'Message',
        validators=[DataRequired(message="Message is required")]
    )
    imageUrl = TextField(
        'Image URL',
        validators=[DataRequired("Image URL is required")]
    )
