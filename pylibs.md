# typing python

Collection, Dict, Optional, Tuple, Union

# pathlib python

```
>>> from pathlib import Path
>>> p = Path('.')
>>> [x for x in p.iterdir() if x.is_dir()]
[PosixPath('src'), PosixPath('training'), PosixPath('data'), PosixPath('.git'), PosixPath('.vscode')]
```

```
>>> list(p.glob('**/*.py'))
[PosixPath('test_pathlib.py'), PosixPath('setup.py'),
 PosixPath('pathlib.py'), PosixPath('docs/conf.py'),
 PosixPath('build/lib/pathlib.py')]
```



# install formatter for python: pip install autopep8 and then plugin in vs code and set up on settings.json of vscode on yout project



