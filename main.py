import pandas

data=pandas.read_csv("data.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}

ask_user=True
while ask_user: 
    user_input=input("Enter a word: ").upper()
    try:
        result=[phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        ask_user=False
            

print(result)