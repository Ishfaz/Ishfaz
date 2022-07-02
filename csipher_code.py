alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caeser(start_text, shift_amount, cispher_direction):
    end_text=""
    if cispher_direction=="decode":
           shift_amount=shift_amount*(-1)
    for char in start_text:
        if char in alphabet:
          position=alphabet.index(char) 
          new_position=position + shift_amount
          end_text+=alphabet[new_position]
        else:
            end_text +=char
    
    print(f"{cispher_direction}d text is {end_text}")
    ################################################################## continuity################################
should=True
while should:
    direction =input("Type encode for encrypt and decode for decrypt:\n")
    text=input("enter the the text:\n").lower()
    shift=int(input("enter the shift_amount:\n"))
    shift=shift % 26
    caeser(start_text =text, shift_amount =shift, cispher_direction=direction)
    result=input("Type 'yes' if you want to go again. Otherwise type 'No'.\n")
    if result=="no":
        should=False
        print("Good bye")
