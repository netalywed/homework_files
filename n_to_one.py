import os
import operator
def order_files ():
    files_path = os.path.join(os.getcwd(), "files")
    our_files = os.listdir(files_path)

    all_files_dict = {}

    for file in our_files:
        with open(files_path + "\\" + file, "r", encoding="utf-8") as f:
            all_files_dict[file] = f.readlines()

    all_files_dict_sorted = sorted(all_files_dict.items(), key=operator.itemgetter(1))

    with open("final.txt", "w", encoding='utf-8') as f:
        for item in all_files_dict_sorted:
            f.write(item[0] + '\n')
            f.write(str(len(item[1])) + '\n')
            for line in item[1]:
                f.write(line)
            f.write('\n')

order_files()



