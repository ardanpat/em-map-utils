em_map_utils.map_covariance
===========================

.. py:module:: em_map_utils.map_covariance

.. autoapi-nested-parse::

   map_covariance.py

   :Author: Ardan Patwardhan
   :Affiliation: EMBL-EBI, Wellcome Genome Campus, CB10 1SD, UK
   :Date: 31/07/2025
   :Description:
       Class for handling the covariance matrix of the map value
       distribution and related eigenvectors and eigenvalues.




Attributes
----------

.. autoapisummary::

   em_map_utils.map_covariance.logger
   em_map_utils.map_covariance.parser


Classes
-------


.. list-table:: Classes
   :header-rows: 0
   :widths: auto
   :class: summarytable


   * - :py:obj:`MapCovariance <em_map_utils.map_covariance.MapCovariance>`
     - \-




Module Contents
---------------

.. py:data:: logger

.. py:class:: MapCovariance(map_grid)

   .. py:attribute:: RHAS_XYZ


   .. py:attribute:: RHAS_ZYX


   .. py:attribute:: RHAS_BASE


   .. py:attribute:: RHAS_ALL


   .. py:method:: sign_align_eigenvectors(evecs1, evecs2)
      :staticmethod:


      Two eigenvector systems may be very similar but look very different due to the signs.
      Here we change the signs of evec2 to make it as similar to evec1 while keeping to a
      right-handed system. In order to maintain a right handed system, two vectors need to
      change sign.

      Note: Eigenvectors are specified in different columns, e.g evecs[:,0], evecs[:,1], evecs[:,2].

      :param evecs1: First set of eigenvectors
      :param evecs2: Second set of eigenvectors
      :return: Second set of eigenvectors where the signs of the eigenvectors have been adjusted



   .. py:method:: find_closest_rhas(vecs)
      :classmethod:


      Given a triplet of basis vectors, find the closest match right
      handed coordinate system.

      :param vecs: Triplet of vectors, one in each column.
      :return: Closest matching right-handed system with each column
          representing a basis vector.



   .. py:method:: align_map_principal_axes(map_grid, axes=None, cubify_if_needed=False, dtype=np.float32)
      :classmethod:


      Determine the principal axes that corresponds to a map grid and rotate the map
      so that the principal axes are aligned with the axes specified.
      Notes:
      1) The axis vectors in axes are in columns, e.g., axis 0 = axes[:,0], axis 1 = axes[:,1].
      2) The principal axis will be ordered by eigenvalue in descending order and the first axis
         will be aligned to axes[:,0]

      :param map_grid: Map grid to be aligned.
      :param axes: Axis vectors to use as a reference when aligning principal axes. If None, the closest right-handed system to the eigenvectors will be used.
      :param cubify_if_needed: If the map is non-cubic, pad it to the max dimension prior to any rotation.
      :param dtype: Data type of the output arrays.
      :return: Aligned map grid, applied rotation, eigenvalues, and eigenvectors.



   .. py:method:: map_rotate_forward_backward(map_grid, rotation, cubify_if_needed=False)
      :classmethod:


      Rotate map by the given rotation, estimate the rotation using
      the map's principal axes. Rotate the map back so that the map
      is once again aligned to the input map and then find the diff
      between the rotation matrices of the input and back-rotated map.
      This method is useful for testing purposes.

      :param map_grid: Input map.
      :param rotation: SciPy rotation to apply to input map.
      :param cubify_if_needed: If map is cubic, pad it to the max dimension prior to any rotation.
      :return: Tuple with rotated map, back-rotated map and back
          rotation.



   .. py:method:: phys_scale_eigenvectors(mrc)

      Using the voxel sizes from an MRC file to scale the eigen-
      vectors to Ångstroms. Note although the voxel size in the three
      dimensions is almost always the same in cryoEM, this routine
      takes into account that they may not be. However this feature
      has not been tested.

      :param mrc: MRC file with voxel sizes.
      :return: Vector with scalings for each of the eigenvectors.



   .. py:method:: lengths_from_eigenvalues(mrc)

      The eigenvalues are related to the extent of the map value
      distribution along the principal axes. This routine attempts
      to estimate the physical extents of the map value distribution
      using different estimates.

      :param mrc: MRC file contain voxel sizes.
      :return: Tuple with FWHM, two sigma and sphere diameter lengths.



   .. py:attribute:: centre_coos


   .. py:attribute:: cov_matrix


   .. py:attribute:: eigenvalues


   .. py:attribute:: eigenvectors


.. py:data:: parser

