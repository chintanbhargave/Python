This project consists of a Dictionary app in which if we entered a word it will give its meaning.

code.py file code loads the whole json file in which all the words and their meaning is stored, everytime we run the code.
Loading the code everytime is not very suitable when we deal with the large amount of data.
Therefore in the MysqlDict.py all the data is stored in the database and accessed by creating a mysql connector.