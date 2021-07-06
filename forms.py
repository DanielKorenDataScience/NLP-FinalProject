from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Length#, FileRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class ChatForm(FlaskForm):
    user_msg = StringField('User Input', render_kw={'autofocus': True})
    run_bot = SubmitField('Ask Bot')
    google = SubmitField('G')
    debug = SubmitField('Debug')
    run_test = SubmitField('Run Test')
    send_log = SubmitField('Send Log')
