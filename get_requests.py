import requests
OAUTH_TOKEN='a275d6ea683a3feec5784ca3b412e5cb9a468921'

repos = requests.get('https://api.github.com/orgs/lodash/repos?access_token=' + OAUTH_TOKEN)
json = repos.json()
pulls = dict()

for i in range(len(json)):
    name = json[i]['name']
    # each value of pulls is a list of pull requests
    # the pull requests are represented as json (dict in python)
    pulls[name] = requests.get('https://api.github.com/repos/lodash/' + name + '/pulls?access_token=' + OAUTH_TOKEN).json()


for key in pulls.keys():
    print "repo " + key + " has " + str(len(pulls[key])) + " pull requests"
