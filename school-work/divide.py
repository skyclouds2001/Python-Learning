import os, random, shutil


def each_file(path):
    return os.listdir(path)


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def divide_train_data(source, target):
    print(each_file(source))

    for c in each_file(source):
        pic_name = each_file(os.path.join(source, c))
        random.shuffle(pic_name)
        train_list = pic_name[0:1499]
        validation_list = pic_name[1499:]
        test_list = []

        mkdir(target + 'train/' + c + '/')
        mkdir(target + 'validation/' + c + '/')
        mkdir(target + 'test/' + c + '/')

        for train_pic in train_list:
            shutil.copy(os.path.join(source, c, train_pic), target + 'train/' + c + '/' + train_pic)

        for validation_pic in validation_list:
            shutil.copy(os.path.join(source, c, validation_pic), target + 'validation/' + c + '/' + validation_pic)

        for test_pic in test_list:
            shutil.copy(os.path.join(source, c, test_pic), target + 'test/' + c + '/' + test_pic)

    return


if __name__ == '__main__':
    filepath = r'D:/学习/3·2信息与内容安全/CNN_synth_testset'
    dist = r'./../CNN_synth_testset_divided/'
    divide_train_data(filepath, dist)
