em_map_utils.demos.demo_map_covariance
======================================

.. py:module:: em_map_utils.demos.demo_map_covariance

.. autoapi-nested-parse::

   demo_map_covariance.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 04/08/2025
   :Description:
       Demonstrate the use of estimating map principal axes.
       A cuboid is first rotated by a known angle. The principal axes of
       the rotated map are used to estimate the back rotation of the map
       which is then applied to the map. Orthogonal surface views of the
       initial cuboid and the back-rotated cuboid are plotted and can be
       compared. They should be the same unless something has gone wrong
       with either the map rotation or the principal axes determination.




Attributes
----------

.. autoapisummary::

   em_map_utils.demos.demo_map_covariance.logger
   em_map_utils.demos.demo_map_covariance.parser


Functions
---------

.. autoapisummary::

   em_map_utils.demos.demo_map_covariance.plot_back_rotated_cuboid


Module Contents
---------------

.. py:data:: logger

.. py:function:: plot_back_rotated_cuboid(in_file, lengths, box_size, rotation, cubify, out_file)

   A cuboid (or an optionally specified input map) is first rotated
   by a known angle. The principal axes of the rotated map are used to
   estimate the back rotation of the map which is then applied to the
   map. Orthogonal surface views of the initial map and the
   back-rotated map are plotted and can be compared.

   :param in_file: Path to the optional input map or None.
   :param lengths: Lengths of the cuboid.
   :param box_size: Size of the 3D volume box.
   :param rotation: Euler angle of rotation in an intrinsic frame following Z-Y'-Z" convention.
   :param cubify: If the map is not cubic, pad it to the largest dimension before rotation operations.
   :param out_file: Optional file to save the figure to.
   :return: No return value.


.. py:data:: parser

