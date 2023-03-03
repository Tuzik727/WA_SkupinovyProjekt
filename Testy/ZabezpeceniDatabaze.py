import pymysql

# Připojení k databázi
db = pymysql.connect(host='localhost', user='user', passwd='password', db='database')

# Testování hesla
try:
    cursor = db.cursor()
    cursor.execute("SELECT 1")
    print("Připojení úspěšné - heslo je správné.")
except pymysql.err.OperationalError as e:
    print("Chyba při připojení: ", e)
    if e.args[0] == 1045:
        print("Chyba při připojení - špatné heslo.")
    elif e.args[0] == 1044:
        print("Chyba při připojení - uživatel nemá přístup k databázi.")
    else:
        print("Chyba při připojení - další chyba.")

# Ověření oprávnění uživatelů
try:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mysql.user")
    results = cursor.fetchall()
    print("Přístupová práva uživatelů:")
    for row in results:
        print(row)
except:
    print("Chyba při získávání informací o uživatelích.")

# Ověření kontroly vstupů
try:
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE id=%s"
    cursor.execute(query, ('1 OR 1=1',))
    results = cursor.fetchall()
    if results:
        print("Chyba - SQL injection je možný.")
    else:
        print("Kontrola vstupů proběhla v pořádku.")
except:
    print("Chyba při ověřování kontroly vstupů.")

db.close()
