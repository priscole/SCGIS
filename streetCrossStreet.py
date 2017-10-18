""" Part 1: Setup and Run Intersect Tool """
#Variable assignment
GDB = 
streets = 
nodes = 
InterFileName = 

#Intersect Analysis GP Tool
InterFile = arcpy.Intersect_analysis(
	in_features = [streets, nodes], 
	out_feature_class = GDB + "\\" + InterFileName, #Concatenation
	join_attributes="", 
	cluster_tolerance="", 
	output_type="POINT") #Use points option

StreetIDColumn = 
JunctionColumn = 

###################################################################################
""" Part 2: Digest Results of Intersect with Python Dictionaries"""

#Associates NodeID with Street Names
nodeIdStreets = {} #Dictionary
for node in arcpy.da.SearchCursor(InterFile, [JunctionColumn, 'Street']):
	if node[0] in nodeIdStreets: #if/else - control flow
		nodeIdStreets[node[0]].add(node[1]) #set - get rid of duplicates
	else:
		nodeIdStreets[node[0]] = {node[1]}

#Associates StreetID with all of its Junctions
streetIDNodes = {} 
for street in arcpy.da.SearchCursor(InterFile, [StreetIDColumn, JunctionColumn]):
	if street[0] in streetIDNodes:
		streetIDNodes[street[0]].append(street[1]) #list of Junction IDs
	else:
		streetIDNodes[street[0]] = [street[1]]

""" FLIP TO SLIDE 19 """
###################################################################################
""" Part 3: Populate Streets Table with Cross Streets using arcpy Update Cursor """


#Update Streets table with cross streets
with arcpy.da.Editor(GDB) as edit: #Open edit session because of geometric network
	with arcpy.da.UpdateCursor(streets, ['OBJECTID', 'Street', "CrossSt1", "CrossSt2"]) as Cursor: 
		for row in Cursor:	
			streetList1 = [street for street in nodeIdStreets[streetIDNodes[row[0]][0]] if street != row[1]]
			row[2] = ", ".join(streetList1)
			if len(streetIDNodes[row[0]]) > 1: #see StreetOID 5694, 6493, 12187, 13406
				streetList2 = [street for street in nodeIdStreets[streetIDNodes[row[0]][1]] if street != row[1]]
				row[3] = ", ".join(streetList2)
			Cursor.updateRow(row)