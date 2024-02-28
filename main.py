# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import json

with open('films.json', 'r') as json_file:
    data = json.load(json_file)

def sort(n):
    return int(n['raiting'])

while True:
    print('')
    print('1. pievienot filmu')
    print('2. dzēst filmu no saraksta')
    print('3. atzīmēt filmu kā skatīto')
    print('4. atfiltrēt noskatītas filmas')
    print('5. atfiltrēt nenoskatītas filmas')
    print('6. top 10 filmas pec reitinga')
    print('7. meklēt filmu pēc nosaukuma daļas')
    print('8. iztukšot sarakstu')
    print('9. Exit')
    
    choice = input("Enter your choice (1-9): ")
    if choice == '1': 
        film_name = input('Ievadi filmu nosaukumu: ')
        film_raiting = input('Ievadi filmu reitingu: ')
        if len(film_name) > 2 and len(film_name) < 120:
            try:
                if int(film_raiting) > 0 and int(film_raiting) < 11:
                    data.append({"name": film_name, "raiting": film_raiting, "watched": False})
                else:
                    print('Reitingam jābūt veselam skaitļiam no 1 līdz 10')
            except:
                print('Reitingam jābūt veselam skaitļiam no 1 līdz 10')
        else:
            print('Nosaukums ir pārāk liels vai mazs')
    with open('films.json', 'w') as json_file:
        json.dump(data, json_file)
    
    if choice == '2':
        film_name = input('Ievadi filmu nosaukumu, kuru vēlies dzēst: ')
        a = 0
        for film in data:
            if film['name'].lower().startswith(film_name.lower()):
                data.remove(film)
                print('Films', film['name'], 'dzēsts')
                a = 1
                break
        if a == 0:
            print('Films nebija atrasts')
    with open('films.json', 'w') as json_file:
        json.dump(data, json_file)
    
    if choice == '3':
        film_name = input('Ievadi skatīto filmu: ')
        for i in data:
            if i['name'].lower().startswith(film_name.lower()):
                print('da')
                i['watched'] = True
                
    with open('films.json', 'w') as json_file:
        json.dump(data, json_file)

    if choice == '4':
        print('------Visi skatītie filmi------')
        for i in data:
            if i['watched'] == True:
                print('Nosaukums:', i['name'],'; Raitings:', i['raiting'])
                
    if choice == '5':
        print('------Visi nenoskatītie filmi------')
        for i in data:
            if i['watched'] == False:
                print('Nosaukums:', i['name'],'; Raitings:', i['raiting'])
                
    if choice == '6':
        print('------TOP 10 FILMAS------')
        
    if choice == '9':
        print('Exiting...')
        break