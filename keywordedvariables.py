def person(name,**data) :
    print(name)
    for i,j in data.items():
        print(i,j)
person('vicky',age =18,city = 'chennai')