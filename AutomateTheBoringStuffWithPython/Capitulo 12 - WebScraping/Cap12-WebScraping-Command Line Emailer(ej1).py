#Ejercicio 1: Command Line Emailer

'''
Write a program that takes an email address and string of text
on the command line and then, using selenium, logs in to your email account
and sends an email of the string to the provided address.

(You might want to set up a separate email account for this program.)

This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook or
Twitter account.

'''
#se podria pasar el input todo al inicio para que sea mas comodo
from selenium import webdriver
import sys,os,time


#print(os.getcwd())
if len(sys.argv)<3:
    print('Faltan datos')
else:
    email = sys.argv[1]
    string = sys.argv[2]

    browser = webdriver.Firefox()
    
    time.sleep(5)
    
    browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1628454288&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d05816975-529f-5d73-437e-cbac20fdedc2&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
    elem = browser.find_element_by_css_selector('#i0116')
    miMail= input('Ingrese su mail:' ) #debe ser correcto si o si
    elem.send_keys(miMail)

    elemSiguiente = browser.find_element_by_css_selector('#idSIButton9')
    elemSiguiente.click()
    
    time.sleep(5)

    elemAreaPass = browser.find_element_by_css_selector('#i0118')
    miContrasena=input('Ingrese su contraseña: ')
    elemAreaPass.send_keys(miContrasena)

    elempassNext= browser.find_element_by_css_selector('#idSIButton9')
    elempassNext.click()

    time.sleep(5)

    elemNO = browser.find_element_by_css_selector('#idBtn_Back')
    elemNO.click()

    time.sleep(10)

    elemMensajeNuevo = browser.find_element_by_css_selector('#id__7')
    elemMensajeNuevo.click()

    time.sleep(8)
    
    destinatario = browser.find_element_by_css_selector('.ms-BasePicker-input')
    destinatario.send_keys(email)
    

    time.sleep(8)

    asunto = browser.find_element_by_css_selector('#TextField251')
    asunto.send_keys('Prueba envio automatico Selenium(Python)')

    time.sleep(8)

    mensajeAenviar = browser.find_element_by_css_selector('._16VySYOFix816mo3KsgOhw')
    mensajeAenviar.send_keys(string)

    time.sleep(3)

    enviar = browser.find_element_by_css_selector('.ms-Button--primary > span:nth-child(1) > i:nth-child(1)')
    enviar.click()

    time.sleep(5)

    print('MENSAJE ENVIADO')

    browser.quit()
    
