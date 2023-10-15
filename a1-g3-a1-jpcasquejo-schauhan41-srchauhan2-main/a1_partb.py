class SetList:
    class Node:
        def __init__(self, data = None, set_list = None, next_node = None, prev_node = None):
            self.data = data
            self.set_list = set_list
            self.next_node = next_node
            self.prev_node = prev_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def get_previous(self):
            return self.prev_node

        def get_set(self):
            return self.set_list

    def __init__(self):
        self.front = None
        self.back = None

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def make_set(self, data):
        if self.front is None:
            new_node = self.Node(data, self)
            self.front = new_node
            self.back = new_node
            return new_node
        else:
            return None

    def find_data(self, data):
        current_node = self.front
        while current_node:
            if current_node.get_data() == data:
                return current_node

            current_node = current_node.get_next()
        return None

    def representative_node(self):
        return self.front

    def representative(self):
        if self.front:
            return self.front.get_data()
        else:
            return None

    def union_set(self, other_set):
        current_node = other_set.front
        count = 0
        while current_node:
            next_node = current_node.get_next()
            current_node.set_list = self
            current_node.next_node = None
            current_node.prev_node = self.back
            if self.back:
                self.back.next_node = current_node
            else:
                self.front = current_node
            self.back = current_node
            count += 1
            current_node = next_node
        other_set.front = None
        other_set.back = None
        return count

    # 	def pop_front(self):
    # if self.front is not None:
    #     rm = self.front
    #     self.front = self.front.next
    #     if self.front is None:
    #         self.back = None
    #     else:
    #         self.front.prev = None
    #     del rm
    # ------------------------------
    # 	def push_front(self, data):
    # nn = self.Node(data, self.front)
    # if self.front is None:
    #     self.back = nn
    # else:
    #     self.front.prev= nn
    # self.front = nn

    def __len__(self):
        count = 0
        cn = self.front
        while cn:
            count += 1
            cn = cn.get_next()
        return count
