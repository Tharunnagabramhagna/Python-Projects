print("📊 GRADE CALCULATOR 📊")
scores = []

while True:
    score = input("\nEnter a test source(or 'done'): ")
    if score.lower() == "done":
        print("👋 Good Bye")
        break

    scores.append(float(score))
    average = sum(scores)/len(scores)
    print(f"Average score: {average:.1f}")

    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    else:
        print("Grade: D or F")


'''
here scores is a empty list and score is used to get done output.later by using append function they 
have imported score as float and after that the average is used to measure the score.sum(scores) is 
the score it self,len(scores) means if it has 1 element then length is 1, for 2 it's len is 2

working:-
          if score= 80
          then score again= 70
          average = 80+70/2 = 150/2 = 75
'''
