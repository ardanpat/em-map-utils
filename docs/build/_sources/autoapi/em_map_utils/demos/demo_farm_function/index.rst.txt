em_map_utils.demos.demo_farm_function
=====================================

.. py:module:: em_map_utils.demos.demo_farm_function

.. autoapi-nested-parse::

   demo_farm_function.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 25/08/2025
   :Description:
       Demo usage of farm function using a dummy function that can fail 50
       percent of the time.




Attributes
----------

.. autoapisummary::

   em_map_utils.demos.demo_farm_function.parser


Functions
---------

.. autoapisummary::

   em_map_utils.demos.demo_farm_function.dummy


Module Contents
---------------

.. py:function:: dummy(x, y, z)

   Dummy function that fails 50% of the time randomly.
   :param x: Not used. Included for testing purposes.
   :param y: Not used. Included for testing purposes.
   :param z: Not used. Included for testing purposes.
   :return: Tuple (status, result_dict) where status is whether the
       function is successful or not, and result_dict is a dictionary
       containing the results of the function.


.. py:data:: parser

