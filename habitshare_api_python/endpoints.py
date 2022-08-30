
from urllib.parse import urljoin

BASE_URL = "https://habitshare.herokuapp.com"
API_VERSION = "v3"

REST_API = urljoin(BASE_URL, "/api/%s/" % API_VERSION)

AUTHORIZE_ENDPOINT = "rest-auth/login/"
HABITS_ENDPOINT = "habits/"
MESSAGES_ENDPOINT = "messages/"

FRIENDS_ENDPOINT = "friends/"
USERS_ENDPOINT = "users/"

LOGIN_URL = urljoin(BASE_URL, AUTHORIZE_ENDPOINT)
HABITS_URL = urljoin(BASE_URL, HABITS_ENDPOINT)
MESSAGE_URL = urljoin(BASE_URL, MESSAGES_ENDPOINT)
FRIENDS_URL = urljoin(REST_API, FRIENDS_ENDPOINT)
FRIENDHABIT_URL = urljoin(REST_API, USERS_ENDPOINT)
