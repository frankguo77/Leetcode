class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        res = f'{t.val}'
        
        if t.left:
            res = f'{res}({self.tree2str(t.left)})'

        if t.right:
            if not t.left:
                res = f'{res}()'
            
            res = f'{res}({self.tree2str(t.right)})'

        return res
                