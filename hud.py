
from debilidades import debilidades

debilidad = debilidades()

class hud:

    # ━ ┃ ┏ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋

    @staticmethod
    def info_hud(criatura, all = False):
      # La información completa de un "pokemon" en especial.
      all_info = f"""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    Nam: {criatura.nombre}. Typ: {criatura.tipo}. HP: {criatura.vida}.
    Def: {criatura.defensa}. Dmg: {criatura.damage}. Vel: {criatura.velocidad}.

    Ataques:
    Nam: {(criatura.ataques[0]).nombre}. Typ: {(criatura.ataques[0]).tipo}. Use: {(criatura.ataques[0]).usos}.
    Dmg: {(criatura.ataques[0]).damage}. Acu: {(criatura.ataques[0]).precision}.
    Dsc: {(criatura.ataques[0]).descripcion}

    Nam: {(criatura.ataques[1]).nombre}. Typ: {(criatura.ataques[1]).tipo}. Use: {(criatura.ataques[1]).usos}.
    Dmg: {(criatura.ataques[1]).damage}. Acu: {(criatura.ataques[1]).precision}.
    Dsc: {(criatura.ataques[1]).descripcion}

    Nam: {(criatura.ataques[2]).nombre}. Typ: {(criatura.ataques[2]).tipo}. Use: {(criatura.ataques[2]).usos}.
    Dmg: {(criatura.ataques[2]).damage}. Acu: {(criatura.ataques[2]).precision}.
    Dsc: {(criatura.ataques[2]).descripcion}

    Nam: {(criatura.ataques[3]).nombre}. Typ: {(criatura.ataques[3]).tipo}. Use: {(criatura.ataques[3]).usos}.
    Dmg: {(criatura.ataques[3]).damage}. Acu: {(criatura.ataques[3]).precision}.
    Dsc: {(criatura.ataques[3]).descripcion}
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
      # Impresión del nombre y tipo.
      name_type_info = f"""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    Nam: {criatura.nombre}. Typ: {criatura.tipo}.
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
      return all_info if all == True else name_type_info

    # clase pokemon: nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
    # clase ataque: nombre, tipo, usos, damage, precision, descripcion    
    # same type attack bonus, efecto, variacion, nivel, ataque, potencia, defensa
    def combat_hud(criatura):
        # El campo de juego.
        hud = f"""
┏━━━━━━━━━━━━━━━━┓
  {criatura[1].nombre} HP: {criatura[1].vida}                   {criatura[1].sprite}
┗━━━━━━━━━━━━━━━━┛
                        ┏━━━━━━━━━━━━━━━━┓
        {criatura[0].sprite}                 {criatura[0].nombre} HP: {criatura[0].vida}
                        ┗━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  1. {(criatura[0].ataques[0]).nombre} PP: {(criatura[0].ataques[0]).usos}  
  2. {(criatura[0].ataques[1]).nombre} PP: {(criatura[0].ataques[1]).usos}
  3. {(criatura[0].ataques[2]).nombre} PP: {(criatura[0].ataques[2]).usos}  
  4. {(criatura[0].ataques[3]).nombre} PP: {(criatura[0].ataques[3]).usos}
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """
        return hud
