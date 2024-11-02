dict ={}
for i in range(len(inorder)):
	dict[inorder[i]] = i
        
	preorder_ind = 0
    def helper(low,high):
        if low > high:
                return None
        else:
            preorder_ind +=1
            return TreeNode(preorder[preorder_ind],helper(low,dict[preorder[preorder_ind]]-1),helper(dict[preorder[preorder_ind]]+1,high)

		     

	
return TreeNode(preorder[0], helper(0,dict[preorder[0]]-1),helper(dict[preorder[0]+1,len(inorder))
