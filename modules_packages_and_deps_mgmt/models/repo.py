import json
import sys


class Repo:
    name: str = ''
    full_name: str = ''
    forks: int = 0,
    stars: int = 0,
    url: str = ''

    def __init__(self, name: str, full_name: str, forks: int, stars: int, url: str):
        self.name = name
        self.full_name = full_name
        self.forks = forks
        self.stars = stars
        self.url = url

    def __str__(self):
        '''__str__ is similar to overriding ToString() in C#'''
        return f'{self.full_name} ⭐ {self.stars}'

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __private_func_demo():
        """private methods are prefixed with double underscores. This won't be visible when called from app.py"""
        print("this is an exmaple private func for Repo class")

    @staticmethod
    def from_dict(dict):
        """static method - called on the class itself as opposted to its instance"""
        return Repo(dict['name'],
                    dict['full_name'], dict['forks'], dict['stargazers_count'],
                    dict['url'])


if __name__ != "__main__":
    print(f"{__name__} imported via {sys.argv[0]}")