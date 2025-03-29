def main():
    n=split_number(get_value())
    print(convert(n))
    
def get_value():
    while True:
        try :
            n=int(input("Valeur à tranformer : "))
            if  n>=4000 : 
                raise Exception 
            else: 
                return n
        except ValueError:
            pass
        except Exception:
            print("Valeur supérieure à 4000, le programme n'est prévu que pour les valeurs inférieurs à 4000\nMerci de rentrer une nouvelle valeur")
    
def convert(n):
    text_unite=romainhelp(n[0],"I","V","X")
    text_diz=romainhelp(n[1],"X","L","C")
    text_centaine=romainhelp(n[2],"C","D","M")  
    text_mil=romainhelp(n[3],"M","","")
    return text_mil+text_centaine+text_diz+text_unite

def split_number(n):
    unite = n%10
    n=n-unite
    diz = int((n%100)/10)
    n=n-diz*10
    centaine = int((n%1000)/100)
    n=n-centaine*100
    mil= int(n/1000)
    return [unite,diz,centaine,mil]

def romainhelp(n,lettre_1,lettre_5,lettre_10):
    match n:
        case 1|2|3:
            text=lettre_1*n
        case 4:
            text=lettre_1+lettre_5
        case 5:
            text=lettre_5
        case 6|7|8:
            text=lettre_5+lettre_1*(n-5)
        case 9:
            text=lettre_1+lettre_10
        case 0:
            text=""
    return text


if __name__ == "__main__" :
    main()