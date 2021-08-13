import wikipedia, requests

page = wikipedia.page("modern art")

url = page.images[0]

req = requests.get(url)
print(url)
print(req.content)
with open("image.jpg", 'wb') as file:
    file.write(req.content)
