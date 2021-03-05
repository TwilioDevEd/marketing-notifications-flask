from flask_wtf import FlaskForm
from werkzeug.datastructures import MultiDict
from wtforms import StringField
from wtforms.validators import DataRequired


class SendMessageForm(FlaskForm):
    message = StringField(
        'Message', validators=[DataRequired(message="Message is required")]
    )
    imageUrl = StringField(
        'Image URL', validators=[DataRequired("Image URL is required")]
    )

    def reset(self):
        blank_data = MultiDict([('message', ''), ('imageUrl', '')])
        self.process(blank_data)
