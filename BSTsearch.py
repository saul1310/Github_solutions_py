def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val==val:
            return root
        if root.val<val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)
