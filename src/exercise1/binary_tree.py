# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # --------------------- additional abstract methods ---------------------
    def left(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)  # possibly None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:  # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p  # visit p between its subtrees
        if self.right(p) is not None:  # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # override inherited version to make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()  # make inorder the default

    def inorderNext(self, p):
        if self.right(p) is not None:
            return self._leftmost(self.right(p))
        else:
            walk = p
            parent = self.parent(walk)
            while parent is not None and walk == self.right(parent):
                walk = parent
                parent = self.parent(walk)
            return parent

    def postorderNext(self, p):
        if self.parent(p) is None:
            return None
        else:
            parent = self.parent(p)
            if p == self.left(parent):
                if self.right(parent) is None:
                    return parent
                else:
                    return self._leftmost(self.right(parent))
            else:
                return parent


def list_to_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root


# Testing the functionality
values = [1, 2, 3, None, 4, 5, 6]
root = list_to_tree(values)
tree = BinaryTree(root)

# Test inorderNext
inorder_nodes = list(tree.inorder())
print("Inorder Traversal:", [node.value for node in inorder_nodes])

for node in inorder_nodes:
    next_node = tree.inorderNext(node)
    if next_node:
        print(f"Inorder next of {node.value}: {next_node.value}")
    else:
        print(f"Inorder next of {node.value}: None")

# Test postorderNext
postorder_nodes = list(tree.positions())  # Assuming this is actually postorder traversal
print("Postorder Traversal:", [node.value for node in postorder_nodes])

for node in postorder_nodes:
    next_node = tree.postorderNext(node)
    if next_node:
        print(f"Postorder next of {node.value}: {next_node.value}")
    else:
        print(f"Postorder next of {node.value}: None")