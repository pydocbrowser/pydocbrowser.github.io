#! /usr/bin/env python

# $Id: test_target_notes.py 8765 2021-06-17 09:59:43Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for the target-notes directives.
"""
from __future__ import absolute_import

if __name__ == '__main__':
    import __init__
from test_parsers import DocutilsTestSupport


def suite():
    s = DocutilsTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

totest = {}

totest['target-notes'] = [
["""\
.. target-notes::
""",
"""\
<document source="test data">
    <pending>
        .. internal attributes:
             .transform: docutils.transforms.references.TargetNotes
             .details:
"""],
["""\
.. target-notes:: :class: custom
""",
"""\
<document source="test data">
    <pending>
        .. internal attributes:
             .transform: docutils.transforms.references.TargetNotes
             .details:
               class: ['custom']
"""],
["""\
.. target-notes::
   :class: custom
   :name: targets
""",
"""\
<document source="test data">
    <pending ids="targets" names="targets">
        .. internal attributes:
             .transform: docutils.transforms.references.TargetNotes
             .details:
               class: ['custom']
"""],
["""\
.. target-notes::
   :class:
""",
"""\
<document source="test data">
    <system_message level="3" line="1" source="test data" type="ERROR">
        <paragraph>
            Error in "target-notes" directive:
            invalid option value: (option: "class"; value: None)
            argument required but none supplied.
        <literal_block xml:space="preserve">
            .. target-notes::
               :class:
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
