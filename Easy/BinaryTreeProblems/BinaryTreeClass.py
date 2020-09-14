#<-2-> defining binary tree
class BinaryTree:
    
    # static varaible
    preorderList =list()
    postorderList=list()
    inorderList=list()
    leafNode=list()
    NonleafNode=list()
    path =list()
    listOfPath = list()
    def __init__(self):
        self.root = None
        self.TotalnonLeafNode = 0
        self.hight = 0
        self.TotalnonLeafNode = 0
        self.levelOfBinaryTree = 0
        self.isStrictBinaryTree = False
        self.totalNode = 0
        self.Max=0
        self.Min= 0
        self.IsBSt = False
        
    def preorderTraversal(self, root,preorderList):  #root:left:right
        temp = root
        if temp:
            preorderList.append(temp.data)
            self.preorderTraversal(temp.left,preorderList)
            self.preorderTraversal(temp.right,preorderList)
        return preorderList
            
    def InorderTraversal(self, root,inorderList):  #left:root:right
        temp = root
        if temp:
            self.InorderTraversal(temp.left,inorderList)
            inorderList.append(temp.data)
            self.InorderTraversal(temp.right,inorderList)
        return inorderList
        
    def postorderTraversal(self, root,postorderList):  #left:right:root
        temp = root
        if temp:
            self.postorderTraversal(temp.left,postorderList)
            self.postorderTraversal(temp.right,postorderList)
            postorderList.append(temp.data)
        return postorderList
        
    # leaf node : None<-root->None
    def countOfNonLeafNode(self, root):
        temp = root
        if temp is None:
            return 0
        if temp.left is None and temp.right is None:
            return 0
        else:
            self.NonleafNode.append(temp.data)
            a=self.countOfNonLeafNode(temp.left)
            b=self.countOfNonLeafNode(temp.right)
        return self.NonleafNode
    
    def countOfLeafNode(self, root):
        temp = root
        if temp is None:
            return 0
        if temp.left is None and temp.right is None:
            self.leafNode.append(temp.data)
        else:
            a=self.countOfLeafNode(temp.left)
            b=self.countOfLeafNode(temp.right)
            
        return self.leafNode
        
    def hightOfBinarytree(self, root):
        temp = root
        if temp is None :
            return 0
        else :
            return 1+ max(self.hightOfBinarytree(root.left),self.hightOfBinarytree(root.right))
    
    def checkStrictBinarytree(self,root):
        temp = root
        if temp is None:
            return True
        if temp.left is  None and temp.right is None:
            return True
        else :
            if (temp.left is not None and temp.right is not None):
                return (self.checkStrictBinarytree(root.left) and self.checkStrictBinarytree(root.right))
            else:
                return False
    
                
    def diameterOfbinarytree(self,root):
        temp =root
        if temp is None:
            return 0
        else :
            lhight = self.hightOfBinarytree(temp.left)
            rhight=self.hightOfBinarytree(temp.right)
            # print(hight)
            lleft = self.diameterOfbinarytree(temp.left)
            rright = self.diameterOfbinarytree(temp.right)
        return max((1+lhight+rhight),max(lleft,rright))
        
    def optimizedHight(self,root,ans):
        if root is None:
            return 0
            
        else:
            lhigth =self.optimizedHight(root.left,ans)
            rhight = self.optimizedHight(root.right,ans)
            ans[0]= max(ans[0],1+ lhigth+rhight)
            return 1+max(lhigth,rhight)
        
    def optimizedDiameterOfBinaeryTree(self,root):
        if root is None:
            return 0
        ans = [-1]
        hightoftree = self.optimizedHight(root,ans)
        return ans[0]
    
    def levelorderTraversal(self,root):
        temp = root
        if temp is None:
            return 0
        que=[]
        que.append(temp)
        res=[]
        while (que):
            arr=[]
            for i in range(len(que)):
                node = que.pop(0)
                arr.append(node.data)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None :
                    que.append(node.right)
            res.append(arr)
        return res
        
    def DetermindAllPathRootToLeaf(self,root,path):
        temp = root
        if temp is None:
            return
        path.append(temp.data)
        if temp.left is None and temp.right is None:
            print(path)
        else:
            self.DetermindAllPathRootToLeaf(temp.left,path)
            self.DetermindAllPathRootToLeaf(temp.right,path)
    
        path.pop()
    
    def findMinOnBT(self,root):
        temp = root
        if temp is None:
            return None
        else :
            Min= temp.data
            if temp.left is not None:
                minL= self.findMinOnBT(root.left)
                Min=min(int(Min),int(minL))
            if temp.right is not None:
                minR=self.findMinOnBT(root.right)
                Min=min(int(minR),int(Min))
        return Min
    
    def findMaxonBt(self,root):
        temp = root
        if temp is None:
            return None
        else :
            Max= temp.data
            if temp.left is not None:
                maxL= self.findMaxonBt(root.left)
                Max=max(int(maxL),int(Max))
            if temp.right is not None:
                maxR=self.findMaxonBt(root.right)
                Max=max(int(maxR),int(Max))
        return Max
        
    def GetLCA(self,root,node1,node2):
        temp= root
        if temp is None:
            return None
        if temp.data == node1 or temp.data == node2:
            return temp.data
    
        lleft=self.GetLCA(temp.left,node1, node2)
        rright=self.GetLCA(temp.right,node1,node2)
        if lleft and rright:
            
            return temp.data
        if lleft is None and rright is None:
            return None
        return lleft if lleft else rright
    
    def IsValidBst(self,root,Max,Min):
        temp= root
        if temp is None:
            return True
        if Min<int(temp.data) and Max>int(temp.data):
            return True
        else:
            return False
        return self.IsValidBst(temp.left,Min,int(temp.data)) and self.IsValidBst(root.right,int(temp.data), Max)
    
    def isStructurallyIdentical(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not  None and root2 is None:
            return False
        else:
            if root1.data == root2.data and self.isStructurallyIdentical(root1.left,root2.left) and self.isStructurallyIdentical(root1.right,root2.right) :
                return True
            else:
                return False
    
    def deepestNode(self,root):
        temp = root
        if temp is None:
            return None
        que =[]
        que.append(temp)
        while(que):
            node= que.pop(0)
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        return node.data
        
    def numberOfLeaveslnBTusingLevelOrder(self,root):
        temp=root
        if temp is None:
            return None
        que=[]
        onlyLeafNode=[]
        que.append(temp)
        while(que):
            node= que.pop(0)
            if node.left is None and node.right is None :
                onlyLeafNode.append(node.data)
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        return onlyLeafNode
        
    def numberOfHalfNodeslnBTusingLevelOrder(self,root):
        temp=root
        if temp is None:
            return None
        que=[]
        onlyOneNode=[]
        que.append(temp)
        while(que):
            node= que.pop(0)
            if (node.left is None and node.right is not None )or(node.left is not None and node.right is None) :
                onlyOneNode.append(node.data)
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        return onlyOneNode
    
    def invertBinaryTree(self,root):
        temp=root
        if temp is not None:
            self.invertBinaryTree(temp.left)
            self.invertBinaryTree(temp.right)
            a=root.left
            root.left = root.right
            root.right=a
        
        return root
                
                
                

        
        
        
        
            
            
            
        
        

       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #
    # def KdistanceOfBinarytree(self, root,k):
    #
    #     temp = root
    #
    #     if temp is None:
    #
    #         return 0
    #
    #     if k==0 :
    #
    #         print (temp.data,end=' ')
    #
    #     else:
    #
    #
    #         self.KdistanceOfBinarytree(temp.left,k-1)
    #
    #         self.KdistanceOfBinarytree(temp.right,k-1)
    #
    # #11
    # def validataBst(self,root,Min,Max):
    #
    #   if root is None :
    #
    #     return True
    #
    #   if(root.data<Min and Max>root.data):
    #
    #     return False
    #
    #   return (self.validataBst(root.left,Min,root.data))and (self.validataBst(root.right,root.data,Max))
    #
    # #12
    # def isStructurallyIdentical(self,root1,root2):
    #
    #   if root1 is None and root2  is None :
    #
    #     return 1
    #
    #   if root1 is None and root2 is not None :
    #
    #     return 0
    #
    #   if root2 is None and root1 is not None :
    #
    #     return 0
    #
    #   else :
    #
    #     if root1.data == root2.data and self.isStructurallyIdentical(root1.left,root2.left) and self.isStructurallyIdentical(root1.right,root2.right) :
    #
    #       return 1
    #
    #     else :
    #
    #       return 0
    # #13
    # def concertingtomirror(self,root):
    #
    #   if root is None :
    #
    #     return None
    #
    #   else :
    #
    #     self.concertingtomirror(root.left)
    #
    #     self.concertingtomirror(root.right)
    #
    #     temp = root.left
    #
    #     root.left= root.right
    #
    #     root.left = temp
    #
    #   return root
    #
