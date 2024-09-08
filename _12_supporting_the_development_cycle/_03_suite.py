import unittest
import _01_runner_test
import _02_tournament_test

general_tests = unittest.TestSuite()
general_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(_01_runner_test.RunnerTest))
general_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(_02_tournament_test.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(general_tests)