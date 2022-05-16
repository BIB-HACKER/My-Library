# f = open('poems.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()

##################################################

#game
def game():
    return 65

score = game()
with open("highscore.txt") as f:
    hiscore = int(f.read())

if hiscore==' ':
    with open("hiscore.txt","w") as f:
        f.write(str(score))
elif int(hiscore)<score:
    with open("hiscore.txt","w") as f:
        f.write(str(score))

