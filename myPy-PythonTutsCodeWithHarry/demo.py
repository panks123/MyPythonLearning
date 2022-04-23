
import requests
import socket
from bs4 import BeautifulSoup



def getData(url):
    '''for getting data from url'''
    r=requests.get(url)
    # print(r.text)
    return  r.text


if __name__=='__main__':

    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        print("No internet")
        exit()
    else:
        myHtmlData = getData("https://prsindia.org/covid-19/cases")

        soup = BeautifulSoup(myHtmlData, 'html.parser')

        record=[]

        for tr in soup.find_all('tbody')[0].find_all('tr'):
            li=[]
            for td in tr.find_all('td'):
                li.append(td.get_text())
            record.append(li)

        print(record,end='\n\n')

    state=[]
    confirmed=[]
    active=[]
    discharged=[]
    deaths=[]

    for item in record:
        state.append(item[1])
    print(state)
    
    print('\n')
    for item in record:
        confirmed.append(item[2])
    print(confirmed)
    
    print('\n')
    for item in record:
        active.append(item[3])
    print(active)
    
    print('\n')
    for item in record:
        discharged.append(item[4])
    print(discharged)

    print('\n')
    for item in record:
        deaths.append(item[5])
    print(deaths)
        

    

# record=[['s.no.','State',confimed cases','Active cases','Discarged','Deaths']]