from os import system, name
from colorama import init, Fore
from getpass import getpass
import stdiomask
from time import sleep

init(autoreset=True)


def show_menu():
    print(f"""{Fore.YELLOW}\nLogin System {Fore.RESET}by {Fore.YELLOW}Elton Marques\n
{Fore.CYAN}[1] {Fore.RESET}Login into an existing account
{Fore.CYAN}[2] {Fore.RESET}Register a new account
{Fore.CYAN}[3] {Fore.RESET}Quit program""")
    while True:
        try:
            option = int(input(Fore.CYAN + '\nYour option: ' + Fore.RESET))
            if option in (1,2,3):
                break
            else:
                print(Fore.RED + f'\n[ERROR] {Fore.WHITE}Type only options 1, 2 or 3.')
        except ValueError:
            print(Fore.RED + f'\n[ERROR] {Fore.WHITE}Type only the options 1, 2 or 3.')
            
    return option


def do_login():
    login = input(Fore.YELLOW + '\nUsername: ' + Fore.RESET)
    password = stdiomask.getpass(prompt=f'{Fore.YELLOW}Password: {Fore.RESET}', mask='*')
    
    return(login, password)


def find_user(login, password):
    users = []
    try:
        with open('users.txt', 'r+', encoding='Utf-8', newline='') as file:
            for row in file:
                row = row.strip(',')
                users.append(row.split())
                
            for user in users:
                the_login = user[0]
                the_password = user[1]
                if login == the_login and password == the_password:
                    return True
            
    except FileNotFoundError:
        return False
    

def close_app():
    system('cls' if name == 'nt' else 'clear')
    sleep(0.5)
    print(Fore.MAGENTA+'\nOK')
    sleep(0.4)
    print(Fore.MAGENTA+'See you soon!')
    sleep(0.8)
    print(Fore.GREEN+'\nThe program was closed successfully')
    sleep(0.8)


while True:
    system('cls' if name == 'nt' else 'clear')
    option = show_menu()
    
    # FAZER LOGIN
    if option == 1: 
        login, password = do_login()
        user = find_user(login, password)

        if user == True:
            print(Fore.GREEN + '\nLOGIN SUCCESSFULLY!\n')
            sleep(2)
            
        else:
            print(Fore.RED + f'\n[ERROR] {Fore.WHITE}Please check the values ​​entered.\n')
            sleep(2)
            
    # CADASTRAR NOVO USUÁRIO        
    elif option == 2: 
            login, password = do_login()
            
            if login == password:
                print(Fore.RED + f'\n[ERROR] {Fore.WHITE}The password must be different from the username.\n')
                password = stdiomask.getpass(prompt=f'{Fore.YELLOW}Password: {Fore.RESET}', mask='*')
                
            user = find_user(login, password)
            if user == True:
                print(Fore.RED + f'\n[ERROR] {Fore.WHITE}The username already exists.\n')
                sleep(2)
            else:
                with open('users.txt', 'a+', encoding='Utf-8', newline='') as file:
                    file.writelines(f'{login} {password}\n')
                print(Fore.GREEN + '\nREGISTRATION SUCCESSFULLY!\n')
                sleep(2)
                
    # SAIR DO PROGRAMA
    elif option == 3:
        close_app()
        break
