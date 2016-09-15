8class Buff(object):
	def __init__(self, time, name='buff', defence=0, damage_plus=0, mana_damage_plus=0, heal=0, damage=0, charisma=0, gold_bonus=1):
		super(Buff, self).__init__()
		self.time = time
		self.name = name
		self.defence = defence
		self.damage_plus = damage_plus
		self.mana_damage_plus = mana_damage_plus
		self.heal = heal
		self.damage = damage
		self.charisma = charisma
		self.gold_bonus = gold_bonus

	def get_name(self):
		try:
			return self.name
		except Exception:
			return 'buff'

	def on_room(self, user, reply, room):
		self.time -= 1

	def on_end(self, user, reply, room):
		pass
		
class RainbowBuff(Buff):
	def __init__(self):
		super(RainbowBuff, self).__init__(50, name='rainbow', mana_damage_plus=50)

class DevilPower(Buff):
	def __init__(self,):
		super(DevilPower, self).__init__(8, name='devilpow', damage_plus=3000000)
	def on_end(self, user, reply, room):
		user.death(reply, reason='Сделка с дьяволом')

class DevilInt(Buff):
	def __init__(self,):
		super(DevilInt, self).__init__(8, name='devilint', mana_damage_plus=3000000)
	def on_end(self, user, reply, room):
		user.death(reply, reason='Сделка с дьяволом')

class DevilMoney(Buff):
	def __init__(self,):
		super(DevilMoney, self).__init__(8, name='devilmon', mana_damage_plus=0)
	def on_end(self, user, reply, room):
		user.death(reply, reason='Сделка с дьяволом')
		user.remove_item('lepergold')

class DevilEntity(Buff):
	def __init__(self,):
		super(DevilEntity, self).__init__(8, name='devilent', damage_plus=3000000, mana_damage_plus=3000000)
	def on_end(self, user, reply, room):
		user.death(reply, reason='Сделка с дьяволом')
		user.remove_item('lepergold')
