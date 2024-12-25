questions = [
  ["What is the capital of Japan?", "Tokyo", "Kyoto", "Osaka", "Hokkaido", 1],

["Which planet is known as the Red Planet?", "Venus", "Mars", "Earth", "Saturn", 2],

["Who wrote the play 'Romeo and Juliet'?", "Shakespeare", "Dickens", "Hemingway", "Tolkien", 1],

["Which element has the chemical symbol 'O'?", "Oxygen", "Osmium", "Ozone", "Opium", 1],

["What is the primary language spoken in Brazil?", "Spanish", "Portuguese", "French", "Italian", 2],

["Which famous scientist developed the theory of relativity?", "Isaac Newton", "Galileo Galilei", "Albert Einstein", "Marie Curie", 3],

["In which country did the Olympic Games originate?", "Greece", "France", "Italy", "England", 1],

["What is the longest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2],

["Which artist is known for the painting 'The Persistence of Memory'?", "Pablo Picasso", "Vincent van Gogh", "Salvador Dalí", "Claude Monet", 3],

["In what year did the Berlin Wall fall?", "1989", "1991", "1985", "1979", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

print('''Welcome to Kaun Banega Crorepati!
Answer the following questions correctly to win prize money!
You have 4 choices for each question. Good luck!''')
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"Quetion: {question[0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    print(f"Correct answer was {reply}")
    break        
print(f"Your take home money is {money}")