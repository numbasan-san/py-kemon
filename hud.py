
class hud:

    # ━ ┃ ┏ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋

    @staticmethod
    def info_hud(criatura):
        hud = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    Nam: {}. Typ: {}. HP: {}.
    Def: {}. Dmg: {}. Vel: {}.
    Spt: {}.
    
    Atk 1: {}
    Atk 2: {}
    Atk 3: {}
    Atk 4: {}
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """.format(criatura.nombre, criatura.tipo, criatura.vida, 
                       criatura.defensa, criatura.damage, criatura.velocidad, 
                       criatura.sprite, criatura.ataques[0], criatura.ataques[1], 
                       criatura.ataques[2], criatura.ataques[3])
        print(hud)

    @staticmethod
    def combat_hud(criatura):
        hud = """
┏━━━━━━━━━━━━━━━━┓
  {} HP: {}                   {}
┗━━━━━━━━━━━━━━━━┛
                        ┏━━━━━━━━━━━━━━━━┓
        {}                 {} HP: {}
                        ┗━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃                         ┃              ┃
┃                         ┃              ┃
┃                         ┃              ┃
┃                         ┃              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┛
        """.format(criatura[1].nombre, criatura[1].vida, criatura[1].sprite, 
                   criatura[0].sprite, criatura[0].nombre, criatura[0].vida)
        print(hud)
