# SMS Notifications with Twilio and Python | Flask

[![Build Status](https://travis-ci.org/TwilioDevEd/marketing-notifications-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/marketing-notifications-flask)

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

   ![Configure Voice](http://howtodocs.s3.amazonaws.com/twilio-number-config-all-med.gif)

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

1. Create a new virtual environment.

    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```
        mkvirtualenv account-verification-flask
        ```

1. Install the requirements using [pip](https://pip.pypa.io/en/stable/installing/).

    ```
    pip install -r requirements.txt
    ```

1. Edit the following keys/values for the `config.py` file inside the  `marketing-notifications-python/` directory. Be sure to replace the place holders and connection string with real information.

    ```
  SECRET_KEY = 'your_authy_secret_key'

  TWILIO_ACCOUNT_SID = '[your_twilio_account_sid]'
  TWILIO_AUTH_TOKEN = '[your_twilio_auth_token]'
  TWILIO_NUMBER = '[your_twilio_phone_number]'

  SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ```

1. Run the migrations.

    ```
    python manage.py db upgrade
    ```

1. Start the development server.

    ```
    python manage.py runserver
    ```

That's it!

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

    ```
    $ coverage run test.py
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
