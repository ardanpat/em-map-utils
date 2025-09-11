em_map_utils.filled_cuboid
==========================

.. py:module:: em_map_utils.filled_cuboid

.. autoapi-nested-parse::

   filled_cuboid.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 28/07/2025
   :Description:
        Generate a 3D volume containing a filled cuboid.




Attributes
----------

.. autoapisummary::

   em_map_utils.filled_cuboid.parser


Functions
---------

.. autoapisummary::

   em_map_utils.filled_cuboid.filled_cuboid


Module Contents
---------------

.. py:function:: filled_cuboid(lengths=(80, 50, 20), box_size=(100, 100, 100), inside_value=1.0, outside_value=0.0, cent_coos=None, dtype=np.float32)

   Generate a cuboid of given lengths.

   Note: Coordinate system is (i,j,k) going from the slowest to fastest
       varying axis.

   :param lengths: Tuple/list/array of cuboid lengths aligned to box
       axes.
   :param box_size: Tuple/list/array of box dimensions.
   :param inside_value: Voxel value inside and on cuboid.
   :param outside_value: Voxel value outside cuboid.
   :param cent_coos: Centre coordinates of cuboid as tuple/list or
       array. If None, the centre of the box is used.
   :param dtype: Data type of 3D volume. Note: it cannot be
       float64 for the current MRC format.
   :return: 3D numpy grid with a cuboid.


.. py:data:: parser

