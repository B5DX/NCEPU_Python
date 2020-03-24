#修改歌词

import os

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    try:
        with open('Blowing in the wind.txt', 'r', encoding='utf-8') as f:
            tmp = f.read()
        tmp = tmp.split('\n')

        try:
            tmp.remove('')
        except ValueError:
            pass

        tmp.insert(0, 'Blowing in the wind')
        tmp.append('1962 by Warner Bros. Inc')
        with open('Blowing in the wind.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(tmp))
        os.rename('Blowing in the wind.txt', 'Blowing in the wind-Bob Dylan.txt')
        # print([line + '\n' for line in tmp])
        print('\n'.join(tmp))
        
    except FileExistsError:
        print(FileExistsError.args)
    else:
        print('Finish')