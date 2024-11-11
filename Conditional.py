userReply = input("Pengiriman Paket pada hari ini? (Enter yes or no) ")

if userReply.lower() == "yes" or "y":
    print("We can help you ship that package!")
elif userReply.lower() == "no" or "n":
    print("Please come back when you need to ship a packeg. Thank you.")
else:
    print("silahkan input yang benar")
    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")