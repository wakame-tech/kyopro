from pathlib import Path
import os
import os.path as path
import subprocess
import fire
import re

root = path.abspath(path.dirname(__file__))

def get_problem_name(url: str):
    matches = re.match(r'https:\/\/atcoder.jp\/contests\/.*\/tasks\/(.*)', url)
    return matches.group(1)

def get_url(contest: str, problem: str):
    return f'https://atcoder.jp/contests/{contest}/tasks/{problem}'

def get_rel_path():
    pwd = os.getcwd()
    return Path(path.relpath(pwd, root))

def get_contest_problem_name():
    rel = get_rel_path()
    assert len(rel.parts) == 3, "run @ src/<contest>/<problem>/"
    _, contest, problem = rel.parts
    return (contest, problem)

def get_contest_name():
    rel = get_rel_path()
    assert len(rel.parts) == 2, "run @ src/<contest>/"
    _, contest = rel.parts
    return contest

def sh(script: str):
    script = script.replace('\\', '\\\\')
    print(script)
    subprocess.call(script)

class Cli(object):
    def _prepare_urls(self, contest: str, problem_set = ['a', 'b', 'c', 'd', 'e', 'f']):
        urls = []
        for problem in problem_set:
            urls.append(get_url(contest, f'{contest}_{problem}'))
        return urls

    def _prepare_from_file(self, file_path: Path):
        urls = []
        with open(file_path) as f:
            for line in f:
                urls.append(line.strip())
        return urls

    # set up directories
    # $submit.py --problems [abcxxx_a,abcxxx_b,abcxxx_c,abcxxx_d,abcxxx_e,abcxxx_f]
    def setup(self, problems: list = []):
        contest_root = Path(os.getcwd())
        problems_path = contest_root / 'problems.txt'
        if problems_path.exists():
            urls = self._prepare_from_file(problems_path)
        else:
            urls = self._prepare_urls(contest_root.parts[-1], problems)

        for url in urls:
            problem = get_problem_name(url)
            problem_root = contest_root / problem
            test_dir = contest_root / problem / 'test'
            if not problem_root.exists():
                os.mkdir(problem_root)
            if not test_dir.exists():
                os.mkdir(test_dir)

            # setup
            sh(f'touch {problem_root / "main.py"}')
            sh(f'oj dl -d {test_dir} {url}')

    def test(self, error: str = '', entry: str = 'main.py', tle: str = '2'):
        if error:
            error = f'-e {error}'
        sh(f'oj t -N {error} -t {tle} -c "python {entry}"')

    def submit(self, entry: str = 'main.py'):
        contest, problem = get_contest_problem_name()
        url = get_url(contest, problem)
        sh(f'oj submit -y {url} {entry}')

    def dl(self):
        contest, problem = get_contest_problem_name()
        url = get_url(contest, problem)
        sh(f'oj dl {url}')

if __name__ == "__main__":
    fire.Fire(Cli)