import requests
import json
import collections
import re 

accessToken = "###################################"
headers = {"Authorization": "bearer "+ accessToken }

def getpullRequests():
    topic_query = """
    query {
    repositoryOwner(login:"iammarco11") {
        login 
        ... on User {
        name
        avatarUrl
        pullRequests(last: 100){
            nodes{
            id
            createdAt
            additions
            deletions
            }
        }
        } 
    }
    } 
    """
    request = requests.post('https://api.github.com/graphql', json={'query': topic_query}, headers=headers)
    if request.status_code == 200:
        result = request.json()
        flag = 0
        storedData = {}
        for user in result['data']['repositoryOwner']['pullRequests']['nodes']:
            TxttoCompare=user['createdAt']
            eachPr = re.match(r'^2019-10',TxttoCompare)
            if eachPr:
                flag = flag + 1
                storedData['id']=user['id']
                storedData['createdAt']=user['createdAt']
                storedData['additions']=user['additions']
                storedData['deletions']=user['deletions']
                print(storedData) #Can use this as count of PR 
        if flag == 0:
            print("No PRs made in Hacktoberfest")

if __name__ == "__main__":
    getpullRequests()