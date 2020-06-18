import random
import json

def parse(filename):
    f = open(filename)
    for l in f:
        yield eval(l)

news_data = []
categories = set(['POLITICS', 'WELLNESS', 'ENTERTAINMENT', 'TRAVEL', 'STYLE & BEAUTY'])

for news in parse('News_Category_Dataset_v2.json'):
    category = (news['category'].encode('ascii','ignore')).decode('utf-8')
    description = (news['short_description'].encode('ascii','ignore')).decode('utf-8')
    headline = (news['headline'].encode('ascii', 'ignore')).decode('utf-8')

    if category in categories:
        headline_words = headline.split()
        description_words = description.split()
        quote = " ".join(headline_words + description_words)
        if len(quote) > 0:
            news_string = category + "\t" + quote
            news_data.append(news_string)

random.shuffle(news_data)

news_data_len = len(news_data)
train_data = news_data[:int(0.7 * news_data_len)]
dev_data = news_data[int(0.7 * news_data_len): int(0.9 * news_data_len)]
test_data = news_data[int(0.9 * news_data_len):]

print("training dataset: %i" % len(train_data))
print("dev dataset: %i" % len(dev_data))
print("test dataset: %i" % len(test_data))

print(train_data[0])

with open('train.tsv', 'w+') as train_file:
    for data in train_data:
        train_file.write(data)
        train_file.write("\n")

with open('dev.tsv', 'w+') as dev_file:
    for data in dev_data:
        dev_file.write(data)
        dev_file.write("\n")

with open('unlabeled.tsv', 'w+') as test_file:
    for data in test_data:
        test_file.write(data)
        test_file.write("\n")


