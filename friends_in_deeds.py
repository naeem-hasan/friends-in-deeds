from facebook import GraphAPI
from data import FriendsData
import requests

TOKEN = ""
TOTAL = 50
FILENAME = "output"

graph = GraphAPI(access_token=TOKEN, version='2.9')
data = FriendsData()

total = 0
total_comments = 0
total_reactions = 0

feed = graph.get_object("me/feed")
while total < TOTAL:
    try:
        all_ids = [i["id"] for i in feed["data"]]
        for id in all_ids:
            comments = graph.get_object(id + "/comments")
            while 2 > 1:
                try:
                    for comment in comments["data"]:
                        data.add_friend(comment["from"]["name"], "COMMENT")
                        total_comments += 1
                    comments = requests.get(comments["paging"]["next"]).json()
                except KeyError:
                    break
            reactions = graph.get_object(id + "/reactions")
            while 2 > 1:
                try:
                    for reaction in reactions["data"]:
                        data.add_friend(reaction["name"], "REACTION")
                        total_reactions += 1
                    reactions = requests.get(reactions["paging"]["next"]).json()
                except KeyError:
                    break
            total += 1
            print "Posts: {}\t\tComments: {}\t\tReactions: {}".format(total, total_comments, total_reactions)
            # data.print_()
            if total >= TOTAL:
                break
        feed = requests.get(feed["paging"]["next"]).json()
    except KeyboardInterrupt, KeyError:
        break

data.save("{}.txt".format(FILENAME))
data.save_csv("{}.csv".format(FILENAME))
print "Done."
