class NODE:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None
#created node with next and previous pointer
class dll:
	def __init__(self):
		self.head=None
#head will always pointing to start
	def ADD_LAST(self,data):
		newnode=NODE(data)
#allocate a node
		if self.head==None:
			self.head=newnode
		else:
			temp=self.head
			while temp.next!=None:
				temp=temp.next
			temp.next=newnode
			newnode.prev=temp
	def ADD_FIRST(self,data):
		newnode=NODE(data)
		newnode.next=self.head
		if self.head!=None:
			self.head.prev=newnode
		self.head=newnode
#adding previous and next pointer to each funtion
	def disp(self,node):
		if self.head==None:
			print("no data")
		print("printing data ")
		while node:
			print(node.data,end=" ")
			last=node
			node=node.next
#taking last variable becouse we cant use nonde for previous becouse at last it will be pointing to None
		print("\nreverse order")
		while last:
			print(last.data,end=" ")
			last=last.prev
	def ADD_AFTER(self,pNODE,data):
		newnode=NODE(data)
		if pNODE==None:
			print("previous node can not be null")
		else:
			newnode.next=pNODE.next
			pNODE.next=newnode
		newnode.prev=pNODE
		if newnode.next:
			newnode.next.prev=newnode

nod=dll()
'''nod.disp(n)'''
nod.ADD_LAST(38)
nod.ADD_LAST(78)
nod.ADD_FIRST(98)
nod.ADD_AFTER(nod.head.next,99)
nod.ADD_FIRST(56)
nod.disp(nod.head)