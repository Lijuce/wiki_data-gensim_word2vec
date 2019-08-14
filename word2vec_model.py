import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

data_file = "wiki_data_seg.txt"
print(LineSentence(data_file))

model = Word2Vec(LineSentence(data_file), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
model.save("wiki.zh.text.model")
# model.wv.save_word2vec("wiki.zh.text.vector", binary=False)
