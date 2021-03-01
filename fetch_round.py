import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver= webdriver.Firefox()
driver.maximize_window()
id=sys.argv[1]
code=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
url=""
for x in code:
    driver.get("https://codeforces.com/problemset/problem/"+id+"/"+x)
    if url!=driver.current_url:
        elements = driver.find_elements(By.TAG_NAME, 'pre')
        for i in range(len(elements)):
            if i%2==0:
                filename ="/"+id+"/"+x+"/input"+str((i//2)+1)+".txt"
            else:
                filename = "/"+id+"/"+x+"/output"+str((i+1)//2)+".txt"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(elements[i].text)
        page= driver.find_element(By.TAG_NAME, 'body')
        screenshot = page.screenshot_as_png
        filename = '/'+id+'/'+x+'/problem.png'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as img:
            img.write(screenshot)
    else:
        break
    url=driver.current_url
driver.quit()
    



