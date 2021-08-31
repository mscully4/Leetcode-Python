from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.history = deque([], capacity) 
        
        self.map = {}

    def get(self, key: int) -> int:
        result = self.map.get(key, None)
        if result == None:
            return -1
        
        if key in self.history:
            self.history.remove(key)
            
        self.history.append(key)
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.history:
            self.history.remove(key)
            
        if len(self.history) == self.capacity:
            remove_key = self.history.popleft()
            del self.map[remove_key]
            
        self.map[key] = value
        
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)
        