from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User
import praw
import os

app = Flask(__name__)
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



CLIENT_ID = "c2YVgHTmKv3aAw"
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = 'http://127.0.0.1:65010/authorize_callback'

@app.route('/')
def homepage():
    link_no_refresh = r.get_authorize_url('UniqueKey',['identity', 'read', 'submit', 'history', 'report'])
    link_refresh = r.get_authorize_url('DifferentUniqueKey',['identity', 'read', 'submit', 'history', 'report'],
                                       refreshable=True)
    link_no_refresh = "<a href=%s>link</a>" % link_no_refresh
    link_refresh = "<a href=%s>link</a>" % link_refresh
    text = "First link. Not refreshable %s</br></br>" % link_no_refresh
    text += "Second link. Refreshable %s</br></br>" % link_refresh
    return text

@app.route('/authorize_callback')
def authorized():
    state = request.args.get('state', '')
    code = request.args.get('code', '')
    info = r.get_access_information(code)
    user = r.get_me()
    variables_text = "State=%s, code=%s, info=%s." % (state, code,
                                                      str(info))
    text = 'You are %s and have %u link karma.' % (user.name,
                                                   user.link_karma)
    back_link = "<a href='/'>Try again</a>"

    subreddit = r.get_subreddit('funny').get_top(limit=5)
    
    print "TYPE", type(subreddit)

    for thing in subreddit:
        print thing.url
        print thing.title
        print thing.subreddit 
        print "*"*80

    # import pdb; pdb.set_trace()

    return variables_text + '</br></br>' + text + '</br></br>' + back_link

if __name__ == '__main__':
    # app.debug = True

    # connect_to_db(app)

    # # Use the DebugToolbar
    # DebugToolbarExtension(app)
    r = praw.Reddit('Test of Reddit API ')
    r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
   
    app.run(debug=True, port=65010)



