from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        enemies = cast.get_actors(ENEMY_GROUP)
        if len(enemies) == 0:
            stats = cast.get_first_actor(STATS_GROUP)
            stats.next_level()
            callback.on_next(NEXT_LEVEL)
