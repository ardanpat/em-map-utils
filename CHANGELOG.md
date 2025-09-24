# Release Notes

## [0.0.3] - 2025/09/19

### Updates
* The multiprocessing package did not work after the MacOS v26.0 Tahoe update. Changed to using the multiprocess package
    spawn instead. This change affects download_emdb.py and structure_size_and_shape.py.

### Additions
* Added timeout to farm_function.py to set a max time limit on the execution of a function.
    This is used by download_emdb.py and structure_size_and_shape.py.
* Added explicit garbage collection at each monitoring interval in farm_function.py.
