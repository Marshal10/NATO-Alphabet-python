import pandas

data=pandas.read_csv("data.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}

user_input=input("Enter a word: ").upper()
result=[phonetic_dict[letter] for letter in user_input]
print(result)