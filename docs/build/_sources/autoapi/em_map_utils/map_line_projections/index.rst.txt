em_map_utils.map_line_projections
=================================

.. py:module:: em_map_utils.map_line_projections

.. autoapi-nested-parse::

   map_line_projections.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 04/08/2025
   :Description:
       Create orthogonal line projections from a map.




Attributes
----------

.. autoapisummary::

   em_map_utils.map_line_projections.logger
   em_map_utils.map_line_projections.parser


Classes
-------


.. list-table:: Classes
   :header-rows: 0
   :widths: auto
   :class: summarytable


   * - :py:obj:`MapLineProjections <em_map_utils.map_line_projections.MapLineProjections>`
     - Class to create orthogonal line projections from a map.




Module Contents
---------------

.. py:data:: logger

.. py:class:: MapLineProjections(map_grid)

   Class to create orthogonal line projections from a map.


   .. py:attribute:: PERM_IDX


   .. py:method:: fit_exp4_func(x, a, b, c, d)
      :staticmethod:


      Fitting function y = a * exp(-b * (x - c)^4) + d
      :param x: x value for calculation of fitting function.
      :param a: Scale factor.
      :param b: Scaling of exponential.
      :param c: Centre x of exponential.
      :param d: Baseline offset of exponential.
      :return: Function evaluated at x.



   .. py:method:: fit_exp4()

      Fit fit_exp4_func to the 3 line projections.
      :return: Fitted profiles to the 3 line projections.



   .. py:method:: cumulative_profile_width(threshold=0.005)

      Determine the cumulative profile of each of the 3 line proj-
      ections. Then determine the indices where the profile crosses
      T and 1 -T where T is some threshold value. The width is then
      taken as the difference between these indices.

      :param threshold: Threshold value for width calculation.
      :return: Array of 3 widths.



   .. py:method:: plot(fig_title=None, fig_size=(18, 6))

      Plot line projections and corresponding fitted curves.

      :param fig_title: Figure title.
      :param fig_size: Figure size.
      :return: Tuple of figure and axes objects..



   .. py:attribute:: map_grid


   .. py:attribute:: coords


   .. py:attribute:: map_prof


   .. py:attribute:: min


   .. py:attribute:: max


   .. py:attribute:: range


   .. py:attribute:: sum


   .. py:attribute:: cent_coords


   .. py:attribute:: variance


   .. py:attribute:: sigma


   .. py:attribute:: two_sigma


   .. py:attribute:: cum_prof_width


   .. py:attribute:: prof_fit
      :value: None



.. py:data:: parser

