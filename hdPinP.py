#!/usr/bin/env python
import shapefile
import sys
import os

e=shapefile.Editor('app_chicago/xx/2015ParcelswConnType.shp')
e.buildQuadTree('app_chicago/quadTree2.txt')

## this is the file to find point to polygon ##

for line in sys.stdin:
    tmp = line.strip().split(',')
    ##ind=e.index_of_first_feature_contains_point(float(tmp[2]),float(tmp[1]))
    #ind=e.index_of_nn_feature(float(tmp[0]),float(tmp[1]))
    [mID, mDist]=e.dist_to_boundary(float(tmp[0]),float(tmp[1]))
    if mID !=-1:
        #xx = e.records[int(ind)][1]
        #print line.strip()+','+ str(ind) 
        #+ ',' + str(xx)
        print line.strip()+','+str(mID)+','+str(mDist)

##    [mID, mDist]=e.dist_to_boundary(float(tmp[1]),float(tmp[2])) 
# above find both ID and distance
##    if mID != -1:
##        print line.strip()+','+str(mID)+','+str(mDist)

