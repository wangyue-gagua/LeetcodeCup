class Node:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.count = 0
        self.left, self.right, self.bottom, self.top = None, None, None, None

class SegTree2D:
    def __init__(self, x1, y1, x2, y2):
        self.root = Node(x1, y1, x2, y2)

    def update(self, node, x1, y1, x2, y2):
        if x2 < node.x1 or y2 < node.y1 or x1 > node.x2 or y1 > node.y2:
            return
        if x1 <= node.x1 and y1 <= node.y1 and x2 >= node.x2 and y2 >= node.y2:
            node.count += 1
            return
        if node.left is None:
            mid_x, mid_y = node.x1 + (node.x2 - node.x1) // 2, node.y1 + (node.y2 - node.y1) // 2
            node.left = Node(node.x1, node.y1, mid_x, mid_y)
            node.right = Node(mid_x + 1, node.y1, node.x2, mid_y)
            node.bottom = Node(node.x1, mid_y + 1, mid_x, node.y2)
            node.top = Node(mid_x + 1, mid_y + 1, node.x2, node.y2)
        self.update(node.left, x1, y1, x2, y2)
        self.update(node.right, x1, y1, x2, y2)
        self.update(node.bottom, x1, y1, x2, y2)
        self.update(node.top, x1, y1, x2, y2)

    def query(self, node, x1, y1, x2, y2):
        if node is None or x2 < node.x1 or y2 < node.y1 or x1 > node.x2 or y1 > node.y2:
            return 0
        if x1 <= node.x1 and y1 <= node.y1 and x2 >= node.x2 and y2 >= node.y2:
            return node.count
        return (self.query(node.left, x1, y1, x2, y2) + 
                self.query(node.right, x1, y1, x2, y2) + 
                self.query(node.bottom, x1, y1, x2, y2) + 
                self.query(node.top, x1, y1, x2, y2))

def max_overlap_square(squares):
    # Step 1: Sort squares by x coordinate, then by y coordinate
    squares = sorted(squares, key=lambda square: (square[0], square[1]))

    # Step 2: Build 2D segment tree
    x_min = min(x - l // 2 for x, y, l in squares)
    x_max = max(x + l // 2 for x, y, l in squares)
    y_min = min(y - l // 2 for x, y, l in squares)
    y_max = max(y + l // 2 for x, y, l in squares)
    seg_tree = SegTree2D(x_min, y_min, x_max, y_max)

    # Step 3: Iterate over sorted squares and update segment tree
    max_count = 0
    for x, y, l in squares:
        count = seg_tree.query(seg_tree.root, x - l // 2, y - l // 2, x + l // 2, y + l // 2)
        max_count = max(max_count, count + 1)
        seg_tree.update(seg_tree.root, x - l // 2, y - l // 2, x + l // 2, y + l // 2)

    return max_count

print(max_overlap_square([[0, 0, 1], [1, 0, 1]]))
print(max_overlap_square([[4,4,6],[7,5,3],[1,6,2],[5,6,3]]))
print(max_overlap_square([[7,7,9],[7,5,3],[1,8,5],[5,6,3],[9,10,2],[8,4,10]]))
