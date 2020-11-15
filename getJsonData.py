import requests
import json, csv, os     
from requests.auth import HTTPBasicAuth

'''
Function Name : getproject(url,pat)
Function Args : url = URL from which we want to get data
                pat = Personal Access token
Description   : This function takes URL, PAT as the arguements and gets the data from URL
Return Value  : Returns JSON data on successful server connection
'''
def getproject(url,pat):
    
    #Make a request to URL using authentication token
    response = requests.get(url, auth=HTTPBasicAuth(username='',password=pat))
    
    if response.status_code == 200:
        print("\nSuccessfully connected to server...")
        json_data = response.json()
        return json_data

    else:
        print("ERROR : Unable to connect the server")


        
if __name__ == '__main__':
   
    token = 'df2xk47s2eynuc2mafpci3e6phuvmufpxmlxhsqmtga6c6hussqa'
        
    url = "https://dev.azure.com/akankshakothariazure/_apis/git/repositories?api-version=6.0"

            #call "getproject" function to check url and token to further create required csv
    data = getproject(url,token)
	
    val = data['value']

    for i in val:
        print(i,"\n")