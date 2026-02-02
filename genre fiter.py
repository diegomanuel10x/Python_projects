print("This is a simple genre filter!")

rock = []
pop = []
rap = []

def genre():
    song = "Enter the song: "
    #genre of song
    gos = "Is it r(rock), p(pop) or rr(rap) or q(quit): "

    while True:
        gen = input(gos)
        if gen == "q":
            break

        elif gen == "r":
            rk = input(song)
            rock.append(rk)
            print(f"Rock:{rock}")

        elif gen == "p":
            p = input(song)
            pop.append(p)
            print(f"Pop:{pop}")

        elif gen ==  "rr":
            rr = input(song)
            rap.append(rr)
            print(f"Rap:{rap}")

        else:
            print("Invalid!")

genre()