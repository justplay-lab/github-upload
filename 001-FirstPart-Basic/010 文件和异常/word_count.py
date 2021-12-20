#coding=gbk
#
def count_words(filename):
    """计算文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        msg += "\nand we logged it, thank you!"
        print(msg)
        
        # 将这个文件名写入missingfile.txt
        file_notfound = 'missingfile.txt'
        with open(file_notfound, 'a') as file_object2:
            file_object2.write(filename + "\n")
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
                " words.")
        print("and 'love' appears " + 
                str(contents.lower().count("love")) +
                " time.\n")
