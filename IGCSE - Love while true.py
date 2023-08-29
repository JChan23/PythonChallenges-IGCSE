#Exercise 1
while True:
  FavoriteSubject = input ('What is your favorite subject? ')
  if FavoriteSubject == "computer science" :
    print("Yes. It is indeed the best subject")
    break
  else:
    print('Hm. Try again.')

#Exercise 2
number = 0 
while number < 15 or number > 20 :
    print("Please enter a number between 15 and 20. Decimals are accepted")
    number = float(input("enter a number:"))
