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

# Importēt json moduļa
import json

# Atverot faila films.json
with open('films.json', 'r') as json_file:
    data = json.load(json_file)

# Pievienot filmu
def sort(n):
    return int(n['raiting'])

# Puslapīgi izvilkšana
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
    
    # Ievadīt izvilkšanu
    choice = input("Enter your choice (1-9): ")
    #
    # Pievienot filmu
    if choice == '1': 
        film_name = input('Ievadi filmu nosaukumu: ')
        film_raiting = input('Ievadi filmu reitingu: ')
        #Parbaudē vai filmam ir atbilstošs garums
        if len(film_name) > 2 and len(film_name) < 120:
            try:
                #Parbaudē vai filmam ir atbilstošs reitings(no 1 līdz 10)
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
    
    # Dzēst filmu
    if choice == '2':
        film_name = input('Ievadi filmu nosaukumu, kuru vēlies dzēst: ')
        checker = 0
        #pārbaudiet visus sarakstā esošo filmu nosaukumus, lai dzēst vajadzīgo
        for film in data:
            #pārbaude if films sākas ar to ko ievada lietotājs
            if film['name'].lower().startswith(film_name.lower()):
                data.remove(film)
                print('Films', film['name'], 'dzēsts')
                checker = 1
                break
        #pārbaudot, vai esam atraduši filmu saraksta 
        if checker == 0:
            print('Films nebija atrasts')
        # Atpriešu faila atkopotas izveidošana
        with open('films.json', 'w') as json_file:
            json.dump(data, json_file)
    
    # Atzīmēt filmu
    if choice == '3':
        film_name = input('Ievadi skatīto filmu: ')
        #pārbaudiet visus sarakstā esošo filmu nosaukumus, lai atrast vajadzīgo un atzīmet ar "watched"
        for i in data:
            #pārbaude if films sākas ar to ko ievada lietotājs
            if i['name'].lower().startswith(film_name.lower()):
                i['watched'] = True
                
    # Atpriešu faila atkopotas izveidošana
    with open('films.json', 'w') as json_file:
        json.dump(data, json_file)

    # Skatītie filmi
    if choice == '4':
        print('------Visi skatītie filmi------')
        #Pārlūkojiet visas sarakstā esošās filmas
        for i in data:
            #Pārbauda, ​​vai atlasītā filma ir skatīta
            if i['watched'] == True:
                print('Nosaukums:', i['name'],'; Raitings:', i['raiting'])
                
    # Nenoskatītie filmi
    if choice == '5':
        print('------Visi nenoskatītie filmi------')
        #Pārlūkojiet visas sarakstā esošās filmas
        for i in data:
            #Pārbauda, ​​vai atlasītā filma ir nenoskatīta
            if i['watched'] == False:
                print('Nosaukums:', i['name'],'; Raitings:', i['raiting'])
                
    #TOP 10 FILMAS
    if choice == '6':
        limiter = 0
        print('------TOP 10 FILMAS------')
        data.sort(key = sort, reverse=True)
        #Pārlūkojiet visas sarakstā esošās filmas
        for i in data:
            #Pārbaudām, vai esam jau izlaiduši 10 filmas
            if limiter < 10:
                print(i)
                limiter += 1
    # Meklēt filmu
    if choice == '7':
        is_film_there = 0
        film_name = input('Meklēt filmu: ')
        #Pārlūkojiet visas sarakstā esošās filmas
        for i in data:
            #pārbaude if films sākas ar to ko ievada lietotājs
            if i['name'].lower().startswith(film_name.lower()):
                #Pārbauda, ​​vai iepriekš esam rādījuši vismaz 1 filmu, lai uzraksts neatkārtotos divas reizes
                if is_film_there == 0:
                    print('Jūsu films:')
                print(i)
                is_film_there += 1
        #Pārbauda, ​​vai iepriekš esam rādījuši vismaz 1 filmu, lai paziņot lietotājam, ka filma nav atrasta
        if is_film_there == 0:
            print('Filma nav atrasts!')
    # Iztukšot sarakstu
    if choice == '8':
        data.clear()
        with open('films.json', 'w') as json_file:
            json.dump(data, json_file)
        print('Saraksts ir tukšs!')
        
    # Iziet
    if choice == '9':
        print('Exiting...')
        break