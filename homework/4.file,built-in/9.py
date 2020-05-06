import requests as rq
import os

def main():
    path = r'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2943900789,3211623788&fm=26&gp=0.jpg'
    img_form = path[path.rindex('.'):]
    img = rq.get(path)
    os.chdir(os.path.dirname(__file__))
    with open(f'test{img_form}', 'wb') as f:
        f.write(img.content)

if __name__ == "__main__":
    main()