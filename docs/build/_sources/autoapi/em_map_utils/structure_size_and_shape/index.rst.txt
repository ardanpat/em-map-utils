em_map_utils.structure_size_and_shape
=====================================

.. py:module:: em_map_utils.structure_size_and_shape

.. autoapi-nested-parse::

   structure_size_and_shape.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 07/08/2025
   :Description:
       Threshold and align map with a box by determining the principal axes
       of the structure and then aligning the principal axes to the box.
       Estimate the size of the molecule using the lengths of the 3
       orthogonal line projections. Estimate the asphericity of the
       structure as a shape measure.




Attributes
----------

.. autoapisummary::

   em_map_utils.structure_size_and_shape.logger
   em_map_utils.structure_size_and_shape.map_name_pattern


Functions
---------

.. autoapisummary::

   em_map_utils.structure_size_and_shape.read_map_list_from
   em_map_utils.structure_size_and_shape.asphericity_coefficient
   em_map_utils.structure_size_and_shape.structure_size_and_shape
   em_map_utils.structure_size_and_shape.main


Module Contents
---------------

.. py:data:: logger

.. py:data:: map_name_pattern

.. py:function:: read_map_list_from(list_file, list_dir=None, file_dir=None)

.. py:function:: asphericity_coefficient(a, b, c)

   Calculate the asphericity coefficient using three orthogonal width
   measures for a structure.
   Tha asphericity coefficient is defined as:
   1 - [ (V/S) / (V0/S0) ]
   where:
   S0 and V0 are the surface area and volume of a sphere with the
   cube root diameter = (abc)^(1/3),
   V is the volume of an ellipsoid with the axes a,b,c,
   S is the surface area of the ellipsoid with axes a,b,c calculated
   using the Carlson symmetric elliptical integral.
   What this formula is based on is that the surface area to volume
   ratio is at a minimum for a sphere compared to any ellipsoid with an
   equivalent volume and the comparison between the ratios increases
   the more the ellipsoid deviated from a sphere.

   :param a: Width along first axis.
   :param b: Width along second axis.
   :param c: Width along third axis.
   :return: Asphericity coefficient.


.. py:function:: structure_size_and_shape(entry_file, aligned_file=None, plot_profile=True, csv_file=None, csv_mode='a')

   Determine the size and shape of  a structure.

   :param entry_file: Name of input MRC file.
   :param aligned_file: Optional name of aligned output MRC file.
   :param plot_profile: Boolean for plotting line projections.
   :param csv_file: Optional name of CSV file to output results to.
   :param csv_mode: Whether to (a)ppend or (w) to CSV file.
   :return: Tuple with physical widths of structure along the principal
       axes, the cube root of these widths (which represents a sphere
       equivalent average), and the asphericity.


.. py:function:: main()

