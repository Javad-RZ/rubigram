from typing import Any


class state:
    def __init__(self):
        self.data: dict[str, dict[str, Any]] = {}
        self.state: dict[str, str] = {}

    async def set_state(self, user_id: str, state: str):
        self.state[user_id] = state

    async def get_state(self, user_id: str):
        return self.state.get(user_id)

    async def remove_state(self, user_id: str):
        self.state.pop(user_id, None)

    async def set_data(self, user_id: str, **data):
        if user_id not in self.data:
            self.data[user_id] = {}
        self.data[user_id].update(data)

    async def get_data(self, user_id: str, key: str = None):
        data = self.data.get(user_id, {})
        return data.get(key) if key else data

    async def remove_data(self, user_id: str, key: str = None):
        if key:
            return self.data.get(user_id, {}).pop(key, None)
        return self.data.pop(user_id, None)