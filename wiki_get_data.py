from gensim.corpora import WikiCorpus
import jieba
import codecs, sys, time

# 提取wiki压缩包的数据
def wiki_xml2txt_processing():
    i = 0
    input_file = "zhwiki.xml.bz2"
    output_file = "wiki_data_%07d.txt" % i
    time_start = time.time()
    wiki = WikiCorpus(input_file, lemmatize=False, dictionary={})
    output = open(output_file, 'w', encoding="utf-8")
    for text in wiki.get_texts():
        str_line = " ".join(text) + "\n"
        # print(str_line)
        output.write(str_line)
        i += 1
        if (i % 100 ==0 ):
            print("Save "+str(i) + " articles")
    output.close()
    print("Finished saved " + str(i) + " articles")
    time_end = time.time()
    print('totally cost', time_end - time_start)

# 将提取好的wiki数据进行分词
def wiki_data_cut_words():
    f = codecs.open('wiki_test.txt', 'r', encoding="utf8")
    target = codecs.open("wiki_data_seg.txt", "w", encoding='utf-8')
    print("open files")
    line_num = 1
    line = f.readline()
    while line:
        print('-----------processing', line_num, ' article---------------')
        line_seg = " ".join(jieba.cut(line))
        target.writelines(line_seg)
        line_num += 1
        line = f.readline()
    f.close()
    target.close()
    # exit()



if __name__ ==  '__main__':
    # f = codecs.open('wiki_test.txt', 'r', encoding="utf8")
    f = open('wiki_test.txt', 'r', encoding="utf8")
    # target = open("wiki_data_seg.txt", "w", encoding='utf-8')
    print("open files")
    line_num = 1
    line = f.readline()
    while line:
        print('-----------processing', line_num, ' article---------------')
        line_seg = " ".join(jieba.cut(line))
        # target.writelines(line_seg)
        print(line_seg)
        line_num += 1
        line = f.readline()
    f.close()
    # target.close()