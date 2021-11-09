print("Hi")
#import gitpath
from github import Github
from pprint import pprint
g = Github()
username=input("Enter your Github user name : \n")
user = g.get_user(username)
for repo in user.get_repos():
     print(repo.name)
content = repo.get_contents("")
for content_file in content:
     print(content_file.name)
 
 
