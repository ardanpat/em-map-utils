em_map_utils.util
=================

.. py:module:: em_map_utils.util

.. autoapi-nested-parse::

   util.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 31/07/2025
   :Description:
       Utility functions used by various modules.




Functions
---------

.. autoapisummary::

   em_map_utils.util.save_map


Module Contents
---------------

.. py:function:: save_map(outfile, map_grid, mrc)

   Save grid as a mrc file copying key header values from an existing
   mrc file.

   :param outfile: Name of file to save map to.
   :param map_grid: Map grid to save.
   :param mrc: MRC file with header information to copy.
   :return: No return value.


