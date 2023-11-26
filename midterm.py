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


def selectionSort(): #O(n^2) n is the number of elements in list
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


def openTab(): # O(1) user inputs are both constants
  while True:
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    if title.strip() and url.strip():

      tab = {"Title": title, "URL": url, "Content": "", "Nested Tabs": []}
      tabList.append(tab)

      current_index = len(tabList) - 1
      print("Tab opened successfully.")
      break
    else:
      print("Title and URl cannot be empty. Please try again.")


def closeTab(): #O(n) number of elements in list
  if len(tabList) == 0:
    print("No tabs to close.")
    return

  index = int(input("Enter the index of the tab to close: "))
  if index >= 0 or index <= len(tabList) - 1:
    tabList.pop(index)
    print("Tab closed successfully.")
  else:
    print("Invalid index.")


def switchTab(): #O(1) the request to get html content from url
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


def displayAllTabs():
  if len(tabList) == 0:
    print("No tabs to display.")
    return
  for tab in tabList:
    print(tab['Title'])
    for nested in tab['Nested Tabs']:
      print("--" + nested['Title'])


def openNestedTabs():
  index = int(
      input("Enter the index of the tab you want to add a nested tab to it: "))
  if 0 <= index <= len(tabList) - 1:
    title = input("Enter the title: ")
    url = input("Enter the URL: ")
    nested = {"Title": title, "URL": url}
    tabList[index]["Nested Tabs"].append(nested)
    print("Nested tab added successfully.")
  else:
    print("Invalid tab index.")


def sortAllTabs():
  selectionSort()
  print(tabList)


def saveTabs():
  if len(tabList) == 0:
    print("No tabs to save.")
    return

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


def importTabs():
  path = str(input("Enter the file path to import the tabs from it: "))
  f = open(path, "r")
  print(f.read())
  f.seek(0)
  tabList = json.load(f)

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
