import sqlite3

db = sqlite3.connect("database.db")

cur = db.cursor()

cur.execute("create table words (word text primary key, type text, definition text, derivation text)")

#we're going to insert some basics into the table

PREFIXES = {
	'مِ'  : ['pronoun', 'first person singular', 'from Hindi मैं'],
	'تُ'  : ['pronoun', 'second person singular', 'from Hindi तू / तुम'],
	'فوَ' : ['pronoun', 'third person singular (m)', ''],
	'فيَ' : ['pronoun', 'third person singular (f)', ''],
	'هُم' : ['pronoun', 'first person plural', 'from Hindi हुम'],
	'وس' : ['pronoun', 'second person plural', 'from Spanish vos / vosotros'],
	'عنِ' : ['pronoun', 'third person plural', 'from Sumerian a.ne.ne']
}

for prefix in PREFIXES:
	info = PREFIXES[prefix]
	command = "insert into words (word, type, definition, derivation) values ('{word}', '{type}', '{definition}', '{derivation}')"
	command = command.format(word = prefix, type = info[0], definition = info[1], derivation = info[2])
	cur.execute(command)


db.commit()
db.close()