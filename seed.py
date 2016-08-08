"""Utility file to seed ratings database from MovieLens data in seed_data/"""
import time
import datetime
from sqlalchemy import func
import json

from model import User, Rating, Movie, connect_to_db, db
from server import app
import requests
import praw
import webbrowser
import os

client_secret = os.environ['CLIENT_SECRET']


r = praw.Reddit(user_agent="Test Script by L Bard")
r.set_oauth_app_info(client_id="c2YVgHTmKv3aAw",
                     client_secret=client_secret,
                     redirect_uri='http://127.0.0.1:65010/authorize_callback'
                     )
# url=r.get_authorize_url('uniqueKey', 'identity read', True)

# webbrowser.open(url)

access_information = r.get_access_information('9ZxlvAMpvic4Ldk-Tk6g9-ieMtQ')
r.set_access_credentials(**access_information)
authenticated_user = r.get_me()
print authenticated_user.name, authenticated_user.link_karma

# access_information=r.get_access_information('')
 # Interest Inquiry by L. Bard"
# r = praw.Reddit(user_agent=user_agent)
# prawWords-["technology"]
# user_name = "Loribard"
# user = r.get_redditor(user_name)
# thing_limit = 10
# gen = user.get_submitted(limit=thing_limit)
# interest_by_subreddit = {}
# for thing in gen:
#     subreddit = thing.subreddit.display_name
#     interest_by_subreddit[subreddit] = (interest_by_subreddit.get(subreddit,0) + thing.score)
# import pprint
# pprint.pprint(interest_by_subreddit)


# def load_reddit_subreddit():

#     """Load users from u.user into database."""

   

# URL = "https://www.reddit.com/r/technology.json"

# # fetch url
# # decode the json string 
# # print titles of articles on page

# def fetch_listing(url):
#     response = requests.get(url)
#     return response.text

# def decode_listing_str(listing_str):
#     listing_dict = json.loads(listing_str)
#     return listing_dict

# def print_titles(listing_dict):
#     posts = listing_dict["data"]["children"]
#     for post in posts:
#         print post["data"]["title"]

# def main():
#     listing_str = fetch_listing(URL)
#     listing_dict = decode_listing_str(listing_str)
#     print_titles(listing_dict)

# if __name__ == '__main__':
#     main()



#     for i, row in enumerate(open("seed_data/u.user")):
#         row = row.rstrip()
#         user_id, age, gender, occupation, zipcode = row.split("|")

#         user = User(age=age,
#                     zipcode=zipcode)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(user)

#         # provide some sense of progress
#         if i % 100 == 0:
#             print i

#     # Once we're done, we should commit our work
#     db.session.commit()


# def load_movies():
#     """Load movies from u.item into database."""

#     print "Movies"

#     for i, row in enumerate(open("seed_data/u.item")):
#         row = row.rstrip()

#         # clever -- we can unpack part of the row!
#         movie_id, title, released_str, junk, imdb_url = row.split("|")[:5]

#         # The date is in the file as daynum-month_abbreviation-year;
#         # we need to convert it to an actual datetime object.

#         if released_str:
#             released_at = datetime.datetime.strptime(released_str, "%d-%b-%Y")
#         else:
#             released_at = None

#         # Remove the (YEAR) from the end of the title.

#         title = title[:-7]   # " (YEAR)" == 7

#         movie = Movie(title=title,
#                       released_at=released_at,
#                       imdb_url=imdb_url)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(movie)

#         # provide some sense of progress
#         if i % 100 == 0:
#             print i

#     # Once we're done, we should commit our work
#     db.session.commit()


# def load_ratings():
#     """Load ratings from u.data into database."""

#     print "Ratings"

#     for i, row in enumerate(open("seed_data/u.data")):
#         row = row.rstrip()

#         user_id, movie_id, score, timestamp = row.split("\t")

#         user_id = int(user_id)
#         movie_id = int(movie_id)
#         score = int(score)

#         # We don't care about the timestamp, so we'll ignore this

#         rating = Rating(user_id=user_id,
#                         movie_id=movie_id,
#                         score=score)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(rating)

#         # provide some sense of progress
#         if i % 1000 == 0:
#             print i

#             # An optimization: if we commit after every add, the database
#             # will do a lot of work committing each record. However, if we
#             # wait until the end, on computers with smaller amounts of
#             # memory, it might thrash around. By committing every 1,000th
#             # add, we'll strike a good balance.

#             db.session.commit()

#     # Once we're done, we should commit our work
#     db.session.commit()


# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()


# if __name__ == "__main__":
#     connect_to_db(app)
#     db.create_all()

    # load_users()
    # load_movies()
    # load_ratings()
    # set_val_user_id()
