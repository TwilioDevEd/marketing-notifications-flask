from flask import request, flash
from marketing_notifications_python import app, db, SUBSCRIBE_COMMAND, UNSUBSCRIBE_COMMAND
from marketing_notifications_python.forms import SendMessageForm, MessageForm
from marketing_notifications_python.models import Subscriber
from marketing_notifications_python.twilio.twilio_services import TwilioServices
from marketing_notifications_python.view_helpers import twiml, view


@app.route('/', methods=["GET", "POST"])
@app.route('/notifications', methods=["GET", "POST"])
def notifications():
    form = SendMessageForm()
    if request.method == 'POST' and form.validate_on_submit():
        subscribers = Subscriber.query.filter(Subscriber.subscribed).all()
        if subscribers is not None:
            flash('Messages on their way!')
            twilio_services = TwilioServices()
            for s in subscribers:
                twilio_services.sendMessage(s.phone_number, form.message.data, form.imageUrl.data)
        else:
            flash('No subscribers found!')

        form.reset()
        return view('notifications', form)

    return view('notifications', form)


@app.route('/message', methods=["POST"])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        subscriber = Subscriber.query.filter(Subscriber.phone_number == form.sender).first
        if subscriber is None:
            subscriber = Subscriber(phone_number=form.sender)
            db.session.add(subscriber)
            db.session.commit()
            output = "Thanks for contacting TWBC! Text 'subscribe' if you would like to receive updates via text message."
        else:
            output = _process_message(form, subscriber)
            db.session.commit()

    twilio_services = TwilioServices()
    return twiml(twilio_services.respond_message(output))


def _process_message(form, subscriber):
    output = "Sorry, we don't recognize that command. Available commands are: 'subscribe' or 'unsubscribe'."

    if message.startswith(SUBSCRIBE_COMMAND) or message.startswith(UNSUBSCRIBE_COMMAND):
        subscriber.subscribed = message.startswith(SUBSCRIBE_COMMAND)

        if subscriber.subscribed:
            output = "You have unsubscribed from notifications. Text 'subscribe' to start receiving updates again"
        else:
            output = "You are now subscribed for updates."

    return output
