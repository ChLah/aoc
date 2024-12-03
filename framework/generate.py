import sys
from os import path, mkdir
from shutil import copyfile, copyfileobj
import urllib.request, urllib.parse


def load_challenge_files(day:int, year:int, session:str):
    base_path = path.dirname(sys.argv[0])
    template_path = path.join(base_path, 'framework', 'solution_template.py.txt')
    base_path = path.join(base_path, 'solutions', f'year{year}', f'day{day}')

    if not path.exists(base_path):
        mkdir(base_path)
    
    solution_path = path.join(base_path, 'solution.py')

    if not path.exists(solution_path):
        copyfile(template_path, solution_path)

    destination_path = path.join(base_path, 'input.txt')
    if not path.exists(destination_path):
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        
        headers = {
            'Referer': f'https://adventofcode.com/{year}/day/{day}',
            'Cookie': f'session={session.strip()}'
        }

        req = urllib.request.Request(url, method='GET', headers=headers)
        with urllib.request.urlopen(req) as response:
            content = response.read().decode("utf-8")
            with open(destination_path, 'wb') as destination:
                destination.write(content.encode("utf-8"))

