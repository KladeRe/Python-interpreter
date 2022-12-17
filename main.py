import interpreter

def main():
    while True:
        text = input("> ")
        if (text.lower() == "exit"):
            break
        result, error = interpreter.execute("stdfn", text)
        if error:
            print(error)
        else:
            print(result)





if __name__=="__main__":
    main()