import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
q = cursor.execute("SELECT * FROM Dictionary")
data = cursor.fetchall()

output = dict(data)

def query(w):
    content = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % w)
    results = cursor.fetchall()
    return results

word = input("Enter a Word: ")
ans = query(word)

if ans:
    for r in ans:
        print(r[1])
else:
    if len(get_close_matches(word,output.keys(),cutoff=0.8)) > 0:
        x = input("Did you mean {} instead? ".format(get_close_matches(word,output.keys())[0]))
        if x == 'y' or x == 'Y':
           temp = query(get_close_matches(word,output.keys())[0])
           for t in temp:
               print(t[1])
        elif x == 'N' or x == 'n':
            print("The word doesn't exists ")
        else:
            print("Please enter Y or N ")   

    
