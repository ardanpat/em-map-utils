em_map_utils.map_threshold
==========================

.. py:module:: em_map_utils.map_threshold

.. autoapi-nested-parse::

   map_threshold.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 05/08/2025
   :Description:
       Threshold map.




Attributes
----------

.. autoapisummary::

   em_map_utils.map_threshold.logger
   em_map_utils.map_threshold.parser


Classes
-------


.. list-table:: Classes
   :header-rows: 0
   :widths: auto
   :class: summarytable


   * - :py:obj:`MapHistogram <em_map_utils.map_threshold.MapHistogram>`
     - Class to represent the map histogram, the related cumulative




Functions
---------

.. autoapisummary::

   em_map_utils.map_threshold.threshold_map


Module Contents
---------------

.. py:data:: logger

.. py:class:: MapHistogram(map_grid, histogram_bins=5000, sigma_factor=3.0)

   Class to represent the map histogram, the related cumulative
   distribution function and histogram of the background (noise) in a
   map.


   .. py:method:: plot_map_histogram()

      Plot the map histogram.

      :return: A tuple with the figure and axes objects.



   .. py:method:: plot_map_cdf()

      Plot the map cumulative distribution function.

      :return: A tuple with the figure and axes objects.



   .. py:method:: plot_bg_histogram()

      Plots the background histogram.

      :return: A tuple with the figure and axes objects.



   .. py:attribute:: sigma_factor
      :value: 3.0



   .. py:attribute:: bin_width


   .. py:attribute:: cum_dist_func


   .. py:attribute:: map_hist_max_idx


   .. py:attribute:: map_hist_max_val


   .. py:attribute:: map_mean


   .. py:attribute:: map_var


   .. py:attribute:: map_sigma


   .. py:attribute:: bg_hist_sum


   .. py:attribute:: bg_frac


   .. py:attribute:: bg_mean_idx


   .. py:attribute:: bg_var_idx


   .. py:attribute:: bg_mean


   .. py:attribute:: bg_var


   .. py:attribute:: bg_sigma


   .. py:attribute:: bg_threshold


.. py:function:: threshold_map(map_grid)

   Determine a threshold level for the map which is suitable for
   visualisation. A two-step procedure is used. First the background
   sigma in the map is estimated and a threshold is calculated based
   on this. The map is thresholded and then orthogonal line projection
   profiles are calculated. A second threshold is calculated based on
   the width of these profiles. The threshold ultimately selected is
   higher of the two values.
   Note: This algorithm exploits the characteristics of cryoEM maps
       and may not work on synthetic maps.

   :param map_grid: Input map.
   :return: A tuple with the thresholded map, the threshold level,
       the histogram object and the line profile object.


.. py:data:: parser

