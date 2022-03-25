# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['docspec']

package_data = \
{'': ['*']}

install_requires = \
['Deprecated>=1.2.12,<2.0.0', 'databind>=1.5.0,<2.0.0']

entry_points = \
{'console_scripts': ['docspec = docspec.__main__:main']}

setup_kwargs = {
    'name': 'docspec',
    'version': '2.0.1',
    'description': 'Docspec is a JSON object specification for representing API documentation of programming languages.',
    'long_description': '# docspec\n\nThis Python packages provides\n\n* A library to (de-) serialize Docspec conformat JSON payloads\n* A CLI to validate and introspect such payloads\n\nExample:\n\n```py\nimport docspec, sys\nfor module in docspec.load_modules(sys.stdin):\n  module.members = [member for member in module.members if member.docstring]\n  docspec.dump_module(sys.stdout)\n```\n\n```\n$ docspec module.json --dump-tree\nmodule docspec\n| class Location\n| | data filename\n| | data lineno\n| class Decoration\n| | data name\n# ...\n```\n\nThe `docspec` Python module requires Python 3.5 or newer.\n\n---\n\n<p align="center">Copyright &copy; 2020, Niklas Rosenstein</p>\n',
    'author': 'Niklas Rosenstein',
    'author_email': 'rosensteinniklas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NiklasRosenstein/docspec/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
