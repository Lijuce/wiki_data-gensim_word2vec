from gensim.models import Word2Vec

model = Word2Vec.load("wiki.zh.text.model")

test_words = ["中国", "数学", "科技", "苹果"]
for i in range(4):
    res = model.most_similar(test_words[i])
    print(test_words[i])
    print(res)

