from flask import flash, request, Flask, Response
from .forms import SendMessageForm
from .database import db
from .models import Subscriber
from .view_helpers import twiml, view
from .twilio.twilio_services import TwilioServices


def init_views(app: Flask) -> None:

    twilio_services = TwilioServices(
        app.config.get('TWILIO_ACCOUNT_SID'), app.config.get('TWILIO_AUTH_TOKEN')
    )

    @app.route('/', methods=["GET", "POST"])
    @app.route('/notifications', methods=["GET", "POST"])
    def notifications() -> Response:
        form = SendMessageForm()
        if request.method == 'POST' and form.validate_on_submit():
            subscribers = Subscriber.query.filter(Subscriber.subscribed).all()
            if subscribers:
                flash('Messages on their way!')
                from_ = app.config.get('TWILIO_PHONE_NUMBER')
                for s in subscribers:
                    twilio_services.send_message(
                        s.phone_number, from_, form.message.data, form.imageUrl.data
                    )
            else:
                flash('No subscribers found!')

            form.reset()
            return view('notifications', form)

        return view('notifications', form)

    @app.route('/message', methods=["POST"])
    def message() -> Response:
        subscriber = Subscriber.query.filter(
            Subscriber.phone_number == request.form['From']
        ).first()
        sms_body = request.form['Body']
        if subscriber is None:
            subscriber = Subscriber(phone_number=request.form['From'])
            db.session.add(subscriber)
            output = "Thanks for contacting TWBC! "
        elif sms_body.lower() not in ('subscribe', 'unsubscribe'):
            output = "Unrecognized command! "
        else:
            output = ""
        if sms_body.lower() == 'subscribe':
            if not subscriber.subscribed:
                subscriber.subscribed = True
                output += "You are now subscribed for updates."
            else:
                output += "You are already subscribed for updates."
        elif sms_body.lower() == 'unsubscribe':
            if subscriber.subscribed:
                subscriber.subscribed = False
                output += (
                    "You have unsubscribed from notifications. "
                    "Text 'subscribe' to start receiving updates again."
                )
            else:
                output += "You are not subscribed for updates."
        else:
            output += (
                "Text 'subscribe' if you would like to receive updates via text message"
                " or 'unsubscribe' to stop receiving them."
            )

        db.session.commit()

        return twiml(twilio_services.respond_message(output))
