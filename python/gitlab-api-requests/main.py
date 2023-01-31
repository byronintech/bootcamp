import requests

response = requests.get("https://gitlab.com/api/v4/users/bkintech/projects")
my_projects = response.json()

print("-----" * 15)
print("API Response:")
print(response.json()[0])

for project in my_projects:
    project_name = project["name"]
    project_url = project["web_url"]
    
    print("-----" * 15)
    print(f"Project Name: {project_name}\nProject Url: {project_url}")
