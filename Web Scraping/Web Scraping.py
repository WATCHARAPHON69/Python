import  requests
from bs4 import  BeautifulSoup
url = "https://docs.google.com/forms/d/1BPvXCcQ3KyA1KWdFz-dK_Lj0lUA-6zndghXvkmF3JxM/edit#responses"

web_data = requests.get(url)
print(web_data.text)
soup = BeautifulSoup(web_data.text,'html.parser')
fin_word = soup.find_all('div',{'class':'freebirdCommonAnalyticsTextResponse'})
for i in fin_word:
    print(i)