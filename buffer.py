arcpy.Buffer_analysis(
	in_features="Parks_SI", 
	out_feature_class="C:/Users/Priscole/Documents/ArcGIS/NYC/SCGisTalk.gdb/parkBuff1320", 
	buffer_distance_or_field="1320", 
	line_side="", 
	line_end_type="", 
	dissolve_option="ALL", 
	dissolve_field="", 
	method="")

arcpy.Clip_analysis(
	in_features="parkBuff1320", 
	clip_features="StatenIsland", 
	out_feature_class="C:/Users/Priscole/Documents/ArcGIS/NYC/SCGisTalk.gdb/park1320Clip", 
	cluster_tolerance="")

arcpy.SymDiff_analysis(
	in_features="StatenIsland", 
	update_features="park1320Clip", 
	out_feature_class="C:/Users/Priscole/Documents/ArcGIS/NYC/SCGisTalk.gdb/SymDiff1320", 
	join_attributes="", 
	cluster_tolerance="")