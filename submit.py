from pathlib import Path
import os
import os.path as path
import subprocess
import fire
import re

root = path.abspath(path.dirname(__file__))

# 'https://atcoder.jp/contests/abc055/tasks/abc055_b' -> 'abc_055_b'
def get_problem_name(url: str):
    matches = re.match(r'https:\/\/atcoder.jp\/contests\/.*\/tasks\/(.*)', url)
    return matches.group(1)

# @ 'src/xxx/abc055_b' -> '(abc_055, abc055_b)'
def get_contest_problem_name():
    rel = get_rel_path()
    assert len(rel.parts) == 3, "run @ src/<contest>/<problem>/"
    problem = rel.parts[-1]
    contest = problem.split('_')[0]
    return (contest, problem)

# '(abc_055, abc055_b)' -> 'https://atcoder.jp/contests/abc055/tasks/abc055_b'
def get_url(contest: str, problem: str):
    return f'https://atcoder.jp/contests/{contest}/tasks/{problem}'

def get_rel_path():
    pwd = os.getcwd()
    return Path(path.relpath(pwd, root))

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
    def setup(self):
        contest_root = Path(os.getcwd())
        problems_path = contest_root / 'problems.txt'
        if problems_path.exists():
            print(f'{problems_path} found')
            urls = self._prepare_from_file(problems_path)
        else:
            assert(len(get_rel_path().parts) == 2)
            contest = contest_root.parts[-1]
            urls = self._prepare_urls(contest)
            print(f'{contest=} {urls=}')

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

    def test(self, error: str = '', entry: str = 'julia main.jl', tle: str = '2'):
        if error:
            error = f'-e {error}'

        sh(f'oj t -N {error} -t {tle} -c "{entry}"')

    def submit(self, entry: str = 'main.jl'):
        contest, problem = get_contest_problem_name()
        print(f'{contest=}, {problem=}')

        url = get_url(contest, problem)
        sh(f'oj submit -y {url} {entry}')

    def dl(self):
        contest, problem = get_contest_problem_name()
        url = get_url(contest, problem)
        sh(f'oj dl {url}')

if __name__ == "__main__":
    fire.Fire(Cli)