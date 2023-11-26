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
    print("Existing program. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")

def openTab():
  while True:
    title = input("Enter the title of the website: ")
    url = input("Enter the URL of the website: ")
    if title.strip() and url.strip():
      
      tab = {"Title": title, "URL": url, "Nested Tabs": []}
      tabList.append(tab)

      current_index = len(tabList) - 1
      print("Tab opened successfully.")
      break
    else:
      print("Title and URl cannot be empty. Please try again.")


def closeTab():
  if len(tabList) == 0:
    print("No tabs to close.")
    return

  index = int(input("Enter the index of the tab to close: "))
  if index >= 0 or index <= len(tabList)-1:
    tabList.pop(index)
    print("Tab closed successfully.")
  else:
    print("Invalid index.")



def switchTab():
  index = int(input("Enter the index of the tab to display: "))
  if len(tabList) == 0:
      print("No tabs to display.")
      return
  elif index > 0 or index <= len(tabList):
    r = requests.get(tabList[index]["URL"])
    print(r.content)
    soup = BeautifulSoup(r.text, 'html.parser')
    tabList[index]['content']=str(soup)
  elif index == "" :
    r = requests.get(tabList[len(tabList)-1]["URL"])
    print(r.content)
    soup = BeautifulSoup(r.text, 'html.parser')
    tabList[index]['content']=str(soup)
  else:
    print("The inex you entered in sout of range!")
