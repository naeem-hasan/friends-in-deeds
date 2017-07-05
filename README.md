# friends-in-deeds
Which friends interact with you the most in Facebook? Find out easily!

## How does it work?
Well, it uses the Facebook Graph API and iterates through your posts. Along the way, it counts every reactions and comments along the ones who did them!

## Great. How do I use it?
You need to install the following, if you don't have already.
* [Python 2.7.x.](https://www.python.org/downloads/)
* [facebook-sdk](https://facebook-sdk.readthedocs.io/en/latest/install.html)

Then clone/download this repository, edit the friends_in_deeds.py file and change the uppercased variables however it suits you.
* `TOKEN` : This is the most important. You need to get an access token of the Facebook's Graph API. Visit [this link](https://developers.facebook.com/tools/explorer/) and click on *Get Token*. Then copy the text of the Access Token field and paste it in the `TOKEN` variable.
* `TOTAL` : How many posts do you want it to check?
* `FILENAME` : It'll generate two files at the end. `{FILENAME}.txt` and `{FILENAME}.csv`. You can define the FILENAME in this variable.

Done! 
