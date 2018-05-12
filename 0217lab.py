music=[("Thriller","Michael Jackson","Pop","1982"),
       ("Back in Black","AC/DC","Rock","1980"),
       ("The Dark Side of the Moon","Pink Floyd","Rock","1973"),
       ("The Bodyguard","Whitney Houston","R&B","1992")]
output="{1:>15} {1:>25} {2:>15} {3:>15}"

print(output.format("Title","Artist","Genre","Year")

for i in music:   
    Album, Artist, Genre, Year=i
    print(output.format(Album, Artist, Genre, Year,sep="\t")
