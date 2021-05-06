# kyopro
##  ⚙ requirements
- Python 3.8.2
- online-judge-tools
- VSCode

## ✨ setup contest from `problems.txt`
`src/<contest>/problems.txt` in contest directory. If absent, create `ABC` contest templates.

#### `src/<contest>/problems.txt`
problem urls
```
https://atcoder.jp/contests/...
https://atcoder.jp/contests/...
```

```bash
$ cd src/<contest>/
$ python path/to/submit.py setup
```

## ✨ Sample case test
```bash
$ cd src/<contest>/<problem>
$ python /path/to/submit.py test
```

or

## Short Cuts & Tasks
| short cut | run |
|:--:|:--:|
| F5 | Test Sample Cases |
| Ctrl + F5 | Submit Code |

<details>
<summary>setup</summary>

#### `tasks.json`
```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "ojTest",
            "type": "shell",
            "command": "cd",
            "args": [
                "\"${fileDirname}\"",
                "&&",
                "python",
                "\"${workspaceRoot}${pathSeparator}submit.py\"",
                "test"
            ],
            "group": {
                "kind": "test",
                "isDefault": true
            }
        },
        {
            "label": "ojSubmit",
            "type": "shell",
            "command": "cd",
            "args": [
                "\"${fileDirname}\"",
                "&&",
                "python",
                "\"${workspaceRoot}${pathSeparator}submit.py\"",
                "submit"
            ],
            "group": {
                "kind": "test",
                "isDefault": true
            }
        }
    ]
}
```

#### `keybindings.json`
```json
    {
        "key": "f5",
        "command": "workbench.action.tasks.runTask",
        "args": "ojTest"
    },
    {
        "key": "Ctrl+f5",
        "command": "workbench.action.tasks.runTask",
        "args": "ojSubmit"
    }
```

</details>