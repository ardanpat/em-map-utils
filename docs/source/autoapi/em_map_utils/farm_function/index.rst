em_map_utils.farm_function
==========================

.. py:module:: em_map_utils.farm_function

.. autoapi-nested-parse::

   farm_function.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 25/08/2025
   :Description:
       Run multiple processes of the same function, changing one parameter
       and collecting any results in a JSON file.




Attributes
----------

.. autoapisummary::

   em_map_utils.farm_function.logger


Classes
-------


.. list-table:: Classes
   :header-rows: 0
   :widths: auto
   :class: summarytable


   * - :py:obj:`FarmFunction <em_map_utils.farm_function.FarmFunction>`
     - Run multiple processes of a function f(v, args, kwargs), mapping




Module Contents
---------------

.. py:data:: logger

.. py:class:: FarmFunction(f, values, args=[], kwargs={}, num_workers=2, max_tries=2, monitoring_interval=5, file_root='dummy', resume=False, retry=False)

   Run multiple processes of a function f(v, args, kwargs), mapping
   v over a list of values and collecting the results in a JSON file.

   In contrast with the Pool function of multiprocessing, this class
   can attempt multiple tries of the function before giving up.


   .. py:attribute:: max_cpu


   .. py:attribute:: f


   .. py:attribute:: values


   .. py:attribute:: args
      :value: []



   .. py:attribute:: kwargs


   .. py:attribute:: num_workers


   .. py:attribute:: max_tries
      :value: 2



   .. py:attribute:: monitoring_interval
      :value: 5



   .. py:attribute:: file_root
      :value: 'dummy'



   .. py:attribute:: db_name
      :value: 'dummy.db'



   .. py:attribute:: output_file
      :value: 'dummy.json'



   .. py:attribute:: resume
      :value: False



   .. py:attribute:: retry
      :value: False



   .. py:attribute:: process_queue


   .. py:attribute:: success_queue


   .. py:attribute:: fail_queue


   .. py:attribute:: num_processed


   .. py:attribute:: num_error


   .. py:attribute:: num_success


   .. py:attribute:: old_values
      :value: []



   .. py:attribute:: lock


   .. py:method:: dict_factory(cursor, row)
      :staticmethod:


      Format rows as a dictionary for SQLite output.

      If the column result is present, it is assumed to be a json
      dump and loaded back into a dictionary.

      :param cursor: Database cursor.
      :param row: Database row tuple.
      :return: Formatted row dictionary.



   .. py:method:: write_to_files(con)

      Write success, failed, and processing tables to a file.

      :param con: Database connection.
      :return: No return value.



