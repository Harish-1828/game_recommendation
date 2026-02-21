"""
Games Database - Curated Steam Games Collection
This module contains a comprehensive database of popular Steam games
"""

GAMES_DATABASE = [
    {
        "id": 1,
        "name": "The Witcher 3: Wild Hunt",
        "genre": "RPG",
        "price": 3299,
        "rating": 97,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/292030/header.jpg",
        "description": "As war rages on throughout the Northern Realms, you take on the greatest contract of your life — tracking down the Child of Prophecy, a living weapon that can alter the shape of the world.",
        "tags": ["RPG", "Open World", "Story Rich", "Fantasy"],
        "release_date": "2015-05-18"
    },
    {
        "id": 2,
        "name": "Cyberpunk 2077",
        "genre": "RPG",
        "price": 4999,
        "rating": 78,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1091500/header.jpg",
        "description": "An open-world, action-adventure story set in Night City, a megalopolis obsessed with power, glamour and body modification.",
        "tags": ["RPG", "Cyberpunk", "Open World", "Futuristic"],
        "release_date": "2020-12-10"
    },
    {
        "id": 3,
        "name": "Elden Ring",
        "genre": "Action",
        "price": 4999,
        "rating": 92,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1245620/header.jpg",
        "description": "Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
        "tags": ["Souls-like", "RPG", "Dark Fantasy", "Difficult"],
        "release_date": "2022-02-25"
    },
    {
        "id": 4,
        "name": "Counter-Strike 2",
        "genre": "FPS",
        "price": 0,
        "rating": 85,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/header.jpg",
        "description": "For over two decades, Counter-Strike has offered an elite competitive experience, one shaped by millions of players from across the globe.",
        "tags": ["FPS", "Competitive", "Multiplayer", "Tactical"],
        "release_date": "2023-09-27"
    },
    {
        "id": 5,
        "name": "Red Dead Redemption 2",
        "genre": "Action",
        "price": 4999,
        "rating": 89,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1174180/header.jpg",
        "description": "America, 1899. The end of the Wild West era has begun. After a robbery goes badly wrong, Arthur Morgan and the Van der Linde gang are forced to flee.",
        "tags": ["Open World", "Story Rich", "Western", "Action"],
        "release_date": "2019-11-05"
    },
    {
        "id": 6,
        "name": "Baldur's Gate 3",
        "genre": "RPG",
        "price": 4999,
        "rating": 96,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1086940/header.jpg",
        "description": "Gather your party and return to the Forgotten Realms in a tale of fellowship and betrayal, sacrifice and survival, and the lure of absolute power.",
        "tags": ["RPG", "D&D", "Turn-Based", "Story Rich"],
        "release_date": "2023-08-03"
    },
    {
        "id": 7,
        "name": "Hogwarts Legacy",
        "genre": "RPG",
        "price": 4999,
        "rating": 84,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/990080/header.jpg",
        "description": "Experience Hogwarts in the 1800s. Your character is a student who holds the key to an ancient secret that threatens to tear the wizarding world apart.",
        "tags": ["Magic", "Open World", "RPG", "Adventure"],
        "release_date": "2023-02-10"
    },
    {
        "id": 8,
        "name": "God of War",
        "genre": "Action",
        "price": 4149,
        "rating": 94,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1593500/header.jpg",
        "description": "Enter the Norse realm. His vengeance against the Gods of Olympus years behind him, Kratos now lives as a man in the realm of Norse Gods and monsters.",
        "tags": ["Action", "Mythology", "Story Rich", "Hack and Slash"],
        "release_date": "2022-01-14"
    },
    {
        "id": 9,
        "name": "Stardew Valley",
        "genre": "Simulation",
        "price": 1249,
        "rating": 98,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg",
        "description": "You've inherited your grandfather's old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life.",
        "tags": ["Farming", "Pixel Art", "Relaxing", "Indie"],
        "release_date": "2016-02-26"
    },
    {
        "id": 10,
        "name": "Hades",
        "genre": "Roguelike",
        "price": 2079,
        "rating": 95,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1145360/header.jpg",
        "description": "Defy the god of the dead as you hack and slash out of the Underworld in this rogue-like dungeon crawler.",
        "tags": ["Roguelike", "Indie", "Action", "Greek Mythology"],
        "release_date": "2020-09-17"
    },
    {
        "id": 11,
        "name": "Terraria",
        "genre": "Sandbox",
        "price": 829,
        "rating": 96,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg",
        "description": "Dig, fight, explore, build! Nothing is impossible in this action-packed adventure game.",
        "tags": ["Sandbox", "2D", "Building", "Survival"],
        "release_date": "2011-05-16"
    },
    {
        "id": 12,
        "name": "Minecraft",
        "genre": "Sandbox",
        "price": 2239,
        "rating": 93,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1086940/header.jpg",
        "description": "Explore randomly generated worlds and build amazing things from the simplest of homes to the grandest of castles.",
        "tags": ["Sandbox", "Survival", "Crafting", "Building"],
        "release_date": "2011-11-18"
    },
    {
        "id": 13,
        "name": "Grand Theft Auto V",
        "genre": "Action",
        "price": 2499,
        "rating": 88,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/271590/header.jpg",
        "description": "When a young street hustler, a retired bank robber and a terrifying psychopath find themselves entangled with some of the most frightening and deranged elements, they must pull off a series of dangerous heists to survive.",
        "tags": ["Open World", "Action", "Crime", "Multiplayer"],
        "release_date": "2015-04-14"
    },
    {
        "id": 14,
        "name": "Portal 2",
        "genre": "Puzzle",
        "price": 829,
        "rating": 97,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/620/header.jpg",
        "description": "The sequel to 2007's Game of the Year, Portal 2 is a hilariously mind-bending adventure that challenges you to use wits over weaponry.",
        "tags": ["Puzzle", "Co-op", "Sci-fi", "First-Person"],
        "release_date": "2011-04-18"
    },
    {
        "id": 15,
        "name": "Dark Souls III",
        "genre": "Action",
        "price": 4999,
        "rating": 91,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/374320/header.jpg",
        "description": "As fires fade and the world falls into ruin, journey into a universe filled with more colossal enemies and environments.",
        "tags": ["Souls-like", "Difficult", "RPG", "Dark Fantasy"],
        "release_date": "2016-04-11"
    },
    {
        "id": 16,
        "name": "Hollow Knight",
        "genre": "Metroidvania",
        "price": 1249,
        "rating": 97,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/367520/header.jpg",
        "description": "Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom of insects and heroes.",
        "tags": ["Metroidvania", "Indie", "2D", "Difficult"],
        "release_date": "2017-02-24"
    },
    {
        "id": 17,
        "name": "Among Us",
        "genre": "Party",
        "price": 415,
        "rating": 79,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/945360/header.jpg",
        "description": "An online and local party game of teamwork and betrayal for 4-15 players...in space!",
        "tags": ["Multiplayer", "Social Deduction", "Casual", "Party"],
        "release_date": "2018-11-16"
    },
    {
        "id": 18,
        "name": "Sekiro: Shadows Die Twice",
        "genre": "Action",
        "price": 4999,
        "rating": 91,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/814380/header.jpg",
        "description": "Carve your own clever path to vengeance in this evolution of the Dark Souls combat.",
        "tags": ["Souls-like", "Difficult", "Action", "Ninja"],
        "release_date": "2019-03-21"
    },
    {
        "id": 19,
        "name": "Valheim",
        "genre": "Survival",
        "price": 1659,
        "rating": 89,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/892970/header.jpg",
        "description": "A brutal exploration and survival game for 1-10 players, set in a procedurally-generated purgatory inspired by viking culture.",
        "tags": ["Survival", "Open World", "Co-op", "Viking"],
        "release_date": "2021-02-02"
    },
    {
        "id": 20,
        "name": "It Takes Two",
        "genre": "Co-op",
        "price": 3319,
        "rating": 94,
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1426210/header.jpg",
        "description": "Embark on the craziest journey of your life in It Takes Two, a genre-bending platform adventure created purely for co-op.",
        "tags": ["Co-op", "Adventure", "Puzzle", "Platformer"],
        "release_date": "2021-03-26"
    }
]

def get_all_games():
    """Return all games in the database"""
    return GAMES_DATABASE

def get_game_by_id(game_id):
    """Get a specific game by ID"""
    for game in GAMES_DATABASE:
        if game["id"] == game_id:
            return game
    return None

def search_games(query):
    """Search games by name, genre, or tags"""
    query = query.lower()
    results = []
    for game in GAMES_DATABASE:
        if (query in game["name"].lower() or 
            query in game["genre"].lower() or 
            any(query in tag.lower() for tag in game["tags"])):
            results.append(game)
    return results

def get_games_by_genre(genre):
    """Get all games of a specific genre"""
    return [game for game in GAMES_DATABASE if game["genre"] == genre]

def get_all_genres():
    """Get list of all unique genres"""
    return list(set(game["genre"] for game in GAMES_DATABASE))
