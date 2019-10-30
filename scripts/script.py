import requests
import json
import collections
import re 
import argparse

from secret import accessToken

headers = {"Authorization": "bearer "+ accessToken }

topic_query = """
        query ($name:String!){
        repositoryOwner(login:$name){
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

class pullRequestsData:

    def __init__(self, username):
        self.variables=dict({
            "name":str(username)
        })
        self.data = {}

    def getPRData(self):
        request = requests.post('https://api.github.com/graphql', json={'query': topic_query,"variables":self.variables},headers=headers)
        if(request.status_code == 200):
            result = request.json()           
            if(result['data']['repositoryOwner'] != None):
                self.data['username'] = result['data']['repositoryOwner']['login']
                self.data['name'] = result['data']['repositoryOwner']['name']
                prsdata = {}
                for pr in result['data']['repositoryOwner']['pullRequests']['nodes']:
                    prdata = {}
                    if(re.match(r'^2019-10', pr['createdAt'])):
                        prdata['createdAt'] = pr['createdAt']
                        prdata['additions'] = pr['additions']
                        prdata['deletions'] = pr['deletions']
                        prsdata[pr['id']] = prdata
                self.data['prsdata'] = prsdata
            else:
                self.data['username'] = result['data']['repositoryOwner']
                
    def displayData(self):
        if(self.data['username'] != None):
            if(self.data['prsdata']):
                print(self.data)
            else:
                print("No PRs for Hacktoberfest")
        else:
            print("User doesn't exist")
        
    def returnsData(self):
        return self.data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to find stats of users individually or as a group",allow_abbrev=False)
    parser.add_argument('-u',"--username", action='store', type=str,help="Enter the username")
    parser.add_argument('-t',"--text", action='store', type=str,help="Use the text file")
    args = parser.parse_args()
    if args.username:
        prData = pullRequestsData(args.username)
        prData.getPRData()
        prData.displayData()
    elif args.text:
        usernames = [x.replace('\n', '') for x in open("{}".format(args.text), "r").readlines()]
        data=[]
        for username in usernames:
            prData = pullRequestsData(username)
            prData.getPRData()
            data.append(prData.returnsData())
        totalPRCount=0
        totalAddCount=0
        totalDelCount=0
        for item in data:
            totalPRCount=totalPRCount+len(dict(dict(item)['prsdata']).keys())
            for i in dict(item)['prsdata'].values():
                totalAddCount+=int(i['additions'])
                totalDelCount+=int(i['deletions'])
        print(totalPRCount,totalAddCount,totalDelCount)