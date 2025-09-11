em_map_utils.demos.demo_map_rotate
==================================

.. py:module:: em_map_utils.demos.demo_map_rotate

.. autoapi-nested-parse::

   demo_map_rotate.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 31/07/2025
   :Description:
       Rotate a simple map and show the orthogonal surface views.




Attributes
----------

.. autoapisummary::

   em_map_utils.demos.demo_map_rotate.parser


Functions
---------

.. autoapisummary::

   em_map_utils.demos.demo_map_rotate.plot_rotated_map


Module Contents
---------------

.. py:function:: plot_rotated_map(in_file, lengths, box_size, rotation, translation, cubify, out_file)

   Rotate a cuboid (or an optionally specified map) and show the
   orthogonal surface views.

   :param in_file: Optional input file - if none is provided a cuboid
       is used as the input.
   :param lengths: Lengths of the cuboid.
   :param box_size: Size of the 3D volume box.
   :param rotation: Euler angle of rotation in an intrinsic frame following Z-Y'-Z" convention.
   :param translation: An initial translation vector.
   :param cubify: If a map is not cubic, pad it to the largest dimension.
   :param out_file: Optional file to save the figure to.
   :return: No return value.


.. py:data:: parser

