import numpy as np

clubs_data = np.array([
    ["Arsenal", "Red", "London"], ["Aston Villa", "Blue", "Birmingham"],
    ["Bournemouth", "Red", "Bournemouth"], ["Brentford", "Red", "London"],
    ["Brighton", "Blue", "Brighton"], ["Burnley", "Claret", "Burnley"],
    ["Chelsea", "Blue", "London"], ["Crystal Palace", "Blue", "London"],
    ["Everton", "Blue", "Liverpool"], ["Fulham", "White", "London"],
    ["Leeds United", "White", "Leeds"], ["Liverpool", "Red", "Liverpool"],
    ["Manchester City", "Blue", "Manchester"], ["Manchester United", "Red", "Manchester"],
    ["Newcastle", "Black", "Newcastle"], ["Nottingham Forest", "Red", "Nottingham"],
    ["Sunderland", "Red", "Sunderland"], ["Tottenham", "White", "London"],
    ["West Ham", "Claret", "London"], ["Wolves", "Yellow", "Wolverhampton"]
])

squads = {
    "Arsenal": ["Saka", "Odegaard", "Rice", "Saliba", "Gyokeres", "Zubimendi", "Eze"],
    "Aston Villa": ["Watkins", "McGinn", "Martinez", "Tielemans", "Tammy Abraham", "Douglas Luiz"],
    "Bournemouth": ["Kroupi", "Evanilson", "Adams", "Kluivert", "Kerkez", "Fraser Forster"],
    "Brentford": ["Igor Thiago", "Mbeumo", "Jensen", "Collins", "Kaye Furo", "Jordan Henderson"],
    "Brighton": ["Joao Pedro", "Mitoma", "Dunk", "Verbruggen", "Pascal Gross", "Rutter"],
    "Burnley": ["Flemming", "Foster", "Cullen", "James Ward-Prowse", "Martin Dubravka"],
    "Chelsea": ["Joao Pedro", "Palmer", "James", "Fernandez", "Cucurella", "Yisa Alao"],
    "Crystal Palace": ["Mateta", "Wharton", "Brennan Johnson", "Evann Guessand", "Henderson"],
    "Everton": ["Pickford", "Tarkowski", "Thierno Barry", "Calvert-Lewin", "Tyrique George"],
    "Fulham": ["Wilson", "Jimenez", "Cairney", "Oscar Bobb", "Adama Traore", "Leno"],
    "Leeds United": ["Calvert-Lewin", "Ampadu", "Aaronson", "Lukas Nmecha", "James"],
    "Liverpool": ["Salah", "Van Dijk", "Hugo Ekitike", "Florian Wirtz", "Alexander Isak"],
    "Manchester City": ["Haaland", "Foden", "Semenyo", "Marc Guehi", "Grealish", "Donnarumma"],
    "Manchester United": ["Fernandes", "Mainoo", "Mbeumo", "Matheus Cunha", "Yoro", "Stefan Ortega"],
    "Newcastle": ["Guimaraes", "Gordon", "Isak", "Ramsey", "Antony Elanga", "Ramsdale"],
    "Nottingham Forest": ["Anderson", "Gibbs-White", "Wood", "Stefan Ortega", "Luca Netz"],
    "Sunderland": ["Roefs", "Xhaka", "Isidor", "Brian Brobbey", "Jocelin Ta Bi", "Melker Ellborg"],
    "Tottenham": ["Son", "Romero", "Maddison", "Conor Gallagher", "Joao Palhinha"],
    "West Ham": ["Bowen", "Kudus", "Kilman", "Adama Traore", "Taty Castellanos"],
    "Wolves": ["Cunha", "Toti", "Gomes", "Adam Armstrong", "Angel Gomes", "Pedro Lima"]
}


def guess_club():
    current_options = clubs_data
    print("25/26 Premier League Club Guesser")

    color = input("Fav colour (Red, Blue, White, Claret, Black, Yellow): ").strip().capitalize()
    current_options = current_options[current_options[:, 1] == color]
    if len(current_options) <= 1: return finalize(current_options)

    city_list = np.unique(current_options[:, 2])
    city = input(f"Fav city ({', '.join(city_list)}): ").strip().capitalize()
    current_options = current_options[np.char.find(current_options[:, 2], city) >= 0]
    if len(current_options) <= 1: return finalize(current_options)

    player = input("Fav prem player: ").strip().lower()
    final_matches = []
    for club in current_options[:, 0]:
        if any(player in p.lower() for p in squads.get(club, [])):
            final_matches.append(club)

    finalize(np.array(final_matches))


def finalize(options):
    if options.ndim == 0 or len(options) == 0:
        print("\nNo clubs found. Check your 2026 squad knowledge!")
    elif len(options) == 1:
        name = options[0, 0] if options.ndim > 1 else options[0]
        print(f"\nYou support {name}!")
    else:
        names = options[:, 0] if options.ndim > 1 else options
        print(f"\nCould be: {', '.join(names)}")


if __name__ == "__main__":
    guess_club()
