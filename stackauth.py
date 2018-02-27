import re
from robobrowser import RoboBrowser
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import json

br= RoboBrowser()
br.open("https://stackoverflow.com/users/login?")
form = br.get_form(id="login-form")
print(form)
print("Enter the email address:")
form['email'] = input()
print("Enter the password:")
form['password'] = input()
br.submit_form(form)

#To check whether you are been logged in properly or not!!
def make_soup(url):
	headers= {}
	headers['User-Agent']= "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	req=urllib.request.Request(url, headers=headers)
	page= urllib.request.urlopen(req)
	soupdata = BeautifulSoup(page, "html.parser")
	return soupdata
soup= make_soup("https://stackoverflow.com/questions")
t= soup.find("div", {"class": "-actions"})
a= t.get_text()
#print(a)
print("You are logged in! ")