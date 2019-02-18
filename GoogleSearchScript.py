import webbrowser
list = []
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = input("What key word do you want to look for?")

for j in search(query, tld="co.in", num=10, stop=1, pause=2):
    list.append(j)
    print(j)

choice = int(input("Which URL would you like to open?"))
if choice < 10:
    url = list[choice]
else:
    print("Out of the range")
    
print(url)
webbrowser.open_new(url)
