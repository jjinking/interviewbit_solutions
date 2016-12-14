"""
LRUCache
"""

class LRUCache:
    """
    Least Recently Used Cache
    Implemented with a dictionary and a linked list
    """
    def __init__(self, capacity):
        """@param capacity, an integer
        """
        self.cap = capacity
        self.len = 0
        self.newest = None
        self.oldest = None
        self.key2node = {}

    def _refresh_node(self, node):
        """Move node to the newest end
        """
        # If node is already the newest, do nothing and return
        if self.newest == node:
            return
        elif self.oldest == node:
            # Node is the oldest
            self._remove_oldest()
        else:
            # Remove from middle
            node.older.newer = node.newer
            node.newer.older = node.older

        # Insert into newest end
        self._insert_newest(node)

    def _insert_newest(self, node):
        """Insert node to newest end
        """
        # If there are no items in the cache, set oldest and newest to the same node
        if self.len == 0:
            self.newest = node
            self.oldest = node
            node.left = None
            node.right = None
        else:
            node.older = self.newest
            self.newest.newer = node
            self.newest = node
            self.newest.newer = None

    def _remove_oldest(self):
        """Remove the oldest node from cache
        """
        # If there are no nodes, return
        if self.len == 0:
            return

        if self.len == 1:
            prev_oldest = self.oldest
            self.newest = None
            self.oldest = None
        else:
            prev_oldest = self.oldest
            self.oldest = self.oldest.newer
            self.oldest.older = None
        return prev_oldest

    def get(self, key):
        """@return an integer
        """
        try:
            node = self.key2node[key]
            self._refresh_node(node)
            return node.val
        except KeyError:
            return -1

    def set(self, key, value):
        """
        @param key, an integer
        @param value, an integer
        @return nothing
        """
        try:
            node = self.key2node[key]
            node.val = value
            self._refresh_node(node)
        except KeyError:
            while self.len >= self.cap:
                prev_oldest = self._remove_oldest()
                self.len -= 1
                del self.key2node[prev_oldest.key]
            node = LRUCache.Node(key, value)
            self._insert_newest(node)
            self.key2node[key] = node
            self.len += 1

    class Node:
        """Doubly linked list node
        """
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.older = None
            self.newer = None
