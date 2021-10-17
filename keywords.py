from os import name
import mysql.connector
import nltk
from nltk.tokenize import word_tokenize
import speechtotext
import pyttsx3

nltk.download('punkt')
query=speechtotext.speech()

text = query
var1 = word_tokenize(text)
print(var1)

'''mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
'''
def my_function(var):
     f = 0 
     k = 0 
     for i in range (len(var)):
         if var[i] == "what" or var[i] == "where" or var[i] == "which":
             a1 = i
             f = 1
      
            
             if f == 1 :
                 for k in range (1,len(var)):
                     if var[k] == "name":
                         k = 1
                     if var[k] == "address" or var[k] == "live":
                         k = 2 
                     if var[k] == "phone":
                         k = 3

     return k
 
ques=my_function(var1)
print(ques)

if ques==1:
    pyobj=pyttsx3.init()
    pyobj.say("raj")  
    pyobj.runAndWait()
if ques==2:
    pyobj=pyttsx3.init()
    pyobj.say("10 shreshtha viha")  
    pyobj.runAndWait()

