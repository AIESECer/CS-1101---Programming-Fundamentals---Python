karate_basic_moves = {'Positions': ['Zenku Tsu Dachi', 'Kokotsu Dachi', 'Kiba Dachi'],
                      'Punchs': ['Oi Tsuki', 'Gyaku Tsuki','Ura Ken'],
                      'Foot Techniques': ['Mae Geri', 'Mawashi Geri','Yoko Geri'] ,
                      'Blocks': ['Age Uke', 'Gedan Barai','Uchi Uke', 'Soto Uke']}

karate_basic_moves_traslation= {'Zenku Tsu Dachi':'Front Stance','Kokotsu Dachi': 'Back Stance', 'Kiba Dachi': 'Horseman Stance',
                                'Oi Tsuki':'Advancing Punch', 'Gyaki Tsuki':'Reverse Punch', 'Ura Ken':'Back Fist',
                                'Mae geri':'Front Kick', 'Mawashi Geri': 'Roundhouse Kick', 'Yoki Geri':'Side Kick',
                                'Age Uke': 'High Block', 'Gedan Barai':'Lower Level Block', 'Uchi-Uke':'Inside Block', 'Soto Uke':'Outisde Block'
                                }

choice=input("What do you want to know about Karate: 1:Basic Moves types and names | 2:Moves translation in English!")
int(choice)

if choice == '1':
    print("Karate basic moves classed by types :")
    for waza in karate_basic_moves : 
        print(waza,": ",karate_basic_moves[waza])
else:
    print("Karate basic names traslated in English :")
    for waza_name in karate_basic_moves_traslation:
        print(waza_name,": " ,karate_basic_moves_traslation[waza_name])


    
