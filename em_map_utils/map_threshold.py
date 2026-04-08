"""
map_threshold.py

:Author: Ardan Patwardhan
:Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
:Date: 05/08/2025
:Description:
    Threshold map.
"""

import argparse
import logging
import matplotlib.pyplot as plt
import mrcfile
import numpy as np
from numpy import dtype

from .map_line_projections import MapLineProjections
from .util import save_map

logger = logging.getLogger(__name__)

class MapHistogram:
    """
    Class to represent the map histogram, the related cumulative
    distribution function and histogram of the background (noise) in a
    map.
    """

    def plot_map_histogram(self, log_y = True):
        """
        Plot the map histogram.

        :param log_y: If True, log scale the y-axis of the map histogram.
        :return: A tuple with the figure and axes objects.
        """
        fig, ax = plt.subplots()
        if log_y:
            plt.yscale('log')
        ax.plot(self.bins[:-1], self.map_histogram)

        ax.set(xlabel='Intensity', ylabel='Normalised frequency',
               title='Histogram')
        return fig, ax

    def plot_map_cdf(self):
        """
        Plot the map cumulative distribution function.

        :return: A tuple with the figure and axes objects.
        """
        fig, ax = plt.subplots()

        ax.plot(self.bins[:-1], self.cum_dist_func)

        ax.set(xlabel='Intensity', ylabel='Cumulative frequency',
               title='Cumulative Distribution Function')
        return fig, ax

    def plot_bg_histogram(self, log_y = True):
        """
        Plots the background histogram.

        :param log_y: If True, log scale the y-axis of the map histogram.
        :return: A tuple with the figure and axes objects.
        """
        fig, ax = plt.subplots()
        if log_y:
            plt.yscale('log')
        ax.plot(self.bg_histogram)

        ax.set(xlabel='Index', ylabel='Normalised frequency',
               title='Background histogram')
        return fig, ax

    def __init__(self, map_grid, histogram_bins = 5000, sigma_factor = 3.0, log_histogram = False):
        """
        Calculate the histogram of an input map and estimate the
        background level. It is assumed that the strongest peak in the
        histogram is due to background and is to the left of the signal.
        Hence, the part of the histogram to the left of the peak will be
        mainly due to background.

        :param map_grid: 3D input map.
        :param histogram_bins: Number of bins to use for the histogram.
        :param sigma_factor: The background level is set to the
            intensity of the peak + this factor multiplied by the
            standard deviation. of the peak.
        :param log_histogram: If True, scale the y-axis of the
            histogram by the log of 1 + original y values.
        """

        self.sigma_factor = sigma_factor

        # Make histogram of map
        self.map_histogram, self.bins = np.histogram(map_grid.astype(np.float64), bins=histogram_bins, density=True)
        if log_histogram:
            self.map_histogram = np.log10(self.map_histogram + 1.0)
        self.bin_width = self.bins[1] - self.bins[0]

        # Cumulative distribution function of map histogram
        self.cum_dist_func = np.cumsum(self.map_histogram) * self.bin_width

        # Find index of peak (mode) in histogram
        self.map_hist_peak_idx = np.argmax(self.map_histogram)
        self.map_hist_peak_val = self.bins[self.map_hist_peak_idx] + 0.5 * self.bin_width

        # Check if peak_idx = 0
        if self.map_hist_peak_idx == 0:
            logger.debug("Warning: Histogram peak found at index = 0 which is abnormal.")

        # Check if peak_idx is equal to the max histogram index
        if self.map_hist_peak_idx == self.map_histogram.size - 1:
            logger.debug("Warning: Histogram peak found at right edge of histogram which would imply no information to the right of background peak.")
            logger.debug("Warning: Using index of the left edge of the histogram instead.")
            self.map_hist_peak_idx = 0

        # Calculate map histogram stats
        mhist_sum = np.sum(self.map_histogram)
        mhist_grid = self.bins[:-1] + 0.5 * self.bin_width

        self.map_mean = (np.dot(self.map_histogram, mhist_grid) / mhist_sum)
        self.map_var = (np.dot(self.map_histogram, mhist_grid**2) / mhist_sum) - self.map_mean ** 2
        self.map_sigma = np.sqrt(self.map_var)

        # Make new histogram taking the old one up to the peak and then mirroring it onto the right
        if self.map_hist_peak_idx == 0:
            self.bg_histogram = self.map_histogram[0:1]
        else :
            self.bg_histogram = np.concatenate((self.map_histogram[0:self.map_hist_peak_idx + 1], self.map_histogram[self.map_hist_peak_idx - 1::-1]))

        # Calculate stats of background histogram

        bhist_len = np.size(self.bg_histogram)
        bhist_grid = np.ogrid[0:bhist_len]

        self.bg_hist_sum = np.sum(self.bg_histogram)
        self.bg_frac = self.bg_hist_sum / np.sum(self.map_histogram)
        self.bg_mean_idx = np.dot(bhist_grid, self.bg_histogram) / self.bg_hist_sum
        self.bg_var_idx = (np.dot(bhist_grid**2, self.bg_histogram) / self.bg_hist_sum) - self.bg_mean_idx**2
        self.bg_mean = self.bins[0] + self.bg_mean_idx * self.bin_width
        self.bg_var = self.bg_var_idx * self.bin_width**2
        self.bg_sigma = np.sqrt(self.bg_var)

        # If the sigma factor results in a threshold greater than the
        # max value of the histogram, take the average of the max value
        # and the background mean.
        self.bg_threshold = min(self.bg_mean + sigma_factor * self.bg_sigma,
                                   (self.bg_mean + self.bins[histogram_bins]) / 2.0)

    def __str__(self):
        str = f"Histogram info:\n" + \
              f"Index of peak in map histogram is {self.map_hist_peak_idx} with a map value {self.map_hist_peak_val}\n" + \
              f"Mean value of map  is {self.map_mean}\n" + \
              f"Variance of map  is {self.map_var}\n" + \
              f"Standard deviation of map  is {self.map_sigma}\n" + \
              f"Sum of background histogram is {self.bg_hist_sum}\n" + \
              f"Background / (Signal + Background) is {self.bg_frac}\n" + \
              f"Signal fraction is {1 - self.bg_frac}\n" + \
              f"Mean index of background histogram is {self.bg_mean_idx}\n" + \
              f"Variance (in index scale) of background histogram is {self.bg_var_idx}\n" + \
              f"Mean value of background in map value scale is {self.bg_mean}\n" + \
              f"Variance of background in map value scale is {self.bg_var}\n" + \
              f"Standard deviation of background is {np.sqrt(self.bg_var)}\n" + \
              f"Threshold of background histogram is {self.bg_threshold}\n"
        return str

