from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

digits=["0","1","2","3","4","5","6","7","8","9"]
def readNumber(l,a):
    i=a+1
    #assert: l[a:i] is the first digit of a number.
    for i in range(a+1,len(l)):
        #Invariant : l[a:i] is a string of digits of a float number.
        if l[i] not in digits:
            return(float(l[a:i]),i) 
    #assert: l[a:i] contains number, i is the index just after the no. OR the no. continues to the end of the list.
    return(float(l[a:]),len(l))
username= input("Please enter username/email\n")
password=input("Please enter password\n")
captcha=0
driver= webdriver.Firefox()
driver.get("https://moodle.iitd.ac.in/login/index.php")
text = driver.find_element_by_id("login").text
for i in range(len(text)):
    if text[i] in digits:
        break
n1=readNumber(text,i)[0]
index2=readNumber(text,i)[1]
n2=readNumber(text,index2+3)[0]
words=text.split(" ")
for x in words:
    if x =="add":
        captcha=n1+n2
    elif x=="subtract":
        captcha=n1-n2
    elif x=="first":
        captcha=n1
    elif x=="second":
        captcha=n2
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("valuepkg3").send_keys(Keys.BACK_SPACE)
driver.find_element_by_id("valuepkg3").send_keys(str(captcha))
driver.find_element_by_id("loginbtn").click()


