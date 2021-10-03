from nose.tools import eq_

import feedly_to_linkace.main


class TestMain:
    def test_hello(self):
        eq_(feedly_to_linkace.main.hello(), "Hello, pipenv app.")
