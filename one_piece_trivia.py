print("ONE PIECE TRIVIA!!!")

greeting = input("\nHello, contestant! Are you ready to begin? ")

name = input("\nOk! But, before we start...what is your name? ")
print(f"\nNice to meet you, {name}")

score = 0
print("\nNow, let us begin!")

question_1 = '\nWho ate the "Chop Chop" fruit? '
print(question_1)

chop_ans_1 = "Bon Clay"
chop_ans_2 = "Daz Bones"
chop_ans_3 = "Buggy the Clown"
chop_ans_4 = "Clawador"

print("A.", chop_ans_1)
print("B.", chop_ans_2)
print("C.", chop_ans_3)
print("D.", chop_ans_4)

ans_1 = input("\n")

if ans_1 == "c" or ans_1 =="C":
    print(f"\nYes, {name} that is correct! You will be awarded 10 points!")
    score += 10
else:
    print("\nNo, that is incorrect.")

print("\nNext question:")
question_2 = "Who was the 3rd member to join the Straw Hat Pirates?"
print(question_2)

straw_member_1 = "Sanji"
straw_member_2 = "Nami"
straw_member_3 = "Usopp"
straw_member_4 = "Zoro"

print("A", straw_member_1)
print("B", straw_member_2)
print("C", straw_member_3)
print("D", straw_member_4)

ans_2 = input("\n")

if ans_2 == "b" or ans_2 == "B":
    print("Awesome! That is correct. That was an easy one.")
    print("The next one will be more difficult.")
    print("You have been awarded 10 more points!")
    score += 10
else:
    print("No, that is incorrect.")


question_3 = "\nWhat is White Beard's full name?"
print(question_3)

white_name_1 = "Edward Newgate"
white_name_2 = "Marshall D. Teach"
white_name_3 = "Basil Hawkins"
white_name_4 = "Demoaro Black"

print("A", white_name_1)
print("B", white_name_2)
print("C", white_name_3)
print("D", white_name_4)

ans_3 = input("\n")

if ans_3 == "A" or ans_3 == "a":
    print(f"\nOhhhh! Amazing {name}! That is correct!")
    print("Here are 10 additional points")
    score += 10
else:
    print("\nNo, sorry. That is incorrect.")

print("\nOn to the Next!")

question_4 = "Who was the first person Luffy fought in the beginning of One Piece?"
print(question_4)

question_4_lists = ["A. Alvida", "B. Buggy the Clown", "C. Clawador", "D. Don Kreig"]

for question_4_list in question_4_lists:
    print(question_4_list)

ans_4 = input("\n")

if ans_4 == "a" or ans_4 == "A":
    print(f"\nGood job {name}! That answer is correct")
    print("You will be awarded 10 more points. Way to go!")
    score += 10
else:
    print("Nope! That is incorrect.")

if score <= 20:
    print("\nYou're not doing too good.")
    print("You should brush up on your knowledge of One Piece.")
print(score)

print("Alrighty then, next question:")
question_5 = "\nWhat is this highest position within the Marines?"
print(question_5)

question_5_lists = [ "A. Admiral", "B. Fleet Admiral",
                     "C. Vice Admiral", "D. Grand Admiral"]

for question_5_list in question_5_lists:
    print(question_5_list)

ans_5 = input("\n")

if ans_5 == "B" or ans_5 == "b":
    print("\nCorrectomundo! Good job.")
    print("You have been awarded 10 points")
    score += 10
else:
    print("\nSorry, that is not the correct answer")

print("\nAwesome! You've just completed half of the questions!")
half_way = input("Are you enjoying it so far? (Only answer with just a 'yes' or a 'no.') ")

if half_way == "yes" or half_way == "Yes":
    print(f"\nFantastic! I am glad you are enjoying it so far {name}.")
    print("Here is the next question:")
elif half_way == "no" or half_way == "No":
    print(f"\nHmm. That's too bad {name}. Oh well!. On to the next question!")

print("\nFrom here on out, the questions get a little harder.")

question_6 = "What sound did the Skyipeans hear" \
             "when the Shandia were sent into the sky via" \
             "'the Knock Up Stream'"
print(question_6)

question_6_lists = ["A. Bird", "B. Thunder",
                    "C. Bell", "D. Explosions"]
for question_6_list in question_6_lists:
    print(question_6_list)

ans_6 = input("\n")

if ans_6 == "c" or ans_6 == "C":
    print("\nGreat job! That is correct.")
    print("\n Here are 10 points.")
    score += 10
else:
    print("\nNo, that is not the answer.")

print("\nNext question is:")
question_7 = ("What is Chopper commonly mistaken for?")
print(question_7)

question_7_lists = ["A. Dog", "B. Doctor",
                    "C. Raccoon", "D. Reindeer"]
for question_7_list in question_7_lists:
    print(question_7_list)

ans_7 = input("\n")


if ans_7 == "c" or ans_7 == "C":
    print(f"\nThat is correct {name}!")
    print("Chopper is constantly mistaken for a raccoon!")
    score += 10
else:
    print("No. That is not what Chopper is usually mistaken for.")

print("\nHere is the 8th question:")
question_8 = "CP9 are all masters of the Rokushiki; superhuman techniques/powers." \
"How many techniques are in the Rokushiki that CP9 used? "
print(question_8)

question_8_lists = ["A. 5", "B. 6", "C. 7", "D. 8"]
for questions_8_list in question_8_lists:
    print(questions_8_list)


ans_8 = input("\n")

if ans_8 == "b" or ans_8 == "B":
    print(f"\nOh wow. Good job {name}. I am surprised you remember that!")
    print("Alright. Here are 10 more points.")
    score += 10
else:
    print("\nIncorrect. I'm sure you'll get the next one. ")

print("\nOk, introducing question 9. This is also a CP9 question:")
question_9 = "There were a total of 10 CP9 agents in the " \
             "Ennies Lobby Arc. How many of them went under cover" \
             "at the Galley La shipwright place in Water 7?"
print(question_9)

question_9_lists = ["A. 3", "B. 4", "C. 6", "D. 7"]
for question_9_list in question_9_lists:
    print(question_9_list)

ans_9 = input("\n")

if ans_9 == "a" or ans_9 == "A":
    print("\nOHHH! Look at you~ That is impressive. Correct!")
    print("10 points will be awarded to you now")
else:
    print("\nNo, incorrect. You have to pay attention "
          "more when watching One Piece! ")

if score == 0:
    print("\nYou have been doing god awful so far."
          "Are you even a One Piece fan?!")
elif score == 10 or score == 20:
    print("\nIf you're truly a One Piece fan. You can do better!")
elif score == 30 or score == 40:
    print("\nYou have SOME knowledge of One Piece it seems. "
          "Just not a lot")
elif score == 50 or score == 60:
    print("\nYou're not that bad, but you're also not doing that great.")
elif score >= 70:
    print("\nYou're doing amazing so for! Great job!")

input("Ok! This is the final question. Are you ready?")

joke_question = input("What is the One Piece?")