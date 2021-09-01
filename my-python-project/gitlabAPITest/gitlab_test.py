import requests

response = requests.get("http://gitlab.com/api/v4/users/nanuchi/projects")
print(response)
print(response.json())
print(response.json()[0])
print(response.text)
print(type(response.text))


my_projects = response.json()

for project in my_projects:
    print(f"Propject name: {project['name']} Project Url {project['web_url']}")