"""
@Harsha CV + PY training Assgn-2
Binary heap implementation
"""

import numpy as np


class BinaryHeap(object):
    """
    """

    def __init__(self, max):
        self.max = max
        if max is True:
            self.arr = [np.inf]
        elif max is False:
            self.arr = [-np.inf]  # used as terminal condition
        self.idx = 0

    def display_heap_type(self):
        if self.max is True:
            print('Max')
        else:
            print('Min')

    def insert(self, elem):
        self.arr.append(elem)
        cur_idx = self.idx + 1
        par_idx = int(cur_idx / 2)
        if self.max is True:
            while(self.arr[par_idx] < elem):
                self.arr[par_idx], self.arr[cur_idx] = (self.arr[cur_idx],
                                                        self.arr[par_idx])
                cur_idx = par_idx
                par_idx = int(cur_idx / 2)
        elif self.max is not True:
            while(self.arr[par_idx] > elem):
                self.arr[par_idx], self.arr[cur_idx] = (self.arr[cur_idx],
                                                        self.arr[par_idx])
                cur_idx = par_idx
                par_idx = int(cur_idx / 2)
        self.idx += 1

    def heapify_down(self):
        # if heap property violated then swap child and parent
        par_idx = 1
        left_child_idx = 2
        right_child_idx = 3
        if self.max is True:
            child_list = [self.arr[left_child_idx], self.arr[right_child_idx]]
            max_idx, max_value = child_list.index(max(child_list)), max(child_list)
            if max_idx == 0:
                max_idx = left_child_idx
            else:
                max_idx = right_child_idx
            while self.arr[par_idx] < max_value and max_idx < self.idx:
                self.arr[par_idx], self.arr[max_idx] = self.arr[max_idx], self.arr[par_idx]
                par_idx = max_idx
                left_child_idx = 2 * par_idx
                right_child_idx = 2 * par_idx + 1
                if right_child_idx > self.idx or left_child_idx > self.idx:
                    break
                child_list = [self.arr[left_child_idx], self.arr[right_child_idx]]
                max_idx, max_value = child_list.index(max(child_list)), max(child_list)
                if max_idx == 0:
                    max_idx = left_child_idx
                else:
                    max_idx = right_child_idx

        elif self.max is not True:
            child_list = [self.arr[left_child_idx], self.arr[right_child_idx]]
            min_idx, min_value = (child_list.index(min(child_list)),
                                  min(child_list))
            if min_idx == 0:
                min_idx = left_child_idx
            else:
                min_idx = right_child_idx
            while self.arr[par_idx] > min_value and min_idx < self.idx:
                self.arr[par_idx], self.arr[min_idx] = self.arr[min_idx], self.arr[par_idx]
                par_idx = min_idx
                left_child_idx = 2 * par_idx
                right_child_idx = 2 * par_idx + 1
                if right_child_idx > self.idx or left_child_idx > self.idx:
                    break

                child_list = [self.arr[left_child_idx], self.arr[right_child_idx]]
                min_idx, min_value = (child_list.index(min(child_list)),
                                      min(child_list))
                if min_idx == 0:
                    min_idx = left_child_idx
                else:
                    min_idx = right_child_idx

    def display_heap_tree(self):
        """
        Displays the heap in a tree structure
        """
        for i in range(self.idx):
            print(self.arr[i + 1])

    def delete_min(self):
        if self.max:
            print("Invalid Operation")
        else:
            min_elt = self.arr[1]
            self.arr[1] = self.arr[self.idx]
            self.idx -= 1
            self.heapify_down()
            return min_elt

    def delete_max(self):
        if self.max is False:
            print("Invalid Operation")
        else:
            del_elt = self.arr[1]
            self.arr[1] = self.arr[self.idx]
            self.idx = self.idx - 1
            self.heapify_down()
            return del_elt

    def sort(self):
        # new_arr = self.arr.copy()
        display_arr = []
        if self.max is True:
            for i in range(self.idx - 1):
                display_arr.append(self.delete_max())
        elif self.max is False:
            for i in range(self.idx - 1):
                display_arr.append(self.delete_min())
        print(display_arr)

    def find_min(self):
        if self.max is True:
            print("Finding min for a max-heap is not a good operation")
        elif self.max is False:
            return self.arr[1]

    def find_max(self):
        if self.max is False:
            print("Finding max for a min-heap is not a good operation")
        elif self.max is True:
            return self.arr[1]


if __name__ == "__main__":
    bh = BinaryHeap(max=False)
    bh.display_heap_type()
    bh.insert(2)
    bh.insert(1)
    bh.insert(5)
    bh.insert(8)

    bh.insert(12)
    bh.insert(4)
    bh.insert(44)
    bh.display_heap_tree()
    bh.delete_min()
    print("After deletion")
    bh.display_heap_tree()
    a = bh.find_min()
    print("Min ", a)
    bh.sort()
