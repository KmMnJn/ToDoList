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
				title text not null,
				due text not null,
				important integer,
				finish integer,
				parent integer);"""

	cur.execute(table_create_sql)# Create table.
	conn.close()# Close Connection.

def create_tree():
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.

	cur.execute('''SELECT * from todo where 1''')
	rows = cur.fetchall()# data fetch on sentence.
	i = 1
	for row in rows:
		while i != row[0]:
			tree.append(0)
			i+=1
		tree.append(Node(row[4]))
		i+=1

	cur.execute(table_create_sql)# Create table.
	conn.close()# Close Connection.

def add_item(_parent):
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.
	(_title, _due, _important) = 
	cur.execute('''INSERT INTO todo (title, due, important, finish, parent) values (?, ?, ?, ?, ?)''', (_title, _due, int(_important), 0, _parent))
	conn.commit()# DB commit
	conn.close()# Close Connection.

	tree[_parent].addChildren(len(tree))
	tree.append(Node(_parent))

def del_item(_parent):
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.
	(_title, _due, _important) = 
	conn.commit()# DB commit
	conn.close()# Close Connection.

	calculate_list = []
	tree[child] = 0
	tree[_parent].deleteChild(child)

def modify_item(_childId):
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.

	cur.execute('''UPDATE todo SET title = ?, due = ?, important = ?, finish = ? WHERE ID = ?''', (_tit, _due, _imp, _fin, _childId))
	conn.commit()# DB commit
	conn.close()# Close Connection.

def move_item(_childId):
	x = int(input(""))
	tree[_childId].setParent(x)

def view_item(_parent):
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.

	cur.execute('''SELECT * from todo where parent = ?''', (_parent,))
	rows = cur.fetchall()# data fetch on sentence.
	for row in rows:
		print(row)

	conn.close()# Close Connection.

#main
tree = [Node(-1)]
create_db()

view_item(2)
