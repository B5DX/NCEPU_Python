import re

def matchEmail(email:str):
    res = re.match(r'[a-zA-Z0-9]{4,20}@163\.com$', email)
    # note: shoudn't be r'^...@163.com', '.' represents any char, so '\' is essential
    # match会从开头开始匹配，如果未必从开头要用search(search加上^就相当于match了)
    if res:
        return True
    else:
        return False

if __name__ == "__main__":
    print(matchEmail('_wrwzx1@163.com'))