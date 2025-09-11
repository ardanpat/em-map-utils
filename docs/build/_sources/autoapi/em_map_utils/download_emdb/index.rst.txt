em_map_utils.download_emdb
==========================

.. py:module:: em_map_utils.download_emdb

.. autoapi-nested-parse::

   download_emdb.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 26/08/2025
   :Description:
       Functions for downloading EMDB maps and other data from EMDB sites.




Attributes
----------

.. autoapisummary::

   em_map_utils.download_emdb.logger
   em_map_utils.download_emdb.emdbid_pattern
   em_map_utils.download_emdb.emdb_root


Functions
---------

.. autoapisummary::

   em_map_utils.download_emdb.read_emdb_ids_from
   em_map_utils.download_emdb.get_emdb_map_name
   em_map_utils.download_emdb.get_map_download_path
   em_map_utils.download_emdb.get_emdb_map_url
   em_map_utils.download_emdb.download_emdb_map
   em_map_utils.download_emdb.main


Module Contents
---------------

.. py:data:: logger

.. py:data:: emdbid_pattern

.. py:data:: emdb_root

.. py:function:: read_emdb_ids_from(filename)

   Read EMDB ids from file.

   Each line is expected to have one EMDB ID and no other characters.

   :param filename: Name of file to read.
   :return: List of EMDB IDs.


.. py:function:: get_emdb_map_name(emdb_id)

   Get EMDB map name from EMDB ID.

   Maps are named as emd_XXX.map.gz, where XXX is 4 - 6 digits.

   :param emdb_id: EMDB ID string.
   :return: Map name.


.. py:function:: get_map_download_path(download_dir, emdb_id)

   Create full path to where EMDB map will be downloaded.

   :param download_dir: Download directory.
   :param emdb_id: EMDB ID string.
   :return: Map download path.


.. py:function:: get_emdb_map_url(emdb_id, loc='EBI')

   Get EMDB map URL from EMDB ID and EMDB location.

   :param emdb_id: EMDB ID string.
   :param loc: One of the 3 sites from the emdb_root dictionary.
   :return: EMDB map URL.


.. py:function:: download_emdb_map(emdb_id, download_dir, loc='EBI', resume=True, chunk_size=2**16)

   Download EMDB map from EMDB ID and EMDB location.

   :param emdb_id: EMDB ID of map to be downloaded.
   :param download_dir: Directory to download to.
   :param loc: EMDB location to download from.
   :param resume: If TRUE and the map has been partially downloaded,
       continue from where it left off.
   :param chunk_size: Chunk size of requests used during download.
   :return: True if the download was successful.


.. py:function:: main()

   Download EMDB map or a list of maps from a EMDB site.

   If a list of files is provided, then multiprocessing is used to
   download EMDB maps.
   :return:


