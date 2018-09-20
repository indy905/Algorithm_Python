# Binary search tree : 부모의 왼쪽 자식 노드는 부모보다 작은 값이, 오른쪽 자식노드에는 큰 값이 오도록 구성된 트리
# Pre order traverse : root 방문 후 left subtree 방문, right subtree 방문
# In Order Traverse : left 방문 후 parent 방문 후 right 방문
# Post Order Travers : left -> right -> parent


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = Node(None)

    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)

    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False

    def remove(self, item):
        if self.head.val is None:
            print("Binary Search Tree가 비었습니다.", item)
        if self.head.val == item:
            # case 1 : 지우려는 노드의 자식 노드가 없을 때, 그냥 삭제
            if self.head.left is None and self.head.right is None:
                self.head = None
            # case 2 : 지우려는 노드가 자식이 하나 있을 때, 삭제 후 자식을 할아버지(지운 노드의 부모)에게 연결
            elif self.head.left is None and self.head.right is not None:
                self.head = self.head.right
            elif self.head.left is not None and self.head.right is None:
                self.head = self.head.left
            # case 3 : 지우려는 노드의 자식이 둘 있을 때, 오른 쪽에 있는 자식 중 가장 왼쪽 노드를 삭제한 노드 위치에 추가
            else:
                self.head.val = self.__most_left_val_from_right_node(self.head.right).val
                self.__removeitem(self.head, self.head.right, self.head.val)
        else:
            if self.head.val > item:
                self.__remove(self.head, self.head.left, item)
            else:
                self.__remove(self.head, self.head.right, item)

    def __remove(self, parent, cur, item):
        if cur is None:
            print("노드가 없습니다 : ", item)
        if cur.val == item:
            # case 1 : 지우려는 노드의 자식 노드가 없을 때, 그냥 삭제
            if cur.left is None and cur.right is None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            # case 2 : 지우려는 노드가 자식이 하나 있을 때, 삭제 후 자식을 할아버지(지운 노드의 부모)에게 연결
            elif cur.left is None and cur.right is not None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right
            elif cur.left is not None and cur.right is None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            # case 3 : 지우려는 노드의 자식이 둘 있을 때, 오른 쪽에 있는 자식 중 가장 왼쪽 노드를 삭제한 노드 위치에 추가
            else:
                cur.val = self.__most_left_val_from_right_node(cur.right).val
                self.__removeitem(cur, cur.right, cur.val)

    def __most_left_val_from_right_node(self, cur):
        if cur.left is None:
            return cur
        else:
            return self.__most_left_val_from_right_node(cur.left)

    def __removeitem(self, parent, cur, item):
        if cur.val == item:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        else:
            if cur.val > item:
                self.__removeitem(cur, cur.left, item)
            else:
                self.__removeitem(cur, cur.right, item)

    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        print(cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        print(cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)

    def postorder_traverse(self):
        if self.headis is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)
        if cur.right is not None:
            self.__postorder(cur.right)

        print(cur.val)





bt = BinaryTree()
bt.add(5)
bt.add(3)
bt.add(4)
bt.add(1)
bt.add(7)
bt.preorder_traverse()
bt.inorder_traverse()