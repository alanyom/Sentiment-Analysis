Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

def strip_punctuation(string):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for wrd in string:
        if wrd in punctuation_chars:
            string = string.replace(wrd, "")
    return string


def get_pos(x):
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())

    myreturn = strip_punctuation(x)
    myreturn = myreturn.split(" ")

    pos_count = 0
    for pos in myreturn:
        lower_pos = pos.lower()
        #        print(lower_pos)
        if lower_pos in positive_words:
            pos_count += 1

    return pos_count


def get_neg(x):
    negative_words = []
    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())

    myreturn = strip_punctuation(x)
    myreturn = myreturn.split(" ")

    neg_count = 0
    for neg in myreturn:
        lower_neg = neg.lower()
        #        print(lower_neg)
        if lower_neg in negative_words:
            neg_count += 1

    return neg_count


def get_net(pos, neg, net):
    if pos == neg:
        net = 0
    else:
        if pos > neg:
            net = pos - neg
        else:
            net = -(neg - pos)

    return (pos, neg, net)


fh = open('project_twitter_data.csv', 'r')
result = open('resulting_data.csv', 'w')

result.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score' + '\n')

total_data = ""
while True:
    line = fh.readline()
    sep_text = list(line.split(","))
    text = (sep_text[0])

    if not line:
        break

    myline = ""

    if (text != 'tweet_text'):
        retweet = (sep_text[1].strip())
        replies = (sep_text[2].strip())

        int_pos = (get_pos(line))
        my_pos = str(int_pos)

        int_neg = (get_neg(line))
        my_neg = str(int_neg)

        int_net = 0
        my_net = str(int_net)

        my_return = list(get_net(int_pos, int_neg, int_net))
        my_pos = str(my_return[0])
        my_neg = str(my_return[1])
        my_net = str(my_return[2])

        newstr = ", ".join((retweet, replies, my_pos, my_neg, my_net))
        result.write(newstr)
        result.write("\n")

        print(newstr)
