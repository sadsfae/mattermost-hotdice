#!/usr/bin/env python
# Basic flask app / API that can serve an outgoing
# webhook or slash command for MatterMost.
# This is a simple random dice roller.

import requests
import os
import json
import subprocess
import random
from urlparse import urlsplit,urlunsplit
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify

app = Flask(__name__)

# sanitize input for unicode
_u = lambda t: t.decode('UTF-8', 'replace') if isinstance(t, str) else t

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/hotdice', methods = ['GET', 'POST'])
def hotdice():
    if request.method == 'GET':
        request_data = request.get_data()
        return "nothing here\n"
        # your code goes here.
    if request.method == 'POST':
        request_json = request.get_json(force=True)
        text_input = str(request_json["text"])
	dicerange_array=text_input.split()
	# basic input sanitization
    if len(dicerange_array) > 1:
        dicerange=str(dicerange_array[1])
        if not is_int(dicerange):
            dicerange='1000'
        else:
            dicerange='1000'
        user_name = str(request_json["user_name"])
        diceroll = random.randint(0, int(dicerange))
        diceroll_result = user_name + " rolled a %s out of %s" % (str(diceroll), str(dicerange))
        diceroll_out = {"response_type": "ephemeral", "icon_url":
                        "https://funcamp.net/w/dice.png", "username":
                        "vegas", "text": diceroll_result}
        response = app.response_class(response=json.dumps(diceroll_out) + '\n', status=200, mimetype="application/json")
        return response
    else:
        return "405 Method Not Allowed"

# same thing as above but for a slashcommand
@app.route('/random', methods=['POST', 'GET'])
def mattermost_random_integration():
  tokens = flask.request.values.get('text').strip().split()
  username = flask.request.values.get('user_name')
  if len(tokens) == 0:
    min_num = 0
    max_num = 1000
  elif len(tokens) == 1:
    min_num = 0
    max_num = int(tokens[0])
  else:
    flask.abort(400, 'Bad formatting')
  result_num = random.randint(min_num, max_num)
  response_text = ('A magic die is rolled by **{}**.  It could have been any '
                   'number from **{}** to **{}**, but this time it turned up a '
                   '**{}**.'.format(username, min_num, max_num, result_num))
  response_dict = {
      'response_type': 'in_channel', # everyone needs to see the result
      'text': response_text
  }
  return flask.jsonify(response_dict)

@app.route('/')
def root():
    """
    Home handler
    """
    return "OK"

if __name__ == "__main__":
    # wsgi server options
    port = int(os.environ.get('MATTERMOST_DKP_PORT', 8090))
    # use 0.0.0.0 if it shall be accessible from outside of host
    app.run(host='127.0.0.1', port=port)
