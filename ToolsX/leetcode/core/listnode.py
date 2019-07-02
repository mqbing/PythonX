import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.has_cycle():
            return 'cycle'
        return f'{self.val}' + ('' if not self.next else f' -> {self.next}')

    def __repr__(self):
        return self.__str__()

    def trim(self):
        # 也可以正则
        return self.__str__().replace(' ', '').replace('-', '').replace('>', '')

    def has_cycle(self) -> bool:
        slow = fast = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if id(slow) == id(fast):
                return True
        return False

    def append_tail(self, node):
        if isinstance(node, ListNode):
            self.get_tail().next = node
            return self
        else:
            return self.append_tail(ListNode(node))

    def get_tail(self):
        tail = self
        while tail.next:
            tail = tail.next
        return tail

    @classmethod
    def create(cls, length=5, start=1, end=10, rand=False):
        if length == 0:
            return None
        node = ListNode(start if not rand else random.randrange(start, end))
        if length == 1:
            return node
        current = node
        for i in range(start + 1, start + length):
            current.next = ListNode(i if not rand else random.randrange(start, end))
            current = current.next
        return node

    @classmethod
    def random(cls, length=5, **kwargs):
        return cls.create(length, **kwargs)

    @classmethod
    def from_array(cls, iterable):
        head = current = None
        for i in iterable:
            if current is None:
                current = head = ListNode(i)
            else:
                current.next = ListNode(i)
                current = current.next
        return head
