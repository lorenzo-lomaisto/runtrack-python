def dev_type(langage):
    if langage == "javascript":
        print("Tu es un developeur web")
    elif langage == "python":
        print("Tu es un developeur IA")
    elif langage == "java":
        print("Tu es un developpeur logiciel")
    elif langage == "reactjs":
        print("Tu es un developpeur mobile")
    else:
        print("Un jour, je serai le meilleure développeur ...")
        dev_type("javascript")
    dev_type("python")
    dev_type("java")
    dev_type("reactjs")
    dev_type("ruby")