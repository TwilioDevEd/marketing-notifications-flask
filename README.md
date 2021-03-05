# SMS Notifications with Twilio and Python | Flask

[![Build Status](https://github.com/TwilioDevEd/marketing-notifications-flask/workflows/Flask/badge.svg)](https://github.com/TwilioDevEd/marketing-notifications-flask/actions?query=workflow%3AFlask)

Use Twilio to create SMS notifications to keep your subscribers in the loop.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/marketing-notifications/python/flask)!

## Local Development

1. You will need to configure Twilio to send requests to your application when SMS are received.

   You will need to provision at least one Twilio number with SMS capabilities
   so the application's users can make property reservations. You can buy a
   number [right here](https://www.twilio.com/user/account/phone-numbers/search).
   Once you have a number you need to configure your number to work with your
   application.
   Open [the number management page](https://www.twilio.com/user/account/phone-numbers/incoming)
   and open a number's configuration by clicking on it.

   Remember that the number where you change the _SMS webhook_ must be the same one you set on the
   `TwilioPhoneNumber` setting.

   To start using `ngrok` in our project you'll have execute to the following
   line in the _command prompt_.

    ```
    ngrok http 8080 -host-header="localhost:8080"
    ```

   Keep in mind that our endpoint is:

    ```
    http://<your-ngrok-subdomain>.ngrok.io/message
    ```

1. Clone this repository and `cd` into it.

    ```
    git clone git@github.com:TwilioDevEd/marketing-notifications-python.git
    ```

1. Create and activate a new python3 virtual environment.

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

1. Install the requirements using [pip](https://pip.pypa.io/en/stable/installing/).

    ```bash
    pip install -r requirements.txt
    ```

1. Copy the `.env.example` file to `.env` and add the following values. Be sure to replace the placeholders and connection string with real information.

   ```
   SECRET_KEY = 'your_authy_secret_key'
   
   TWILIO_ACCOUNT_SID = '[your_twilio_account_sid]'
   TWILIO_AUTH_TOKEN = '[your_twilio_auth_token]'
   TWILIO_NUMBER = '[your_twilio_phone_number]'
   
   SQLALCHEMY_DATABASE_URI = 'sqlite://'
   ```

1. Create Flask application variables
   
   ```bash
   export FLASK_APP=notifications 
   export FLASK_ENV=development
   ```
1. Run the migrations.

   ```bash
   flask db upgrade
   ```

1. Start the development server.

    ```bash
    flask run
    ```

That's it!

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

    ```
    python test.py
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](LICENSE)
* Lovingly crafted by Twilio Developer Education.
