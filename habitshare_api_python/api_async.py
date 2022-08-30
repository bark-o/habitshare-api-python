import asyncio

from habitshare_api_python.api import HabitShare


async def run_async(func):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, func)


class HabitShareAsync:
    def __init__(self, username, password):
        self._api = HabitShare(username, password)

    async def get_habits(self):
        """Returns a dict with all of authorized user's habit data"""
        return await run_async(lambda: self._api.get_habits())

    async def get_friends(self):
        """Returns a dict with metadata on authorized user's friends"""
        return await run_async(lambda: self._api.get_friends())

    async def get_friend(self, friend, update=False):
        """Return the id of a friend given their exact name in HabitShare."""
        return await run_async(lambda: self._api.get_friend(friend, update))

    async def friend_last_checkin(self, friend):
        """Return the last overall checkin from a friend."""
        return await run_async(lambda: self._api.friend_last_checkin(friend))

    async def message(self, friend, message):
        """Send a message from the authorized account to a friend."""
        return await run_async(lambda: self._api.message(friend, message))

    async def friend_habit_trackers(self, friend):
        """Returns dict of habit data from a friend. (Similar to get_habits but for another user.)"""
        return await run_async(lambda: self._api.friend_habit_trackers(friend))
