from cs50 import SQL

db = SQL("sqlite:///favorites.db")

# print(db)

favourite = input("Favourite: ")
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE language = ?", favourite)
row = rows[0]

# print(row["n"])
# print(rows)

#! RACE CONDITION
id = 505
db_race = SQL("enter-the-db-path/url")
db.execute("BEGIN TRANSACTION")
rows = db.execute("SELECT likes FROM posts WHERE id = ?", id)
likes = rows[0]
db.execute("UPDATE posts SET likes = ? WHERE id = ?", likes + 1, id)
db.execute("COMMIT")


#! SQL INJECTION:

email = "booty@of.com'--" # "--" in sql means a comment, it'll comment everything after --
password = "password"
db.execute(f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
# db.execute(f"SELECT * FROM users WHERE email = 'booty@of.com'--' AND password = '{password}'");
# the ' the user deliberatly put in the email actually closes the ' put in by the user in the sql query and the -- the user put in, makes the rest of the sql query marked as a comment which is not to be executed
# so the user only enters the email and the sql query runs and actually retursn the user with that email without entering the password

#* Thats why use placeholders - ? to avoid simple sql injection attack like above


db.execute("SELECT * FROM users WHERE email = ?  AND password = ?", email, password)
# There are other ways to solve this error like -
# while taking the inputs, search for any single quotes and convert them to two single quotes
