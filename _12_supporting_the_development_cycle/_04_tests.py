import logging
import rt_with_exceptions
import unittest

FORMAT = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='UTF-8', format=FORMAT)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            alex = rt_with_exceptions.Runner('Alex', -5)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                alex.walk()
            self.assertEqual(alex.distance, 50)
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            oleg = rt_with_exceptions.Runner({'Oleg'}, 5)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                oleg.run()
            self.assertEqual(oleg.distance, 100)
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        vica = rt_with_exceptions.Runner('Vica')
        marina = rt_with_exceptions.Runner('Marina')
        for _ in range(10):
            vica.run()
            marina.walk()
        self.assertNotEqual(vica.distance, marina.distance)


if __name__ == '__main__':
    unittest.main()
