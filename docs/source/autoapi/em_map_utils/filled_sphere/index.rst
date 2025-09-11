em_map_utils.filled_sphere
==========================

.. py:module:: em_map_utils.filled_sphere

.. autoapi-nested-parse::

   filled_sphere.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 28/07/2025
   :Description:
       Generate a 3D volume of filled sphere.




Attributes
----------

.. autoapisummary::

   em_map_utils.filled_sphere.parser


Functions
---------

.. autoapisummary::

   em_map_utils.filled_sphere.filled_sphere


Module Contents
---------------

.. py:function:: filled_sphere(diameter=50, box_size=(100, 100, 100), inside_value=1.0, outside_value=0.0, cent_coos=None, dtype=np.float32)

   Generate a 3D volume containing a filled sphere.

   Note: Coordinate system is (i,j,k) going from the slowest to fastest
       varying axis.

   :param diameter: Diameter of the filled sphere in voxels.
   :param box_size: Lengths of the sides of the 3D volume along the
       (i,j,k) axes.
   :param inside_value: Map value inside and on the filled sphere.
   :param outside_value: Map value outside the filled sphere.
   :param cent_coos: Centre (i,j,k) coordinates of the filled sphere.
       If none are specified, the centre of the box is used.
   :param dtype: Data type of 3D volume. Note: it cannot be
       float64 for the current MRC format.
   :return: 3D numpy grid with filled sphere.


.. py:data:: parser

