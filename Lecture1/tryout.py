class Food(object):
	def__init__(self,n,v,w):
		self.name = n
		self.value = v
		self.calories = w
	def getValue(self):
		return self.value
	def getCost(self):
		return self.calories
	def density(self):
		return self.getValue()/self.getCost()
	def __str__(self):
		return self.name + ':<' + str(self.value)+', '+str(self.calories)+'>'

def buildMenu(names,values,calories):
	"""returns list of foods """
	menu = []
	for i in range(len(values)):
		menu.append(Food(names[i],values[i],calories[i]))
	return menu
def greedy(items,maxUnits,keyFunction):
	"""returns list of items and total values of items"""
	itemsCopy = sorted(items, key = keyFunction,reverse = True)
	result = []
	totalValue,totalCost = 0.0
	for i in range(len(itemsCopy)):
		if(totalCost+itemsCopy[i].getCost())<=maxUnits:
			result.append(itemsCopy[i])
			totalValue += itemsCopy[i].getValue()
			totalCost += itemsCopy[i].getCost()
	return (result,totalValue)
def testGreedy(items,maxUnits,keyFunction):
	taken,val = greedy(items,maxUnits,keyFunction)
	print('Total value taken ',val)
	for item in taken:
		print(' ',item)
def testGreedys(items,maxUnits):
	testGreedy(items,maxUnits,Food.getValue)
	print('Use greedy by value to allocate',maxUnits,'calories')
	testGreedy(items,maxUnits,Food.getCost)
	print('Use greedy by cost to allocate',maxUnits,'calories')
	testGreedy(items,maxUnits,lambda x: 1/Food.getCost(x))		
	print('Use greedy by density to allocate',maxUnits,'calories')
	testGreedy(items,maxUnits,Food.density)
names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names,values,calories)
testGreedys(foods,1000)
		
