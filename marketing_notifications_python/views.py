from flask import render_template, redirect, url_for, request, session, flash
from marketing_notifications_python import app
from marketing_notifications_python.forms import SendMessageForm
from marketing_notifications_python.models import Subscriber
from marketing_notifications_python.twilio.message_sender import MessageSender
from marketing_notifications_python.view_helpers import twiml, view


@app.route('/', methods=["GET", "POST"])
@app.route('/notifications', methods=["GET", "POST"])
def register():
    form = SendMessageForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            subscribers = Subscriber.query.filter(Subscriber.suscribed == True);
            if subscribers.count() > 0:
                flash('Messages on their way!')
                sender = MessageSender()
                for s in subscribers:
                    sender.send(s.phone_number, form.message, form.imageUrl)
            else:
                flash('No subscribers found!')

    return view('notifications', form)
