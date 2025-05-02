class Treenode:
    def __init__(self,data):
        self.info=data
        self.left=None
        self.right=None
def create():
    data=int(input("\nenter data to be inserted or type -1 to exit: "))
    if data == -1:
        return None
    tree=Treenode(data)
    print("enter the left child of: "+ str(data))
    tree.left=create()
    print("enter the right child of: "+ str(data))
    tree.right=create()
    return tree
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.info,end=" ")
    inorder(root.right)
if __name__=="__main__":
    root=None
    root=create()
    inorder(root)
