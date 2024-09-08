import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        alex = runner.Runner('Alex')
        for _ in range(10):
            alex.walk()
        self.assertEqual(alex.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        oleg = runner.Runner('Oleg')
        for _ in range(10):
            oleg.run()
        self.assertEqual(oleg.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        vica = runner.Runner('Vica')
        marina = runner.Runner('Marina')
        for _ in range(10):
            vica.run()
            marina.walk()
        self.assertNotEqual(vica.distance, marina.distance)


if __name__ == '__main__':
    unittest.main()
