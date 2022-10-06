#======================================
#Nombre del estudiante: Paula Rodríguez
#Carnet: 20221110264
#======================================
anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy x Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}
historial=[]
while True:
    option=input("Please select the action you wish to complete: \n1. Select the TV series you wish to watch \n2. Consult history \n3. Exit \n--->")
    while not option.isnumeric():
        print("Invalid option.")
        option=input("Please select the action you wish to complete: \n1. Select the TV series you wish to watch \n2. Consult history \n3. Exit \n--->")
    while int(option)<1 or int(option)>3:
        print("Invalid option.")
        option=input("Please select the action you wish to complete: \n1. Select the TV series you wish to watch \n2. Consult history \n3. Exit \n--->")
    option=int(option)
    if option==1:
        num=1
        for anime_available,information in anime.items():
            print(f"{num}. {anime_available}")
            num+=1
        series_selected=input("Please select the anime you wish to watch: \n--->")
        while not series_selected.isnumeric():
            print("Invalid option.")
            series_selected=input("Please select the anime you wish to watch: \n--->")
        while int(series_selected)<1 or int(series_selected)>3:
            print("Invalid option.")
            series_selected=input("Please select the anime you wish to watch: \n--->")
        series_selected=int(series_selected)
        if series_selected==1:
            series_selected="Demon Slayer"
            for anime_available,information in anime.items():
                for season,episodes in information.items():
                        if series_selected==anime_available:
                            print(f"*{season}")
            season_selected=input("Please enter the season you wish to watch: ")
            while not season_selected.isnumeric():
                print("Invalid option.")
                season_selected=input("Please select the season you wish to watch: \n--->")
            while int(season_selected)<1 or int(season_selected)>2:
                print("Invalid option.")
                season_selected=input("Please select the season you wish to watch: \n--->")
            if season_selected==1:
                season_selected="Temporada 1"
            else:
                season_selected="Temporada 2"
            for anime_available,information in anime.items():
                for season,episodes in information.items():
                    if series_selected==anime_available:
                        for episode in episodes:
                            if season_selected==season:
                                print(f"*{episode}")
            episode_selected=input("Please select the episodes you wish to watch: ")
            while not episode_selected.isnumeric():
                print("Invalid option.")
                episode_selected=input("Please select the episodes you wish to watch: \n--->")
            episode_selected=int(episode_selected)
            for anime_available,information in anime.items():
                    for season,episodes in information.items():
                        if series_selected==anime_available:
                            for episode in episodes:
                                if episode["cap"]==episode_selected:
                                    historial.append(episode)
        elif series_selected==2:
            series_selected="Spy x Family"
            for anime_available,information in anime.items():
                for season,episodes in information.items():
                        if series_selected==anime_available:
                            print(f"*{season}")
                            print(f"*{episodes}")
            episode_selected=input("Please select the episode you wish to watch: ")
            while not episode_selected.isnumeric():
                print("Invalid option.")
                episode_selected=input("Please select the episode you wish to watch: \n--->")
            episode_selected=int(episode_selected)
            if episode_selected==4 or episode_selected==7:
                for anime_available,information in anime.items():
                    for season,episodes in information.items():
                        if series_selected==anime_available:
                            for episode in episodes:
                                if episode["cap"]==episode_selected:
                                    historial.append(episode)
        else:
            series_selected="Attack on Titan"
            for anime_available,information in anime.items():
                for season,episodes in information.items():
                    if series_selected==anime_available:
                        print(f"*{season}")
            season_selected=input("Please enter the season you wish to watch: ")
            while not season_selected.isnumeric():
                print("Invalid option.")
                season_selected=input("Please select the season you wish to watch: \n--->")
            if int(season_selected)==3:
                season_selected="Temporada 3"
            elif int(season_selected)==4:
                season_selected="Temporada 4"
            for anime_available,information in anime.items():
                for season,episodes in information.items():
                    if series_selected==anime_available:
                        for episode in episodes:
                            if season_selected==season:
                                print(f"*{episode}")
            episode_selected=input("Please select the episodes you wish to watch: ")
            while not episode_selected.isnumeric():
                print("Invalid option.")
                episode_selected=input("Please select the episodes you wish to watch: \n--->")
            episode_selected=int(episode_selected)
            for anime_available,information in anime.items():
                    for season,episodes in information.items():
                        if series_selected==anime_available:
                            for episode in episodes:
                                if episode["cap"]==episode_selected:
                                    historial.append(episode)
    elif option==2:
        print(f"Your watch history is: {historial}.")
        print(f"You have watched {len(historial)} episodes.")
    else:
        print("Thank you for preferring us!")
        break