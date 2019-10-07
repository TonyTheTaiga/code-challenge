def checkMagazine(magazine, note):
    notedict = dict()
    magdict = dict()

    for x in note:
        if x in notedict.keys():
            notedict[x] = notedict[x] + 1
        else:
            notedict[x] = 1

    for x in magazine:
        if x in magdict.keys():
            magdict[x] = magdict[x] + 1
        else:
            magdict[x] = 1
 
    for key in note:
        try:
            if magdict[key] < notedict[key]:
                print('No')
                return
        except KeyError:
            print('No')
            return

    print('Yes')