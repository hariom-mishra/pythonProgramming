class NODE:
	def __init__(self,data):
		self.data=data
		self.next=None
class sll:
	def __init__(self):
		self.head=None
	
	def ADD_LAST(self,value):
		newnode=NODE(value)
		if self.head==None:
			self.head=newnode
		else:
			temp=self.head
			while temp.next!=None:
				temp=temp.next
			temp.next=newnode
	def ADD_FRONT(self,value):
		newnode=NODE(value)
		newnode.next=self.head
		self.head=newnode;
		
	def Disp(self):
		if self.head==None:
			print("no data")
		else:
			temp=self.head
			while temp!=None:
				print(temp.data, end=" ")
				temp=temp.next
			print()
	def dlt_frnt(self):
		if self.head==None:
			print("no data to delete")
		else:
			self.head=self.head.next
	def dlt_lst(self):
		if self.head==None:
			print("no data to delte")
		else:
			temp=self.head
			while temp.next.next!=None:
				temp=temp.next
			temp.next=None

nod=sll()
nod.Disp()
nod.ADD_LAST(34)
nod.ADD_LAST(98)
nod.ADD_FRONT(22)
nod.ADD_LAST(56)
nod.ADD_FRONT(11)
nod.Disp()
nod.dlt_lst()
nod.Disp()