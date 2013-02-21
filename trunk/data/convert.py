import os,sys


def convert(tabContent):
	nodeDict=dict()
	retString="<?xml version=\"1.0\" encoding=\"UTF-8\"?><graphml>\n" 
	retString+="<key id=\"label\" for=\"all\" attr.name=\"label\" attr.type=\"string\"/>\n"
	retString+="<key id=\"weight\" for=\"all\" attr.name=\"weight\" attr.type=\"double\"/>\n"
	retString+="<graph id=\"G\" edgedefault=\"undirected\">\n"
	
	edgeString=""
	nodeString=""
	nodeId=0
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
			nodeString+=" <node id=\""+str(nodeId)+"\">  <data key=\"label\">"+n1+"</data></node>\n"
		if n2 not in nodeDict:
			nodeId+=1
			nodeDict[n2]=nodeId
			nodeString+=" <node id=\""+str(nodeId)+"\">  <data key=\"label\">"+n2+"</data></node>\n"
		edgeString+="<edge source=\""+str(nodeDict[n1])+"\" target=\""+str(nodeDict[n2])+"\"> <data key=\"weight\">"+w+"</data></edge>\n"

	retString+=nodeString+edgeString+"</graph></graphml>"	
	return retString

print convert(open(sys.argv[1]).read())
