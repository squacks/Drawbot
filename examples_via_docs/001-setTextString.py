# font('LucidaGrande', 100)
# text('Hello World!', (100, 200))

#clr1 = 1, .35, .21
#clr2 = .41, .05, 0

for eachFontName in installedFonts(supportsCharacters='ЉДЖ'):
    print(eachFontName)

# newPage(200, 200)
# text('a quick brown', (30, 80))
# fontSize(20)
# text('fox jumps over', (30, 40))



someText= """Considerare l’esistenza di un insieme di strumenti convenzionali di organizzazione e interpretazione dello spazio concatenati, il quale in qualche modo interagisca con la lingua parlata, è utile perché conviene dal punto di vista progettuale"""
newPage(200, 200)

fill(1, .35, .21)
rect(0, 0, 200, 200)


font("BlenderPro-Heavy", 16)
fill(.4156, .0588, .0039)
textBox(someText, (20, 30, 150, 150), align='left')


