#Import arcpy to use ArcGIS tools
import arcpy

#Set environments
arcpy.env.overwriteOutput = True 
arcpy.env.addOutputsToMap = True

#Properties of your map: mxd and data frame
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]

#Parameters - information to collect from the user
parks = arcpy.GetParameterAsText(0) #type: feature layer
lands = arcpy.GetParameterAsText(1) #type: feature layer
outPath = arcpy.GetParameterAsText(2) #type: data element
finalName = arcpy.GetParameterAsText(3) #type: string

#Custom Functions
def makeFullPath(path, name):
    return path + "\\" + name

def removeLayersFromMap(layer):
	removeLayer = arcpy.mapping.Layer(layer)
	arcpy.mapping.RemoveLayer(df, removeLayer)

#Run 3 ArcPy Geoprocessing Tools
arcpy.Buffer_analysis(parks, makeFullPath('in_memory', "buff1320"),1320, "", "", "ALL")
arcpy.Clip_analysis("buff1320", lands, makeFullPath('in_memory', "clip1320"))
arcpy.SymDiff_analysis(lands, "clip1320", makeFullPath(outPath, finalName))

#execute custom function - remove intermediary products from map
removeLayersFromMap("buff1320")
removeLayersFromMap("clip1320")