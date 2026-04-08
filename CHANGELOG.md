# Release Notes

## [0.1.0] - 2025/04/08

### Updates
* The thresholding strategy in map_thresholdhas been changed as the previous one failed in a few cases where the new 
    strategy does not. The new strategy involves calculating the threshold in 2 different ways and taking the average 
    value. First the background sigma in the map is estimated and a threshold is calculated based on this. The map is 
    thresholded and then orthogonal line projection profiles are calculated. The widths of the profiles are calculated 
    and used to estimate the volume of the structure. The cumulative histogram of the map is then scanned from the 
    right until the number of voxels is equivalent to the estimated volume of the structure and the point on the 
    histogram is taken as a second threshold.  These two values are averaged to a final value.
* structure_size_and_shape.py was often crashing when used in multiprocessing mode and running on large maps. The
    parameter max_map_size has been added. If any map dimension exceeds this value, the map is rescaled before running 
    the program.
* structure_size_and_shape.py now also calculates max eccentricity defined as:
    np.fabs(1 - min_width / max_width).

### Additions
* Added map_resample.py to downsample or upsample maps.


## [0.0.3] - 2025/09/19

### Updates
* The multiprocessing package did not work after the MacOS v26.0 Tahoe update. Changed to using the multiprocess package
    spawn instead. This change affects download_emdb.py and structure_size_and_shape.py.

### Additions
* Added timeout to farm_function.py to set a max time limit on the execution of a function.
    This is used by download_emdb.py and structure_size_and_shape.py.
* Added explicit garbage collection at each monitoring interval in farm_function.py.
