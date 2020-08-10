from itertools import permutations
from ..conf import get_settings


class PretyObjectMixin():

    @staticmethod
    def get_pretty_object_list(queryset, b_size=2, box_size=4):

        class Box(object):

            def __init__(self, index):
                super().__init__()

                self._items = []
                self._size = box_size

            @property
            def size(self):
                if not self._items:
                    return 0
                return sum(self.item_size(item) for item in self._items)

            @staticmethod
            def item_size(item):
                return b_size if item.border else 1

            def add(self, item):
                if self.size + self.item_size(item) <= self._size:
                    self._items.append(item)
                    return

                items = self._items.copy()
                items.append(item)
                for comb in permutations(items, len(self._items)):

                    _sum = sum(self.item_size(item) for item in comb)
                    if not _sum == self._size:
                        continue

                    diff = set(self._items).difference(set(comb))

                    self._items = list(comb)

                    try:
                        return diff.pop()
                    except KeyError:
                        return

                return item

            def complete(self):
                return self.size == self._size

        box = None
        count = get_settings('SPECIAL_PRODUCTS_COUNT')
        iteration = 0
        objs = list(queryset.order_by('?')[:count])
        result = []
        while iteration < (count * b_size / box_size):

            if box is None:
                box = Box(iteration)
                box.add(objs.pop(0))

            empty = set()
            for index, item in enumerate(objs):

                obj = box.add(item)
                objs[index] = obj

                if obj is None:
                    empty.add(index)

                if box.complete():
                    break

            for index, pos in enumerate(empty):
                del objs[pos - index]

            if box.complete() or not objs:
                result.append(box._items)
                box = None

            if not objs:
                break

            iteration += 1

        if objs:
            box = box or Box(len(result))
            for orphan in objs:
                box._items.append(orphan)
            result.append(box._items)

        return result
