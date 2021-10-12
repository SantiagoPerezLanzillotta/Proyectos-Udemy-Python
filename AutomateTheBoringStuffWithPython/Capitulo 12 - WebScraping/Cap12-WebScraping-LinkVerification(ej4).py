#Ejercicio 4 : Link Verification
'''
Write a program that, given the URL of a web page, will attempt to download
every linked page on the page.

The program should flag any pages that have a 404 “Not Found” status code
and print them out as broken links.

'''
import bs4
import requests
import re

link = input('Ingrese donde desea hacer el link verification: ')

res = requests.get(link)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')

#matches = soup.findAll('a')
matches = soup.select('a[href]') # devuelve los elementos a con el atributo href

#print(matches[0].get('href'))

linksFallados = []
print(matches)
regex = re.compile('^https:')
for i in range(0, len(matches)):    
    URL=matches[i].get('href')
    #print(f'este es el {URL} url a pasar')
    #print(type(URL))
    if len(regex.findall(URL))>0:
        res = requests.get(URL)
        print(f'Codigo: {res.status_code} para {URL}')
        if res.status_code !=200:
            linksFallados.append(URL)
    else:
        linksFallados.append(URL)
        

print(linksFallados)

#agrego un regex extra para las urls que no son validas

