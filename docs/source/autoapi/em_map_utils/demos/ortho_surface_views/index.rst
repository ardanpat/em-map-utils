em_map_utils.demos.ortho_surface_views
======================================

.. py:module:: em_map_utils.demos.ortho_surface_views

.. autoapi-nested-parse::

   ortho_surface_views.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 30/07/2025
   :Description:
       Plot orthogonal surface views in the i, j and k directions of a
       3D numpy grid.




Functions
---------

.. autoapisummary::

   em_map_utils.demos.ortho_surface_views.ortho_surface_views


Module Contents
---------------

.. py:function:: ortho_surface_views(map_grid, fig_title=None, color_map='YlOrRd', fig_size=(18, 6))

   Plot orthogonal surface views in the i, j and k directions of a
   3D numpy grid.


   :param map_grid: 3D numpy grid.
   :param fig_title: Title for the overall figure. Default is None.
   :param color_map: Color map of the figure. Default is "YlOrRd".
   :param fig_size: Size of the figure. Default is (7, 21)
   :return: figure object and subplot objects as tuple (fig, ax).


