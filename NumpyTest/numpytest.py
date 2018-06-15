# encoding = utf-8
import numpy as np

def main():
    list = [[1, 3, 5], [2, 4, 6]]
    print(type(list))
    np_list = np.array(list)
    print(type(np_list))

if __name__=="__main__":
    main()
