from typing import Text
import praw
import pickle
import time
from threading import Thread

filename = 'Files/commentsRepliedTo.pk'
commentsRepliedTo = []
with open(filename, 'rb') as fi:
    commentsRepliedTo = pickle.load(fi)
blacklist = ["Title Of Your Sextape", "Title Of Your Sex tape", "title of your sextape", "title of your sex tape", "Title of your sextape", "Title of your sextape", "Title of your sex movie", "Title Of Your Sex Movie"]
#replyMessage = f""
#with open('FAQ.txt') as f:
#    replyMessage = f.readlines()
print("Starting Bot...")
reddit = praw.Reddit(
    user_agent="astroneerfaqv1",
    client_id="Ae8uA0bGBIr6Ch4SDk6j2Q",
    client_secret="9vqY61P1SlK-QvtovGPffN4d2p3-mQ",
    username="Astroneer-FAQ",
    password="seattle1AF"
)
def callWait():
    print("Waiting 5 minutes before next call...")
    time.sleep(60)
    print("Waiting 4 minutes before next call...")
    time.sleep(60)
    print("Waiting 3 minutes before next call...")
    time.sleep(60)
    print("Waiting 2 minutes before next call...")
    time.sleep(60)
    print("Waiting 1 minutes before next call...")
    time.sleep(60)
inbox = reddit.inbox
comments = reddit.inbox.comment_replies
def getFAQ(mention):#, completion):
            body = f"{mention.body}"
            request = body.replace("u/Astroneer-FAQ ", "")
            capBody = request.capitalize()
            print(capBody)
            if "Balls" in capBody or "Marbles" in capBody or "Ball" in capBody or "Marble" in capBody or "Ball" in capBody or "Marble" in capBody:
                with open('Files/FAQ/Marbles.txt') as f:
                    with open('Files/FAQ/Ending.txt') as e:
                        mention.reply(f"Astroneer FAQ:\n\n{f.read()}\n\n{e.read()}")
            elif "Achievements" in capBody or "Multiplayer" in capBody or "Power" in capBody or "Scrap" in capBody or "Storage" in capBody or "Storms" in capBody:
                with open(f'Files/FAQ/{capBody}.txt') as f:
                    with open('Files/FAQ/Ending.txt') as e:
                        mention.reply(f"Astroneer FAQ:\n\n{f.read()}\n\n{e.read()}")
            else:
                with open('Files/FAQ/Achievements.txt') as a:
                    with open('Files/FAQ/Marbles.txt') as marbles:
                        with open('Files/FAQ/Multiplayer.txt') as multiplayer:
                            with open('Files/FAQ/Power.txt') as power:
                                with open('Files/FAQ/Scrap.txt') as scrap:
                                    with open('Files/FAQ/Storage.txt') as storage:
                                        with open('Files/FAQ/Storms.txt') as storms:
                                            with open('Files/FAQ/Ending.txt') as ending:
                                                #return(f"Astroneer FAQ:\n\n{a.read()}\n\n{marbles.read()}\n\n{multiplayer.read()}\n\n{power.read()}\n\n{scrap.read()}\n\n{storage.read()}\n\n{storms.read()}\n\n{ending.read()}")
                                                done = (f"Astroneer FAQ:\n\n{a.read()}\n\n{marbles.read()}\n\n{multiplayer.read()}\n\n{power.read()}\n\n{scrap.read()}\n\n{storage.read()}\n\n{storms.read()}\n\n{ending.read()}")
                                                return done
