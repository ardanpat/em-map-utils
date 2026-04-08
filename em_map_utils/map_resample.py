"""
map_resample.py

:Author: Ardan Patwardhan
:Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
:Date: 13/03/2026
:Description: 
    Rescale a map. Can be used to make a map smaller or to oversample it.
"""

import argparse
import mrcfile
import numpy as np
from scipy import ndimage
from .util import save_map

def map_resample(map_grid,
                 sampling_factor,
                 centre_coos = None,
                 fill_value = 0.0,
                 spline_order = 3,
                 dtype = np.float32):
    sampling_factor = float(sampling_factor)
    max_indices = np.array(map_grid.shape) - 1.0
    centre_coos = np.asarray(centre_coos) if centre_coos is not None else  max_indices / 2.0
    pos_range = [np.arange(centre_coos[i], max_indices[i], sampling_factor) for i in range(map_grid.ndim)]
    neg_range = [np.arange(centre_coos[i], 0, -sampling_factor)[1:][::-1] for i in range(map_grid.ndim)]
    full_range = tuple(np.concatenate((neg_range[i], pos_range[i])) for i in range(map_grid.ndim))

    coos_grid = np.meshgrid(*full_range, indexing='ij')
    coords = np.reshape(coos_grid, (map_grid.ndim, -1))

    resampled_values = ndimage.map_coordinates(map_grid, coords, order=spline_order, output=dtype, cval = fill_value)
    resampled_grid = np.reshape(resampled_values, coos_grid[0].shape)

    return resampled_grid


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Resample map. Note: Coordinate system is (i,j,k) going from the slowest to fastest varying axis. (i,j,k) map to (Z,Y,X) here.')
    parser.add_argument('infile', metavar='FILE', type=str, help="Map file to resample.")
    parser.add_argument("outfile", metavar='FILE', type=str, help="Resampled map.")
    parser.add_argument('sampling', metavar='RRR', type=float, default = 2.0, help="Sampling factor to use when resampling map. E.g., sampling=2 will reduce each dimension by a factor of two.")
    parser.add_argument('-c', '--centre', metavar='XXX', type=float, nargs=3, help='Centre for resampling. If none specified, will default to centre of box.')
    parser.add_argument('-i', '--int_order', metavar='VAL', type=int, default=3, help='Spline interpolation order.')
    parser.add_argument('-f', '--fill_value', metavar='VAL', type=float, default=0.0, help='Map value to use when interpolated points lie outside the box.')
    args = parser.parse_args()

    with mrcfile.open(args.infile) as mrc:

        resampled_grid = map_resample(mrc.data,
                                      sampling_factor = args.sampling,
                                      centre_coos = args.centre,
                                      spline_order = args.int_order,
                                      fill_value = args.fill_value)

        # Save rotated map to file
        voxel_size = mrc.voxel_size.copy()
        voxel_size.x = voxel_size.x * args.sampling
        voxel_size.y = voxel_size.y * args.sampling
        voxel_size.z = voxel_size.z * args.sampling
        save_map(args.outfile, resampled_grid, mrc, voxel_size)