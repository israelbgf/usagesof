import unittest

from core.usagesof import Usages, Formatter


__author__ = 'israel.bgf'


class UsagesOfTestCase(unittest.TestCase):

    def test_should_return_usages_when_queried_about(self):
        usages = Usages(from_file='sample_usages.txt')

        found = usages.lookup('git')
        expected = [('git commit', 'Commits current {staged} area to repository.')]

        self.assertEqual(found, expected)

    def test_should_return_formatted_output_on_console(self):
        formatter = Formatter()

        given = 'ls >>> list {current} directory'
        expected = '\033[1ls\033[0\n\nlist \033[1current\033[0 directory'

        self.assertEqual(expected, formatter.format(given))


if __name__ == '__main__':
    unittest.main()
