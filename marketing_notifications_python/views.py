from flask import render_template, redirect, url_for, request, session, flash
from marketing_notifications_python import app
import twilio.twiml
from marketing_notifications_python.view_helpers import twiml


@app.route('/')
def home():
    return "marketing_notifications_python"

