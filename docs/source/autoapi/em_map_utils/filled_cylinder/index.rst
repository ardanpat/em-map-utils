em_map_utils.filled_cylinder
============================

.. py:module:: em_map_utils.filled_cylinder

.. autoapi-nested-parse::

   filled_cylinder.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 28/07/2025
   :Description:
       Generate a 3D volume containing a filled cylinder.




Attributes
----------

.. autoapisummary::

   em_map_utils.filled_cylinder.parser


Functions
---------

.. autoapisummary::

   em_map_utils.filled_cylinder.filled_cylinder


Module Contents
---------------

.. py:function:: filled_cylinder(diameter=50, length=100, box_size=(100, 100, 100), inside_value=1.0, outside_value=0.0, cent_coos=None, alignment_axis='i', dtype=np.float32)

   Generate a 3D volume containing a filled cylinder.

   Note: Coordinate system is (i,j,k) going from the slowest to fastest
       varying axis.

   :param diameter: Diameter of cylinder in voxels.
   :param length: Length of cylinder in voxels.
   :param box_size: Lengths of the sides of the 3D volume along the
       (i,j,k) axes.
   :param inside_value: Map value inside and on the cylinder.
   :param outside_value: Map value outside the cylinder.
   :param cent_coos: Centre (i,j,k) coordinates of the cylinder.
   :param alignment_axis: Long axis ('i', 'j' or 'k') of cylinder.
   :param dtype: Data type of 3D volume. Note: it cannot be
       float64 for the current MRC format.
   :return: 3D numpy grid with filled cylinder.


.. py:data:: parser

