import sqlite3
import os

NEW_ENTRY_DIR = "new_entries"
OLD_ENTRY_DIR = "old_entries"

db = sqlite3.connect("database.db")

cur = db.cursor()

listing = os.listdir(NEW_ENTRY_DIR)

'''
An entry assumes the format:

root
definition
derivation (optional)

Optional lines can be left empty

'''

for entry in listing:
	fname = os.path.join(NEW_ENTRY_DIR, entry)
	f = open(fname, "r")
	data = f.read()
	f.close()

	spldata = data.split("\n")

	root, definition, derivation = spldata[0], spldata[1], spldata[2]

	if len(root) == 0:
		print("Root can not be empty!")
		continue

	if len(definition) == 0:
		print("Definition can not be empty!")

	command = "insert into roots (root, definition, derivation) values ('{root}', '{definition}', '{derivation}')"
	command = command.format(root = root, definition = definition, derivation = derivation)

	try:
		cur.execute(command)
	except sqlite3.IntegrityError:
		print("Root <" + root + "> already exists!")

	os.rename(fname, os.path.join(OLD_ENTRY_DIR, entry))

db.commit()
