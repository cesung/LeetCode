/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private int minDiff = Int32.MaxValue;
    private int prev = -1;

    private void InorderTraversal(TreeNode root) {
        if (root.left != null) {
            InorderTraversal(root.left);
        }

        if (prev != -1) {
            minDiff = Math.Min(
                minDiff,
                Math.Abs(prev - root.val)
            );
        }
        prev = root.val;

        if (root.right != null) {
            InorderTraversal(root.right);
        }
    }

    public int GetMinimumDifference(TreeNode root) {
        InorderTraversal(root);

        return minDiff;       
    }
}