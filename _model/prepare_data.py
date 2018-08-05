import numpy as np


def get_dataset(in_path, out_path, length, window, company_name, w2vec):
    data_set = []
    f_out = open(out_path, 'w')

    with open(in_path, 'r') as f_in:
        for l in f_in:
            wordlist = l.strip().split(" ")

            if wordlist != company_name:
                continue

            wordlist_l = list(filter(lambda o: o != company_name, wordlist[0:length]))
            wordlist_r = list(filter(lambda o: o != company_name, wordlist[length+1:]))

            if len(wordlist_l) < window or len(wordlist_r) < window:
                continue

            wordnear = wordlist_l[-window:] + wordlist_r[0:window]
            f_out.write(" ".join(wordnear)+"\n")
            veclist = [w2vec[w] for w in wordnear]
            data_set.append(veclist)

    f_out.close()

    training_set_len = int(len(data_set) * 0.8)
    training_set = data_set[0:training_set_len]
    testing_set = data_set[training_set_len:]
    label = [[1, 0] for _ in data_set]
    training_label = np.array(label[0:training_set_len])
    testing_label = np.array(label[training_set_len:])

    print("training dataset: %d, testing data set: %d"%(len(training_set), len(testing_set)))

    return data_set, training_set, testing_set, training_label, testing_label
