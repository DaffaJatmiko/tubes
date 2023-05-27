from sprite_obj import *
from npc import *

class ObjectsHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'sprite/NPC/'
        self.static_sprite_path = 'sprite/Static/'
        self.anim_sprite_path = 'sprite/Animated/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_pos = {}

        # Sprite Map
        add_sprite(PantungUtuh(game, pos=(1.5, 3.5)))
        add_sprite(PantungUtuh(game, pos=(1.5, 6.5)))
        add_sprite(ApiBiru(game, pos=(1.5, 2.5)))
        add_sprite(ApiKuning(game, pos=(1.5, 7.5)))
        add_sprite(Pillar(game, pos=(27, 4)))
        add_sprite(Pillar(game, pos=(28, 4)))
        add_sprite(Pillar(game, pos=(27, 6)))
        add_sprite(Pillar(game, pos=(28, 6)))
        add_sprite(Buku(game, pos=(27.5, 6)))
        add_sprite(PantungUtuh(game, pos=(28, 17.5)))
        add_sprite(PantungUtuh(game, pos=(25, 17.5)))
        add_sprite(Sphere(game, pos=(27.5, 5)))
        add_sprite(Candle(game, pos=(27, 5)))
        add_sprite(Candle(game, pos=(27.5, 4)))
        add_sprite(Candle(game, pos=(28, 5)))

        # NPC map
        add_npc(Pig(game, pos=(27.5, 2)))
        add_npc(Mino(game, pos=(17, 23)))
        add_npc(Mino(game, pos=(17, 21)))
        add_npc(Flame(game, pos=(3, 27)))
        add_npc(Flame(game, pos=(8, 9)))
        add_npc(Flame(game, pos=(20, 4)))
        add_npc(Tentara(game, pos=(24, 17)))
        add_npc(Tentara(game, pos=(12, 1)))
        add_npc(Tentara(game, pos=(16, 9)))
        add_npc(NPC(game, pos=(12, 2.5)))

    def check_win(self):
        if not len(self.npc_pos):
            self.game.game_win()

    def update(self):
        for sprite in self.sprite_list:
            sprite.update()
        for npc in self.npc_list:
            npc.update()
        self.npc_pos = [
            npc.map_pos for npc in self.npc_list if npc.alive]
        self.check_win()
    
    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)