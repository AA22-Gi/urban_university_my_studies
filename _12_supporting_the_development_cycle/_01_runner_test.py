import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        alex = runner.Runner('Alex')
        for _ in range(10):
            alex.walk()
        self.assertEqual(alex.distance, 50)

    def test_run(self):
        oleg = runner.Runner('Oleg')
        for _ in range(10):
            oleg.run()
        self.assertEqual(oleg.distance, 100)

    def test_challenge(self):
        vica = runner.Runner('Vica')
        marina = runner.Runner('Marina')
        for _ in range(10):
            vica.run()
            marina.walk()
        self.assertNotEqual(vica.distance, marina.distance)


if __name__ == '__main__':
    unittest.main()