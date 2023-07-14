from instapy2 import InstaPy2
from instapy2.types import FetchMode

session = InstaPy2(username="", password="")
session.login()

# see documentation for a function
print(session.like.hashtags.__doc__) # hint: __doc__

# like hashtags (no interaction needed) :)
session.like.hashtags(amount=20, iterable=["food", "burger"], mode=FetchMode.RECENT)

# like locations (interaction needed) :)
session.like.locations(amount=10, iterable=["Perth, Western Australia"])

# like usernames (no interaction needed) :)
session.like.usernames(amount=50, iterable=["official_antique"])