import flask
from flask import url_for, redirect, render_template


def twiml(resp):
    resp = flask.Response(str(resp))
    resp.headers['Content-Type'] = 'text/xml'
    return resp


def view(view_name, form=None):
    return render_template("{0}.html".format(view_name), form=form)


def redirect_to(view_name, **options):
    return redirect(url_for(view_name, **options) if options else url_for(view_name))
