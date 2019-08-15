import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import os, sys, logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logger.setLevel(level=logging.INFO)
    logger.info("runnin %s" % ' '.join(sys.argv))
    if len(sys.argv) < 4:
        print ("No enough argv for python working")
        sys.exit(1)
    data_file, model_name, vector_pickle_name = sys.argv[1:4]  # 读取命令行的后三变量名

    model = Word2Vec(LineSentence(data_file), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save(model_name)
    model.wv.save_word2vec_format(vector_pickle_name, binary=False)
    logger.info("Build model successfully!")


