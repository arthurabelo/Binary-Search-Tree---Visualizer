class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if self.isnumber(key) and self.isnumber(node.val):
            key = float(key)
            node.val = float(node.val)
        if key < node.val:
            key, node.val = self.conv_float_str(key, node.val)
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            key, node.val = self.conv_float_str(key, node.val)
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
                
        
    def remove(self, key):
        if self.root is None:
            return False
        else:
            self.root, deleted = self._remove(self.root, key)
        return deleted
                
    def _remove(self, node, key):
        if node is None:
            return node, False
        
        if self.isnumber(key) and self.isnumber(node.val):
            key = float(key)
            node.val = float(node.val)
    
        if key < node.val:
            key, node.val = self.conv_float_str(key, node.val)
            node.left, _ = self._remove(node.left, key)
        elif key > node.val:
            key, node.val = self.conv_float_str(key, node.val)
            node.right, _ = self._remove(node.right, key)
        else:  # Quando key == node.val
            # Caso 1: Nó folha
            if node.left is None and node.right is None:
                return None, False
            # Caso 2: Nó com um filho
            elif node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            # Caso 3: Nó com dois filhos
            else:
                # Encontre o menor valor na subárvore direita (sucessor)
                min_larger_node = self._find_min(node.right)
                # Substitua o valor do nó atual pelo valor do sucessor
                node.val = min_larger_node.val
                # Remova o sucessor da subárvore direita
                node.right, _ = self._remove(node.right, min_larger_node.val)
    
        return node, True
            
    def isnumber(self, num):
        try:
            float(num)
            return True
        except:
            pass
        return False
    
    def conv_float_str(self, key, node_val):
        def convert(value):
            try:
                float_value = float(value)
                if float_value.is_integer():
                    return str(int(float_value))
                else:
                    return str(float_value)
            except ValueError:
                return str(value)
        
        return convert(key), convert(node_val)
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def exists(self, root, name):
        if root is None:
            return False
        if self.isnumber(root.val):
            root.val = float(root.val)
        name, root.val = self.conv_float_str(name, root.val)
        if root.val == name:
            return True
        elif name < root.val:
            return self.exists(root.left, name)
        else:
            return self.exists(root.right, name)

    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node):
        if node is None:
            return -1
        return max(self.height(node.left) + 1, self.height(node.right) + 1)

    def minValueNode(self, node):
        if self.isnumber(node.val):
            node.val = float(node.val)
        _, node.val = self.conv_float_str(0.0, node.val)
        current = node
        if node is not None:
            while current.left is not None:
                current = current.left
            return current.val
        else:
            return None

    def maxValueNode(self, node):
        if self.isnumber(node.val):
            node.val = float(node.val)
        _, node.val = self.conv_float_str(0.0, node.val)
        current = node
        if node is not None:
            while current.right is not None:
                current = current.right
            return current.val
        else:
            return None

    def leafNodes(self, node, leaves=[]):
        if node is not None:
            if node.left is None and node.right is None:
                leaves.append(node.val)
            self.leafNodes(node.left, leaves)
            self.leafNodes(node.right, leaves)
        return ', '.join(map(str, leaves))

    def internalPathLength(self, node, depth=0):
        if node is None:
            return 0
        else:
            return depth + self.internalPathLength(node.left, depth+1) + self.internalPathLength(node.right, depth+1)

    def isBalanced(self, node):
        if node is None:
            return True
        left_height = self.height(node.left) + 1 # Altura do ramo da esquerda mais 1 para contar com a raíz
        right_height = self.height(node.right) + 1 # Altura do ramo da direita mais 1 para contar com a raíz
        if abs(left_height - right_height) <= 1 and self.isBalanced(node.left) and self.isBalanced(node.right):
            return True
        return False

    def inorderTraversal(self, node, result=[]):
        if node:
            self.inorderTraversal(node.left, result)
            result.append(node.val)
            self.inorderTraversal(node.right, result)
        return result

    def postorderTraversal(self, node, result=[]):
        if node:
            self.postorderTraversal(node.left, result)
            self.postorderTraversal(node.right, result)
            result.append(node.val)
        return result

    def preorderTraversal(self, node, result=[]):
        if node:
            result.append(node.val)
            self.preorderBTraversal(node.left, result)
            self.preorderBTraversal(node.right, result)
        return result
    
    def preorderBTraversal(self, node, result=[]):
        if node:
            result.append(node.val)
            self.preorderTraversal(node.right, result)
            self.preorderTraversal(node.left, result)
        return result

    def levelOrderTraversal(self):
        if self.root is None:
            return []
        queue, result = [self.root], []
        while queue:
            current = queue.pop(0)
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result