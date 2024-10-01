# Class notes on how to use and learn loops

# for --> arrays  (lists and tuples)
# infinite loop  --> run forever

# while loop
def movieMenu(index):
    movies = [
        "Raiders of the Lost Ark",
        'Star Wars',
        'Jurassic Park',
        'Matrix',
    ]
    return movies[index]

movie_names = 0
while(movie_names < 4):
        title = movieMenu(movie_names)
        print(title)
        if(movie_names == 1):
            print("Only 2 names remaining")
        movie_names += 1         # += this is equivalent to i = i + 1