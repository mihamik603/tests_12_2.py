import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False

    def run(self, distance):
        time = distance / self.speed
        return time

    def walk(self, distance):
        time = distance / (self.speed / 2)
        return time

class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for runner in self.participants:
            time_taken = runner.run(self.distance)
            results[time_taken] = runner.name
        return dict(sorted(results.items()))


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner(name="Усэйн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_usain_nick(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner3])
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(distance=90, participants=[self.runner2, self.runner3])
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner2, self.runner3])
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

if __name__ == '__main__':
    unittest.main()
