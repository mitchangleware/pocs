import os
import subprocess
import sys
import unittest

# /path/to/demos/maximum-cut/tests/test_maximum_cut.py
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDemo(unittest.TestCase):
    def test_smoke(self):
        """run maximum_cut.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'maximum_cut.py')
        subprocess.check_output([sys.executable, demo_file])

    def test_maximum_cut(self):
        demo_file = os.path.join(project_dir, 'maximum_cut.py')
        output = subprocess.check_output([sys.executable, demo_file])
        output = str(output).upper()
        if os.getenv('DEBUG_OUTPUT'):
            print("Example output \n" + output)

        # TODO
        #        with self.subTest(msg="Verify if output ... \n"):
        #    self.assertIn("??".upper(), output)