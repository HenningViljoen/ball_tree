import numpy as np

samples_per_leaf = 2

class ball_tree(object):
    def __init__(self):
        self.dimension_compare = 0
        self.centroid = [0, 0]
        self.left = None
        self.right = None

    def fit(self, data):
        if len(data) <= samples_per_leaf:
            return

        dim0 = [d[0] for d in data]
        dim1 = [d[1] for d in data]
        self.centroid = [sum(dim0)/len(dim0), sum(dim1)/len(dim1)]
        print(f'centroid: {self.centroid}')
        dim0_var = max(dim0) - min(dim0)
        dim1_var = max(dim1) - min(dim1)
        self.dimension_compare = 0 if dim0_var >= dim1_var else 1
        print(f'dimension_compare: {self.dimension_compare}')
        list0 = [d for d in data if d[self.dimension_compare] <= self.centroid[self.dimension_compare]]
        list1 = [d for d in data if d[self.dimension_compare] > self.centroid[self.dimension_compare]]
        print(f'list0: {list0}')
        print(f'list1: {list1}')
        print()
        self.left = ball_tree()
        self.left.fit(list0)
        self.right = ball_tree()
        self.right.fit(list1)

        pass

if __name__ == '__main__':
    np.random.seed(0)
    X = np.random.random((8, 2)) * 2 - 1
    X[:, 1] *= 0.1
    X[:, 1] += X[:, 0] ** 2
    data = X.tolist()
    tree = ball_tree()
    tree.fit(data)
    pass




