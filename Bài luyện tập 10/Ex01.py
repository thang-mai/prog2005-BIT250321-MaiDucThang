import os

def lay_ten_file(path):
    return os.path.basename(path)

def lay_ten_bai_hat(path):
    return os.path.splitext(os.path.basename(path))[0]

path = input('Nhap duong dan: ')
print('Ten file: ', lay_ten_file(path))
print('Ten bai hat: ', lay_ten_bai_hat(path))