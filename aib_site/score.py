import json


def getScoreFromJSON():
    """Gets the last score from a JSON object"""
    theFilePath = "/home/lc101/LC101CP/appsInProgress/alien_invasionOOP/aib_site/static/aib_site/json/stats.json"
    with open(theFilePath,"r") as f:
        dictObj = json.load(f)
        f.close()
    return dictObj
    
    