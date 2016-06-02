#!/usr/bin/env python
import shapefile_point
import sys
import os

e=shapefile_point.Editor('app_chicago/Flint/flint.shp')
#e=shapefile_point.Editor('app_chicago/outsideFlint/outsideFlint.shp')
e.buildQuadTree('app_chicago/quadTreeFlint.txt')
#e.buildQuadTree('app_chicago/quadTreeOutsideFlint.txt')

#c=0
#print 'started'

for line in sys.stdin:
    tmp = line.strip().split(',')
    ##ind=e.index_of_first_feature_contains_point(float(tmp[2]),float(tmp[1]))
    #ind=e.index_of_nn_feature(float(tmp[0]),float(tmp[1]))
    mID=e.index_of_closest_feature_to_points(float(tmp[0]),float(tmp[1]))
    #c=c+1
    if mID !=-1:
        #xx = e.records[int(ind)][1]
        #print line.strip()+','+ str(ind) 
        #+ ',' + str(xx)
        temp = ""
        for item in mID:
            temp = temp + "," + str(item)
        print line.strip()+temp#+','+str(mDist)

##    [mID, mDist]=e.dist_to_boundary(float(tmp[1]),float(tmp[2]))
##    if mID != -1:
##        print line.strip()+','+str(mID)+','+str(mDist)
    #print c
