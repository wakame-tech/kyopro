from pathlib import Path
import os
import os.path as path
import subprocess
import fire

root = path.abspath(path.dirname(__file__))

def get_url(dirname: str):
    *contest, problem = dirname.split('_')
    contest = '_'.join(contest)
    return f'https://atcoder.jp/contests/{contest}/tasks/{dirname}'

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
    # set up directories
    # $submit.py --problems [abcxxx_a,abcxxx_b,abcxxx_c,abcxxx_d,abcxxx_e,abcxxx_f]
    def setup(self, contest: str, problems: list = []):
        if len(problems) == 0:
            problems = list(map(lambda p: f'{contest}_{p}', ['a', 'b', 'c', 'd', 'e', 'f']))

        print(problems)

        contest_root = Path(root) / 'src' / contest

        if not contest_root.exists():
            os.mkdir(contest_root)

        for problem in problems:
            problem_root = contest_root / problem
            test_dir = contest_root / problem / 'test'
            if not problem_root.exists():
                os.mkdir(problem_root)
            if not test_dir.exists():
                os.mkdir(test_dir)

            # setup
            sh(f'touch {problem_root / "main.py"}')
            sh(f'oj dl -d {test_dir} {get_url(problem)}')

    def test(self, error: str = '', entry: str = 'main.py', tle: str = '2'):
        contest, problem = get_contest_problem_name()
        if error:
            error = f'-e {error}'
        sh(f'oj t -N {error} -t {tle} -c "python {entry}"')

if __name__ == "__main__":
    fire.Fire(Cli)