import os,sys


def convert(tabContent,promoterset):
	nodeDict=dict()
	retString="<?xml version=\"1.0\" encoding=\"UTF-8\"?><graphml>\n" 
	retString+="<key id=\"label\" for=\"all\" attr.name=\"label\" attr.type=\"string\"/>\n"
	retString+="<key id=\"petcount\" for=\"edge\" attr.name=\"petcount\" attr.type=\"double\"/>\n"
	retString+="<key id=\"degree\" for=\"node\" attr.name=\"degree\" attr.type=\"double\"/>\n"
	retString+="<key id=\"promoter\" for=\"node\" attr.name=\"promoter\" attr.type=\"string\"/>\n"
	retString+="<graph id=\"G\" edgedefault=\"undirected\">\n"
	
	edgeString=""
	nodeString=""
	nodeId=0
	nodeDegree=dict()
	for line in tabContent.split("\n"):
		comps=line.strip().split()
		if len(comps)<2:
			continue
		n1=comps[0]
		n2=comps[1]
		w=comps[2]
		if n1 not in nodeDict:
			nodeId+=1
			nodeDict[n1]=nodeId
			nodeDegree[n1]=0
		if n2 not in nodeDict:
			nodeId+=1
			nodeDict[n2]=nodeId
			nodeDegree[n2]=0
		nodeDegree[n1]+=1
		nodeDegree[n2]+=1
		edgeString+="<edge source=\""+str(nodeDict[n1])+"\" target=\""+str(nodeDict[n2])+"\"> <data key=\"petcount\">"+w+"</data></edge>\n"

#node string
	for node in nodeDict:
		nodeString+=" <node id=\""+str(nodeDict[node])+"\">  <data key=\"label\">"+node+"</data><data key=\"degree\">"+str(nodeDegree[node])+"</data> <data key=\"promoter\">"+str(node in promoterset)+"</data></node>\n"
	retString+=nodeString+edgeString+"</graph></graphml>"	
	return retString


promoterset=set()
if len(sys.argv)>2:
	lines=open(sys.argv[2],'r').readlines()
	for line in lines:
		comps=line.strip().split("=")
		if len(comps)<2:
			 continue
		if "Yes" in comps[1]:
			promoterset.add(comps[0].strip())
print convert(open(sys.argv[1]).read(),promoterset)
