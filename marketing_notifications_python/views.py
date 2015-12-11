from flask import request, flash
from marketing_notifications_python.forms import SendMessageForm
from marketing_notifications_python.models import init_models_module
from marketing_notifications_python.twilio import init_twilio_module
from marketing_notifications_python.view_helpers import twiml, view
from flask import Blueprint
from marketing_notifications_python.twilio.twilio_services import TwilioServices


def construct_view_blueprint(app, db):
    SUBSCRIBE_COMMAND = "subscribe"
    UNSUBSCRIBE_COMMAND = "unsubscribe"

    views = Blueprint("views", __name__)

    init_twilio_module(app)
    init_models_module(db)
    from marketing_notifications_python.models.subscriber import Subscriber

    @views.route('/', methods=["GET", "POST"])
    @views.route('/notifications', methods=["GET", "POST"])
    def notifications():
        form = SendMessageForm()
        if request.method == 'POST' and form.validate_on_submit():
            subscribers = Subscriber.query.filter(Subscriber.subscribed).all()
            if len(subscribers) > 0:
                flash('Messages on their way!')
                twilio_services = TwilioServices()
                for s in subscribers:
                    twilio_services.sendMessage(s.phone_number, form.message.data, form.imageUrl.data)
            else:
                flash('No subscribers found!')

            form.reset()
            return view('notifications', form)

        return view('notifications', form)

    @views.route('/message', methods=["POST"])
    def message():
        subscriber = Subscriber.query.filter(Subscriber.phone_number == request.form['From']).first()
        if subscriber is None:
            subscriber = Subscriber(phone_number=request.form['From'])
            db.session.add(subscriber)
            db.session.commit()
            output = "Thanks for contacting TWBC! Text 'subscribe' if you would like to receive updates via text message."
        else:
            output = _process_message(request.form['Body'], subscriber)
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

    return views
