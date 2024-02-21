def d():
    animal = 'elephant'
    def e():
        nonlocal animal
        animal = 'giraffe'
        print("inside nested func: " + animal)

    print("before calling nested func: " + animal)
    e()
    print("after calling nested func: " + animal)

#global variable
animal = "camel"
d()
print("global animal: " + animal)