def count_voxels_matching_criteria(map, threshold, cuboid_dims):
    """
    Count the number of voxels in the map that are within the dimensions
    of a centred cuboid and with map values above a threshold.

    :param map: Input map.
    :param threshold: Threshold to count voxels with.
    :param cuboid_dims: Only count voxels within a centred cuboid with
        these dimensions.
    :return: Count of voxels within the cuboid and with map values
        above a threshold.
    """
    map_centre = (np.asarray(np.shape(map)) - 1)/2
    half_width = np.asarray(cuboid_dims)/2

    def f(i, j, k):
        return (np.fabs(i - map_centre[0]) < half_width[0]
            and np.fabs(j - map_centre[1]) < half_width[1]
            and np.fabs(k - map_centre[2]) < half_width[2]
            and (map[int(i),int(j), int(k)] > threshold))

    fvec = np.vectorize(f)
    y = np.fromfunction(fvec, np.shape(map))
    vox_count = np.count_nonzero(y)
    return vox_count

def threshold_map(map_grid):
    """
    Determine a threshold level for the map which is suitable for
    visualisation. A two-step procedure is used. First the background
    sigma in the map is estimated and a threshold is calculated based
    on this. The map is thresholded and then orthogonal line projection
    profiles are calculated. A second threshold is calculated based on
    the width of these profiles. These two values are averaged to a
    final value.
    Note: This algorithm exploits the characteristics of cryoEM maps
        and may not work on synthetic maps.

    :param map_grid: Input map.
    :return: A tuple with the thresholded map, the threshold level,
        the histogram object and the line profile object.
    """

    # Calculate the log histogram and estimate the background level
    # from it.
    sigma_factor = 3
    hist = MapHistogram(map_grid, sigma_factor=sigma_factor, log_histogram=True)
    logger.debug("Histgram of input map")
    logger.debug(hist)

    # Set values below background_threshold to 0 in data
    map_grid1 = np.where(map_grid >= hist.bg_threshold, map_grid - hist.bg_threshold, 0)

    # 1D profiles along each axis
    prof = MapLineProjections(map_grid1)
    logger.debug(prof)

    # Fraction of box size
    box_fraction = count_voxels_matching_criteria(map_grid1, threshold=0, cuboid_dims=prof.cum_prof_width) / np.prod(np.asarray(map_grid1.shape))
    logger.debug(f"Fraction of box taken up by structure: {box_fraction}")

    # Find threshold value from cumulative distribution function of non-logged histogram of original map.
    hist_nolog = MapHistogram(map_grid, sigma_factor=sigma_factor, log_histogram=False)
    idx = np.searchsorted(hist_nolog.cum_dist_func, 1 - box_fraction)
    threshold_vol = hist_nolog.bins[idx] + 0.5 * hist_nolog.bin_width
    logger.debug(f"Threshold from volume estimation: {threshold_vol}")

    # Take the average of the two thresholds
    threshold_av = 0.5 * (hist.bg_threshold + threshold_vol)
    map_grid2 = np.where(map_grid >= threshold_av, map_grid - threshold_av, 0)
    logger.debug(f"Final threshold (average): {threshold_av}")

    return map_grid2, threshold_av

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Threshold map.')
    parser.add_argument('infile', metavar='FILE', type=str, help="Input map.")
    parser.add_argument('outfile', metavar='FILE', type=str, help="Thresholded map.")
    parser.add_argument('-p', '--plot', action='store_true', help="Plot histogram and line profiles.")
    args = parser.parse_args()

    with mrcfile.open(args.infile) as mrc:
        map_grid1, threshold, hist, prof = threshold_map(mrc.data)
        print(hist)
        print(f"Map threshold is {threshold}")
        if args.plot:
            prof.plot()
            fig1, ax1 = hist.plot_map_histogram()
            fig2, ax2 = hist.plot_map_cdf()
            fig3, ax3 = hist.plot_bg_histogram()
            plt.show()
        save_map(args.outfile, map_grid1, mrc)