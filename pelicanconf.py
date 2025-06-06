AUTHOR = 'casey durfee'
SITENAME = "mathletix"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Pacific/Honolulu'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
#    ("Pelican", "https://getpelican.com/"),
#    ("Python.org", "https://www.python.org/"),
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
#    ("You can add links in your config file", "#"),
#    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


### added by me
STATIC_PATHS = ["img", "extra/CNAME"]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
ARTICLE_EXCLUDES = ["img"]
PAGE_EXCLUDES = ["img"]