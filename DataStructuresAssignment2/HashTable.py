MAX_HASH_TABLE_SIZE = 4096


class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def get_valid_index(self, key):
        # Use Python's in-built `hash` function and implement linear probing
        idx = hash(key) % len(self.data_list)
        while self.data_list[idx] and self.data_list[idx][0] != key:
            idx = (idx + 1) % len(self.data_list)
        return idx

    def __getitem__(self, key):
        # Implement the logic for "find" here
        idx = self.get_valid_index(key)
        return self.data_list[idx][1]

    def __setitem__(self, key, value):
        # Implement the logic for "insert/update" here
        idx = self.get_valid_index(key)
        self.data_list[idx] = (key, value)

    def __iter__(self):
        return (x for x in self.data_list if x is not None)

    def __len__(self):
        return len([x for x in self])

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)
