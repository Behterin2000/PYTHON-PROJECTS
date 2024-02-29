def strip_punctuation(s):
    new=''
    for character in s:
        if character in punctuation_chars:
            continue
        new=new+character
    return new

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt","r") as content1:
    content1=content1.readlines()
    for lin in content1:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use  
negative_words=[]          
with open("negative_words.txt","r") as content2:
    content2=content2.readlines()
    for lin in content2:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_pos(sentence):
    sentence=sentence.lower()
    sentence=sentence.split()
    pos_counter=0 
    for word in sentence:
        word=strip_punctuation(word)
        if word in positive_words:
            pos_counter=pos_counter+1
    return pos_counter

def get_neg(sentence):
    sentence=sentence.lower()
    sentence=sentence.split()
    neg_counter=0 
    for word in sentence:
        word=strip_punctuation(word)
        if word in negative_words:
            neg_counter=neg_counter+1
    return neg_counter    
    
filex=open("project_twitter_data.csv",'r')
main_content=filex.readlines()


filey=open("resulting_data.csv",'w')
header=("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
filey.write(header)
filey.write('\n')

for words in main_content[1:]:
    vals=words.strip().split(",")
   
    retweet_counter=vals[1]
    reply_count=vals[2]
    good_word_count=get_pos(vals[0])
    bad_word_count=get_neg(vals[0])
    score=good_word_count-bad_word_count
    output='{},{},{},{},{}'.format(retweet_counter,reply_count,good_word_count,bad_word_count,score)
    filey.write(output)
    filey.write('\n')
filex.close()
filey.close()