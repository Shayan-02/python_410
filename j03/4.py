u1 = input("enter your choice(""rock"",""paper"",""scissors""): ")
u2 = input("enter your choice(""rock"",""paper"",""scissors""): ")
if u1 == u2:
    print("draw")
elif u1 == "rock" and u2 == "scissors":
    print("user1 win")
elif u1 == "scissors" and u2 == "paper":
    print("user1 win")
elif u1 == "paper" and u2 == "rock":
    print("user1 win")
elif u1 == "paper" and u2 == "scissors":
    print("user2 win")
elif u1 == "scissors" and u2 == "rock":
    print("user2 win")
elif u1 == "rock" and u2 == "paper":
    print("user2 win")
else:
    print("invalid input")


if u1 == u2:
    print("draw")
elif u1 == "rock":
    if u2 == "scissors":
        print("user1 win")
    if u2 == "paper":
        print("user2 win")
elif u1 == "scissors":
    if u2 == "rock":
        print("user2 win")
    if u2 == "paper":
        print("user1 win")
elif u1 == "paper":
    if u2 == "rock":
        print("user1 win")
    if u2 == "scissors":
        print("user2 win")
else:
    print("invalid input")
