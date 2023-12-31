#the modules an functionalities that i needed
import json
import os
import requests
from bs4 import BeautifulSoup

tabList = []
current_index = None


def menu():
  print("Welcome to Sima's midterm answer.")
  print("Please select one of the following options from the menu:")
  print("1. Open Tab")
  print("2. Close Tab")
  print("3. Switch Tab")
  print("4. Display All Tabs")
  print("5. Open Nested Tabs")
  print("6. Sort All Tabs")
  print("7. Save Tabs")
  print("8. Import Tabs")
  print("9. Exit")


#i used the selectionSort function you taught us, changed what needed to change for my use
def selectionSort():  #O(n^2) n is the number of elements in list + it is nested
  border = 0
  while border < len(tabList) - 1:
    minIndex = border
    for i in range(border + 1, len(tabList)):
      if tabList[i]['Title'].lower() < tabList[minIndex]['Title'].lower():
        minIndex = i
    temp = tabList[border]
    tabList[border] = tabList[minIndex]
    tabList[minIndex] = temp
    border = border + 1


#we take the title and url parameters from user
#then save them in a tabList list using a built in function append
#the parameters are title, url, content(switch to html) and list nested tabs all in a dictionary
def openTab():  # O(1) user inputs are both constants
  while True:
    title = str(input("Enter the title of the website: "))
    url = input("Enter the URL of the website: ")
    if title.strip() and title.isalpha() and url.strip():

      tab = {"Title": title, "URL": url, "Content": "", "Nested Tabs": []}
      tabList.append(tab)

      current_index = len(tabList) - 1
      print("Tab opened successfully.")
      break
    else:
      print("Title and URl cannot be empty. Please try again.")


#we check if the list is not empty
#then we take the index which should be integer from the user
#if the index is in the range we use pop(a built in function to delete item from list)
#if the index is larger or smaller the program prints invalid
def closeTab():  #O(n) number of elements in list
  if len(tabList) == 0:
    print("No tabs to close.")
    return

  index = int(input("Enter the index of the tab to close: "))
  if index == '':
    tabList.pop()
    print("the last tab closed successfully.")
  elif index >= 0 and index <= len(tabList) - 1:
    tabList.pop(index)
    print("Tab closed successfully.")
  else:
    print("Invalid index.")


#check if tab is not empty
#using web scraping we display the html of the tab with index the user chose
#if the user didnt enter an index, the last page html is displayed
#all the html that is displayed is seved in content in the main list
#i learned and used beutifulsoup from geeksforgeeks from the link is below
#https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
def switchTab():  #O(1) the request to get html content from url
  index = int(input("Enter the index of the tab to display: "))
  if len(tabList) == 0:
    print("No tabs to display.")
    return

  elif index > 0 or index <= len(tabList):
    r = requests.get(tabList[index]["URL"])
    print(r.content)
    soup = BeautifulSoup(r.text, 'html.parser')
    tabList[index]['content'] = str(soup)
  elif index == "":
    r = requests.get(tabList[len(tabList) - 1]["URL"])
    print(r.content)
    soup = BeautifulSoup(r.text, 'html.parser')
    tabList[index]['content'] = str(soup)
  else:
    print("The inex you entered in sout of range!")


#using a for loop i printed the title of all the tabs in tablist
#also ive learned that i should use '' instead of ""
#i didnt really know before that there is a difference
def displayAllTabs():  #O(n) where n is tabs elements in list
  if len(tabList) == 0:
    print("No tabs to display.")
    return
  for tab in tabList:
    print(tab['Title'])
    for nested in tab['Nested Tabs']:
      print("--" + nested['Title'])


#the program reads only index to nest a spesific tab
#the title must be a string
#we append the nested into a specific tab in tablist
def openNestedTabs():  #O(1)
  index = int(
      input("Enter the index of the tab you want to add a nested tab to it: "))
  if 0 <= index <= len(tabList) - 1:
    title = str(input("Enter the title: "))
    url = input("Enter the URL: ")
    nested = {"Title": title, "URL": url}
    tabList[index]["Nested Tabs"].append(nested)
    print("Nested tab added successfully.")
  else:
    print("Invalid tab index.")


#we called the slectionsort function we learned and wrote in the beginning of the program
#then print all the list
def sortAllTabs():  #O(n^2) since it uses selectionSort()
  selectionSort()
  print(tabList)


#saveTabs was a bit challenging
#i learned and used from w3schools the link is below
#https://www.w3schools.com/python/python_file_remove.asp
#first i checked if the list in empty
#the user entered the path, using the function from w3schools i checked
#if the path exists, if it doesnt exist it creats a new on eusing x
#if it exists but the user wants to overwrite it we use w
#if it exists and the user doesnt want to overwrite then it appends using a
#we open the path as file and put it in it as json
#this was the most challenging part, but it was fairly solvable haha
def saveTabs():  #O(n) where n is the number of elements in the list
  if len(tabList) == 0:
    print("No tabs to save.")
    return
#let path always .txt
  path = str(input("Enter the file path to save the tabs in it: "))
  exists = os.path.exists(path)
  if not exists:
    mode = 'x'
    print("Creating a new file.")
  elif exists and input(
      "File already exists.overwrite it? (y/n): ").lower() == 'y':
    mode = 'w'
  else:
    mode = 'a'
    print("Appending to the existing file.")
  with open(path, mode) as f:
    json.dump(tabList, f, indent=2)
  print("Saved successfully!")


#the user enters the path
#ive learnt this from w3schools, the link is below
#open() is used to open a file in a certain way
#i used it here to open path and just read it, nothing more is allowed
#after that we print it, and then we put the cursor from the start seek(0) since
# the program just left the txt file read with the cursor at the end
#then we load to the list from file, from being json then list
def importTabs():  # O(n) the content reads content of file and loads it
  path = str(input("Enter the file path to import the tabs from it: "))
  f = open(path, "r")
  print(f.read())
  f.seek(0)
  tabList = json.load(f)


#the menu, which doesnt need any brain cells
while True:
  menu()
  choice = input("Enter your choice: ")
  if choice == "1":
    openTab()
  elif choice == "2":
    closeTab()
  elif choice == "3":
    switchTab()
  elif choice == "4":
    displayAllTabs()
  elif choice == "5":
    openNestedTabs()
  elif choice == "6":
    sortAllTabs()
  elif choice == "7":
    saveTabs()
  elif choice == "8":
    importTabs()
  elif choice == "9":
    print("Exiting program. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")