def runMentions():
    #print("fetching FAQ.txt...")
    #with open('FAQ.txt') as f:
    #    replyMessage = f.read()
        #print(f"replyMessage = {replyMessage}")
    print("fetching mentions:")
    for mention in inbox.mentions(limit=25):
        #print(f"{mention.author}\n{mention.body}\n")
        #print(f"commentsRepliedTo = {commentsRepliedTo}")
        if mention.id in commentsRepliedTo:
            print(f"{mention.submission.url} Already responded")
        else:
            print("replying...")
        #if mention.id not in commentsRepliedTo:
            print(f"{mention.author}\n{mention.body}\n")
            commentsRepliedTo.append(mention.id)
            commentsRepliedTo.append(mention.body)
            print(f"commentsRepliedTo = {commentsRepliedTo}")
            with open(filename, 'wb') as fi:
                # dump your data into the file
                pickle.dump(commentsRepliedTo, fi)
            body = f"{mention.body}"
            request = body.capitalize().replace("U/astroneer-faq ", "")
            capBody = request.capitalize()
            print(f"CapBody = {capBody}")
            if "Balls" in capBody or "Marbles" in capBody or "Ball" in capBody or "Marble" in capBody or "Ball" in capBody or "Marble" in capBody:
                with open('Files/FAQ/Marbles.txt') as f:
                    with open('Files/FAQ/Ending.txt') as e:
                        mention.reply(f"Astroneer FAQ:\n\n{f.read()}\n\n{e.read()}")
                        print(f"replied: {capBody} FAQ")
            elif "Achievements" in capBody or "Multiplayer" in capBody or "Power" in capBody or "Scrap" in capBody or "Storage" in capBody or "Storms" in capBody:
                with open(f'Files/FAQ/{capBody}.txt') as f:
                    with open('Files/FAQ/Ending.txt') as e:
                        mention.reply(f"Astroneer FAQ:\n\n{f.read()}\n\n{e.read()}")
                        print(f"replied: {capBody} FAQ")
            else:
                with open('Files/FAQ/Achievements.txt') as a:
                    with open('Files/FAQ/Marbles.txt') as marbles:
                        with open('Files/FAQ/Multiplayer.txt') as multiplayer:
                            with open('Files/FAQ/Power.txt') as power:
                                with open('Files/FAQ/Scrap.txt') as scrap:
                                    with open('Files/FAQ/Storage.txt') as storage:
                                        with open('Files/FAQ/Storms.txt') as storms:
                                            with open('Files/FAQ/Ending.txt') as ending:
                                                #return(f"Astroneer FAQ:\n\n{a.read()}\n\n{marbles.read()}\n\n{multiplayer.read()}\n\n{power.read()}\n\n{scrap.read()}\n\n{storage.read()}\n\n{storms.read()}\n\n{ending.read()}")
                                                done = (f"Astroneer FAQ:\n\n{a.read()}\n\n{marbles.read()}\n\n{multiplayer.read()}\n\n{power.read()}\n\n{scrap.read()}\n\n{storage.read()}\n\n{storms.read()}\n\n{ending.read()}")
                                                mention.reply(done)
                                                print(f"replied Full FAQ")
            #getFAQ(mention, completion=mention.reply(getFAQ()))
            #mention.reply(f"u/{mention.author} here you go.\n\n{replyMessage}")
    #callWait()
    print("Waiting 10 seconds before next mentions call...")
    time.sleep(5)

def runComments():
    print("fetching comments:")
    for comment in comments(limit=25):
        if comment.id in commentsRepliedTo:
            print(f"{comment.submission.url} Already replied")
        else:
            print("replying...")
            print(f"{comment.author}\n{comment.body}\n")
            commentsRepliedTo.append(comment.id)
            commentsRepliedTo.append(comment.body)
            print(f"commentsRepliedTo = {commentsRepliedTo}")
            body = f"{comment.body}"
            capitalize = body.capitalize()
            with open(filename, 'wb') as fi:
                # dump your data into the file
                pickle.dump(commentsRepliedTo, fi)
            if "Good bot" in capitalize:
                path = "Files/Voting/Upvotes.pk"
                with open(path, 'rb') as rv:
                    count = pickle.load(rv)
                    with open(path, 'wb') as wv:
                        # dump your data into the file
                        pickle.dump(int(count) + 1, wv)
                comment.reply("Thank you for upvoting this bot! Have a good day!")
            elif "Bad bot" in capitalize:
                path = "Files/Voting/Downvotes.pk"
                with open(path, 'rb') as rv:
                    count = pickle.load(rv)
                    with open(path, 'wb') as wv:
                        # dump your data into the file
                        pickle.dump(int(count) + 1, wv)
                comment.reply("We're sorry you had a bad experience, please let us know how to improve by dming me.")
            checkVotes()
            #getFAQ(mention, completion=mention.reply(getFAQ()))
            #mention.reply(f"u/{mention.author} here you go.\n\n{replyMessage}")
    #callWait()
    print("Waiting 10 seconds before next comments call...")
    time.sleep(5)

def checkVotes():
    with open("Files/Voting/Downvotes.pk", 'rb') as dv:
        downvotes = pickle.load(dv)
        with open("Files/Voting/Upvotes.pk", 'rb') as uv:
            upvotes = pickle.load(uv)
            print(f"Upvotes: {upvotes}\nDownvotes: {downvotes}\n")

def checkCommands():
    text = input().capitalize()
    if "Voting" in text or "Votes" in text:
        checkVotes()

def run():
    while True:
        if __name__ == '__main__':
            Thread(target = checkCommands).start()
        if commentsRepliedTo != []:
            runMentions()
            runComments()
        else:
            print("Waiting for commentsRepliedTo to populate...")

run()