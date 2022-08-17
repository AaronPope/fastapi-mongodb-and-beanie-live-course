from pathlib import Path
import pprint
import json

from package import Package

def main():
    file = Path(__file__).parent / 'pydantic.json'
    with open(file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)

    print (data)
    


if __name__ == '__main__':
    main()
