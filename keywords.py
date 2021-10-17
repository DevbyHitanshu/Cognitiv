from os import name
from re import L
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
query1=speechtotext.speech()

text = query1
var2 = word_tokenize(text)
print(var2)
def my1_function(var):
     J = 0 
     L = 0 
     for i in range (len(var)):
         if ques==1 and var[i] == "tiger" :
             J = 1
         elif ques==1 :
             J = 4
         if ques==2 and var[i] == "A" and var[i+1] == "street" and var[i+2] == "delhi" and var[i+3] == "India" :
             J = 2
         elif ques==2:
             J = 5
         if ques==3 and var[i] == "782-717-6615" :
             J = 3
         elif ques==3:
             J = 6

            
             
     return J

ans=my1_function(var2)
print(ans)

if ans==4:
    pyobj=pyttsx3.init()
    pyobj.say("Tiger woods")  
    pyobj.runAndWait()
if ans==5:
    pyobj=pyttsx3.init()
    pyobj.say("a Street Delhi India")  
    pyobj.runAndWait()
if ans==6:
    pyobj=pyttsx3.init()
    pyobj.say("7827176615")
    pyobj.runAndWait()


