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


	cur.execute(table_create_sql)# Create table.
	conn.close()# Close Connection.

def add_item(_parent):
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.
	(_title, _due, _important) = 
	cur.execute('''INSERT INTO todo (title, due, important, finish, parent) values (?, ?, ?, ?, ?)''', (_title, _due, int(_important), 0, _parent))
	conn.close()# Close Connection.

	tree[_parent].addChildren(len(tree))
	tree.append(Node(_parent))

def del_item(_parent):
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.
	(_title, _due, _important) = 
	conn.close()# Close Connection.

	calculate_list = []
	tree[child] = 0
	tree[_parent].deleteChild(child)

def modify_item(_childId):
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.
	cur.execute('''UPDATE todo SET what = ?, due = ?, finished = ? WHERE ID = ?''', (wh, du, Fi, Rid))
	conn.close()# Close Connection.

def move_item(_childId):
	

def view_item(_parent):
	import sqlite3
	conn = sqlite3.connect("todolist.db")# Create DB file.
	cur = conn.cursor()# Create cursor on Connection.

	conn.close()# Close Connection.

tree = [Node(-1)]
