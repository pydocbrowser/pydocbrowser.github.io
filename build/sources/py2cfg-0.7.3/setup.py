# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['_proto_',
 '_proto_.src',
 'py2cfg',
 'py2cfg._proto_',
 'py2cfg._proto_.src',
 'py2cfg.server',
 'server',
 'src']

package_data = \
{'': ['*']}

install_requires = \
['astor', 'flask', 'graphviz>=0.1', 'pudb', 'requests', 'websocket-server>=0.4']

entry_points = \
{'console_scripts': ['py2cfg = py2cfg._runner:main']}

setup_kwargs = {
    'name': 'py2cfg',
    'version': '0.7.3',
    'description': 'Converts python source code to colorful Control Flow Graphs (CFGs).',
    'long_description': "# py2cfg\nPython3 control flow graph generator\n\n`py2cfg` is a package that can be used to produce control flow graphs (CFGs) for Python 3 programs. \nThe CFGs it generates can be easily visualised with graphviz.\nThat graphical analysis is the main purpose of the module.\n\n## Examples\nBelow is an example of a piece of code that generates the Fibonacci sequence and the CFG produced for it with py2cfg:\n\n```py\n# fib.py\n\ndef fib():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\n\nfib_gen = fib()\nfor _ in range(10):\n    next(fib_gen)\n```\n\n![](_static/fib_cfg.svg)\n![](docs/source/_static/fib_cfg.svg)\n\n```py\nclass Sort:\n    def merge(self, l, r):\n        i = 0\n        j = 0\n        arr = []\n        size = len(l) + len(r)\n        for k in range(0, size):\n            lSentinel = i == len(l)\n            rSentinel = j == len(r)\n            if i == len(l):\n                arr.append(r[j])\n                j += 1\n            elif j == len(r):\n                arr.append(l[i])\n                i += 1\n            elif l[i] <= r[j]:\n                arr.append(l[i])\n                i += 1\n            else:\n                arr.append(r[j])\n                j += 1\n\n        return arr\n\n    def merge_sort(self, src):\n        n = len(src) / 2\n        l = src[0:n]\n        r = src[n:]\n        if len(l) > 1:\n            l = self.merge_sort(l)\n        if len(r) > 1:\n            r = self.merge_sort(r)\n\n        src = self.merge(l, r)\n        return src\n\n    def insertion_sort(self, src):\n        j = 1\n        for j in range(1, len(src)):\n            i = j - 1\n            key = src[j]\n        while i >= 0 and src[i] >= key:\n            src[i + 1] = src[i]\n            i = i - 1\n            src[i + 1] = key\n        return src\n```\n\n![](_static/speed_sort_cfg.svg)\n![](docs/source/_static/speed_sort_cfg.svg)\n\nIt can also be used interactively with pudb3.\n\n![](_static/pudb3-py2cfg.gif)\n![](docs/source/_static/pudb3-py2cfg.gif)\n\n### More examples\nAfter cloning, see `./examples/` for some code snippets to run this on.\nTo generate `_cfg.svg` or `_cfg.png` or `_cfg.pdf` images for each example, clone this repo and run the following command in the repo root directory:\n```sh\ngit clone repourl\ncd intorepodirectory\n./generate_examples.sh\n```\n\n## Installation via pip3\nNote: installation is not required, but is handy.\n\nTo install simply run\n```sh\npip3 install py2cfg --user\n```\n\nor clone this repo and pip install locally\n```\ngit clone <url>\ncd intoprojectdirectory\npip3 install . --user\n```\n\n## Usage\nIt can be used three ways:\n\n### Run via shell command\nIf you have installed, then the default command is py2cfg:\n```py\npy2cfg <file.py>\n``` \nThis will create a `<file>_cfg.svg` file, which contains the colored cfg of the file.\nIf you don't want to install via pip, the innards of the py2cfg command can be run right from the repo:\n\n### Run with pudb3\n```bash\npy2cfg <file.py> --debug\n```\n\n### Via wrapper\nIf you have not installed, then you can run a script present in the repo, `py2cfg/_runner.py`, to directly generate a CFG of a Python program and visualise it:\n```sh\ncd intoreporootdir\npython3 py2cfg/_runner.py path_to_my_code.py\n```\n\n### Via import\nWhether or not you have installed (easier if you have), to use py2cfg in your own python code, simply import the module in your Python interpreter or program.\nThen use the `py2cfg.CFGBuilder` class to build CFGs. \nFor example, to build the CFG of a program defined in a file with the path `./example.py`, the following code can be used:\n\n```py\nfrom py2cfg import CFGBuilder\n\ncfg = CFGBuilder().build_from_file('example', './example.py')\n```\n\nThis returns the CFG for the code in `./example.py` in the `cfg` variable. \nThe first parameter of `build_from_file` is the desired name for the CFG, and the second one is the path to the file containing the source code.\nThe produced CFG can then be visualised with:\n\n```py\ncfg.build_visual('exampleCFG', 'pdf')\n```\n\nThe first paramter of `build_visual` is the desired name for the DOT file produced by the method, and the second one is the format to use for the visualisation.\n\n\n# Contributing\n\n## Issues\nModifications and improvements to this project are driven via Gitlab-Issues.\nCheck them out to create one, or fix one.\n\n## Unit tests \nOur minimal tests are run via Gitlab-CI. \nMake sure you don't break them!\n\n## Type hinting\nNote: any new additions to the project should adhere to type-hinting standards enforced by:\n```sh\nmypy --strict --disallow-any-explicit *.py\n```\n* [ ] This is a current issue -- yes we need to fix some things...\n\n## Style\nTo maximize the ability of version control to pin down changes, and keep the style consistent, before you make any commit to the project, run this strict code auto-formatter:\n```sh\nblack py2cfg/*.py\n```\nDo so automatically with pre-commit:\nhttps://black.readthedocs.io/en/stable/version_control_integration.html\n\n# Project history\nNote: py2cfg took it's original inspiration from an older cfg project, though has long since diverged:\n* https://github.com/coetaur0/staticfg\n* https://pypi.org/project/staticfg/\n",
    'author': 'Joe Studer',
    'author_email': 'jmsxw4@mst.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/classroomcode/py2cfg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
