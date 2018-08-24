from extract import dataset
from operator import itemgetter
from extract import attribute_list,fname

attribute_list=attribute_list[:-1]
tempattlist = attribute_list[:]
usedattlist = []
def calculate(ccount,total):
	gini = 0.0
	for key in ccount:
		temp = (float(ccount[key])/float(total))
		gini+=(temp*temp)
	return (1-gini)
		

def findgini(att):
	finalgini = 0.0
	totalrec = 0.0
	ginirec = []
	totalrec = len(dataset)-1
	for key in att:
		ccount = {}
		for ele in att[key]:
			if ele not in ccount:
				ccount[ele] = 1
			else:
				ccount[ele]+=1
		temp = [key,calculate(ccount,len(att[key]))]
		ginirec.append(temp)
		temp = []
	
	for gini in ginirec:
		finalgini+=(float(gini[1])*float(len(att[gini[0]])))/float(totalrec)
	
	return finalgini

def findMin(gini):
	attList=[]
	giniList=[]
	for i in gini:
		attList.append(i[0])
		giniList.append(i[1])
	
	return attList[giniList.index(min(giniList))]
	
	
def findBestSplit(E):
	gini = []
	att = dict()
	for i in range(len(E[0])-1):
		if i not in usedattlist:
			for j in range(len(E)):
				if E[j][i] not in att:
					temp = []
					temp.append(E[j][len(E[0])-1])
					att[E[j][i]]=temp
				else:
					att[E[j][i]].append(E[j][len(E[0])-1])
			temp = [i,findgini(att)]
			gini.append(temp)
			#print gini	
			att.clear()
	
	return findMin(gini)
	#return min(i[1] for i in gini if i)

def classcount(E):
	d = dict()
	for rec in E:
		if rec[-1] not in d:
			d[rec[-1]] = 1
		else:
			d[rec[-1]]+=1
	return d


def Stopping_condition(E):
	if len(classcount(E)) == 1:
		return True
	
	if attribute_list == []:
		return True
		
	for i in range(len(E[0])-1):
		for j in range(1,len(E)-2):
			if (E[j][i] != E[j+1][i]):
				return False
				
	return False

def Classify(E):
	d = classcount(E)
	return max(d.iteritems(),key = itemgetter(1))[0]
	


def TreeGrowth(E):
	if not E:
		return
	if Stopping_condition(E) == True:
		label = Classify(E)
		#print label
		return label
	else:
		#print E
		root = dict()
		bestsplit = int(findBestSplit(E))
		V = dict()
		usedattlist.append(bestsplit)
		bestatt = dataset[0][bestsplit]
		attribute_list.remove(bestatt)
		root[bestatt] = {}
		for i in range(len(E)):
			if E[i][bestsplit] not in V:
				V[E[i][bestsplit]] = []
				V[E[i][bestsplit]].append(E[i])
			else:
				V[E[i][bestsplit]].append(E[i])
		for key in V:
			root[bestatt][key] = TreeGrowth(V[key])
	return root

E = dataset[1:]
#print findBestSplit(E)
dt=TreeGrowth(E)

test_attr=[]

def decision(dt,line):

	if type(dt) is not dict:
		return dt
	else:
		dk=dt.keys()[0]
		dt=dt[dk][line[test_attr.index(dk)]]
		#print dt
		return decision(dt,line)
		
fh=open(fname,'r')
i=0
count=0
tot=0
for line in fh:
	if i==0:
		test_attr=line.split(',')
		i+=1
		continue
	tot+=1
	lineSplit=line.split(',')
	target=decision(dt,lineSplit[:-1])
	2
	if target ==  lineSplit[-1].strip():
		count+=1
		
print 'Accuracy - ',((float(count)/tot)*100)
	















