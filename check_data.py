from rich import print

def take_data() : # just to take url and injection point 

    import sys # importation for the argumments

    if(len(sys.argv) >= 4) : # control if the arguments are more than three

        print("[red][-] sorry too much data ") # alert about the arguments error 

        return 0 # return 0 becouse in octoinjection.py will make a error 
    
    else : 

        url = sys.argv[1] # the first argument'll be the url 

        sqli_point = sys.argv[2] # the second argument'll be the injection point 

        return url,sqli_point # return the 2 element at octoinjection.py 



def is_it_200(url): # it's to control the status code with element the url 

    import requests # import rquest to make a GET request and check the status code 

    response = requests.get(url) # takes the satus code of url 

    status = response.status_code # takes the satus code of url

    if(status == 200 ) : # control about the satus code if it is 200

        print(f"[yellow][+] Data and status code are ok....the injection is starting") # alert that the tool is starting...

        return 200 # return the status to permitted that the code can continue 

    else : # if it is not 200

        print(f"[red][-] sorry but the status code about {url} it' not 200") # alert about the error 

        return 0 #  return 0 becouse in octoinjection.py will make a error 

