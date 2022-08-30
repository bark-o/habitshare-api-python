import requests
import json
from datetime import datetime
from habitshare_api_python.endpoints import (
    LOGIN_URL,
    HABITS_URL,
    MESSAGE_URL,
    FRIENDS_URL,
    FRIENDHABIT_URL,
)


class HabitShare:
    def __init__(self, username, password):
        """Fetches key for authorized user and initializes a list of friends to reference"""
        basic_headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
        }
        body = json.dumps({"password": password, "username": username})
        self.token = requests.post(LOGIN_URL, headers=basic_headers, data=body).json()[
            "key"
        ]
        self.auth_payload = {
            "Authorization": "Token " + self.token,
            "Content-type": "application/json",
            "Accept": "application/json",
        }

        # keep the friend list stored.
        self.get_friends()

    def get_habits(self):
        """Returns a dict with all of authorized user's habit data"""
        return requests.get(HABITS_URL, headers=self.auth_payload).json()

    def get_friends(self):
        """Returns a dict with metadata on authorized user's friends"""
        self.friends = requests.get(FRIENDS_URL, headers=self.auth_payload).json()
        return self.friends

    def get_friend(self, friend, update=False):
        """Return the id of a friend given their exact name in HabitShare."""
        if update:
            self.get_friends()

        usr = [user for user in self.friends if user["name"] == friend][0]
        return usr

    def friend_last_checkin(self, friend):
        """Return the last overall checkin from a friend."""
        usr = self.get_friend(friend)
        return datetime.strptime(usr["lastCheckin"], "%Y-%m-%d")

    def message(self, friend, message):
        """Send a message from the authorized account to a friend."""
        friend_id = str(self.get_friend(friend)["id"])
        body = json.dumps({"content": message, "friendId": friend_id})
        r = requests.post(MESSAGE_URL, headers=self.auth_payload, data=body)
        return r

    def friend_habit_trackers(self, friend):
        """Returns dict of habit data from a friend. (Similar to get_habits but for another user.)"""
        friend_id = str(self.get_friend(friend)["id"])
        full_friend_data = requests.get(
            FRIENDHABIT_URL + friend_id, headers=self.auth_payload
        ).json()["habits"]
        friend_trackers = {}
        for habit in full_friend_data:
            friend_trackers[habit["title"]] = habit["trackers"]
        return friend_trackers
