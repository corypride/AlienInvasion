import json
from aib_site.static.aib_site.py_code.alien_invasion.communication import systemFilePath

def getScoreFromJSON():
    """Gets the last score from a JSON object"""
    theFilePath = systemFilePath+"alien_invasionOOP/aib_site/static/aib_site/json/stats.json"
    with open(theFilePath,"r") as f:
        dictObj = json.load(f)
        f.close()
    return dictObj
    
    