
The problem is divided into 3 sub cases:
1. If the node has no child
2. if the node has 1 child
3. if the node has 2 child

For case 1 and 2 it's simple 
- if it has no child we simply go to parent and remove the reference to the current node
- for 1 child we simply go to parent node and replace the reference from cur_node to cur_node's only child
- for case 3 we are finding min val in right subtree of bst and replacing it with cur_node val (Note this value will always be smaller than right subtree and greater then current node val thus the bst property remains intact)
- for case 3 we are also removing the right subtree min val as we have moved that value to deleted not


We are using recursion based solution for this
