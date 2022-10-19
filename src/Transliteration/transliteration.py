from ISO15919toTamil import ISO15919toTamil
t=ISO15919toTamil()
def main():
    while True:
        z=input("Enter your text : ")
        print(t.iso15919_to_tamil(z))
        cont=input("Do you want to continue? (y/n) : ")
        if(cont=='y' or cont=='Y'):
            continue
        else:
            break

if __name__ == "__main__":
    main()