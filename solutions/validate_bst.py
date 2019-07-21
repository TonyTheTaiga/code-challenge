#!/usr/bin/python3
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

    10
  /    \
5       15
      /    \
    11      20
   /  \
  6    16      
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Edge case of []
        if not root:
            return True

        def helper(node, lb, ub):
            if not node:
                return True
            
            if lb != None and ub != None:
                if node.val <= lb or node.val >= ub:
                    return False
            elif lb != None and ub == None:
                if node.val <= lb:
                    return False
            elif lb == None and ub != None:
                if node.val >= ub:
                    return False
            
            return helper(node.left, lb, node.val) and helper(node.right, node.val, ub)
        

        return helper(root, None, None)