import random

class Unique:
    def __init__(self, items, **kwargs):
        self.items = items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.iterator = iter(items)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                item = next(self.iterator)
                key = item.lower() if self.ignore_case and isinstance(item, str) else item

                if key not in self.seen:
                    self.seen.add(key)
                    return item
            except StopIteration:
                raise StopIteration



if __name__ == "__main__":
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique_data1 = Unique(data1)
    print(list(unique_data1))

    data2 = (random.randint(1, 3) for _ in range(10))
    unique_data2 = Unique(data2)
    print(list(unique_data2))

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_data3 = Unique(data3)
    print(list(unique_data3))

    unique_data4 = Unique(data3, ignore_case=True)
    print(list(unique_data4))
