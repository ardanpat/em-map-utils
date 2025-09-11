em_map_utils.map_rotate
=======================

.. py:module:: em_map_utils.map_rotate

.. autoapi-nested-parse::

   map_rotate.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 30/07/2025
   :Description:
       Rotate map.




Attributes
----------

.. autoapisummary::

   em_map_utils.map_rotate.parser


Functions
---------

.. autoapisummary::

   em_map_utils.map_rotate.map_rotate


Module Contents
---------------

.. py:function:: map_rotate(map_grid, rotation, rotation_centre=None, initial_translation=None, cubify_if_needed=False, interpolation_order=5, fill_value=0, dtype=np.float32)

   Rotate map.

   :param map_grid: Map to rotate.
   :param rotation: Rotation specified as a SciPy rotation object.
   :param rotation_centre: Centre of rotation, taken as the centre of the box if not specified.
   :param initial_translation: A translation that can be applied to the map prior to rotation.
   :param interpolation_order: Spline interpolation order.
   :param cubify_if_needed: If the map box is non-cubic, add padding
       and make it cubic to the largest dimension before rotating the
       map.
   :param fill_value: Value to use when interpolation points lie outside the box.
   :param dtype: Data type of returned map
   :return: Rotated map.


.. py:data:: parser

