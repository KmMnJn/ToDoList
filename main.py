class Node:
	def __init__(self, _parent):
		self.parent = _parent
		self.children = []
	def setParent(self, _parent):
		self.parent = _parent
	def addChildren(self, child):
		import bisect
		bisect.insort(self.children, child)
	def deleteChild(self, child):
		self.children.remove(child)

def create_db():
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.

	table_create_sql = """create table if not exists todo (
				id integer primary key autoincrement,
				what text not null,
				due text not null,
				important integer,
				finish integer,
				parent integer);"""
	cur.execute(table_create_sql)# Create table.
	conn.close()# Close Connection.

tree = []
a = Node(0)
a.addChildren(5)
a.addChildren(9)
a.addChildren(11)
a.addChildren(14)

a.deleteChild(11)

print(a.children)