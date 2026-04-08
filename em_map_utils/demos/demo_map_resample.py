"""
demo_map_resample.py

:Author: Ardan Patwardhan
:Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
:Date: 13/03/2026
:Description: 
    Rescale a map and show orthogonal surface views of the initial and
    resampled map. If no map is provided, a cuboid is used.
"""

import argparse
import matplotlib.pyplot as plt
import mrcfile
from scipy.spatial.transform import Rotation as R
from ..filled_cuboid import filled_cuboid
from ..map_resample import map_resample
from .ortho_surface_views import ortho_surface_views

def plot_resampled_map(in_file, lengths, box_size, sampling, out_file):

    mrc = None
    if in_file is None:
        map_grid = filled_cuboid(lengths=lengths, box_size=box_size)
    else:
        mrc = mrcfile.open(in_file)
        map_grid = mrc.data

    fig1, ax1 = ortho_surface_views(map_grid, fig_title="Input map")

    resampled_grid = map_resample(map_grid,
                                  sampling_factor=args.sampling)

    fig2, ax2 = ortho_surface_views(resampled_grid, fig_title="Resampled map")
    if out_file:
        fig2.savefig(out_file)
    plt.show()

    if mrc is not None:
        mrc.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Plot orthogonal surface views of a resampled cuboid. Note: Coordinate system is (i,j,k) going from the slowest to fastest varying axis.')
    parser.add_argument('-i', '--infile', metavar='FILE', type=str,
                        help='Optional input file. If none specified, a cuboid is used.')
    parser.add_argument('-o', '--outfile', metavar='FILE', type=str, help='Optional file to save the figure to.')
    parser.add_argument('-l', '--lengths', metavar='ZZZ', type=float, nargs=3, default=[70, 40, 20],
                        help='Cuboid dimensions (i,j,k) in voxels.')
    parser.add_argument('-b', '--box_size', metavar='XXX', type=int, nargs=3, default=[100, 100, 100],
                        help='Three lengths of the sides (i,j,k) of the box in voxels.')
    parser.add_argument('-s', '--sampling', metavar='TTT', type=float, default = 2.0,
                        help='Resample by this factor.')

    args = parser.parse_args()
    plot_resampled_map(args.infile, args.lengths, args.box_size, args.sampling, args.outfile)