'''
The PyUFGet module provides interfaces to search and download matrices from the
University of Florida Sparse Matrix Collection.

There are two ways to use PyUFGet:
* By importing the PyUFGet module in Python, or
* As a standalone command-line tool

To search for sparse matrices that match a given criterion, use `PyUFGet.search` ::

  PyUFGet.search(name_or_id, **kwargs)

`PyUFGet.search` only returns a list of `Matrix` objects that match the selection criterion. To download the matrices
themselves, use the `download` method in the `Matrix object` or use `PyUFGet.fetch` ::

  PyUFGet.fetch(name_or_id, format, location, **kwargs)

The rules for specifying the search criteria in `PyUFGet.search` and
 `PyUFGet.fetch` are as follows:

1. `name_or_id` can be either the numerical ID of the matrix such as
   `42` or a pattern such as `"HB/ash*"` or `"c-"`. This field is
   optional.
2. `**kwargs` is a set of key-value pairs containing one or more search constraints:
     - matid: An integer matrix ID such as `42`
     - group: The matrix group name such as `HB`
     - name: A pattern containing the matrix name such as `ash-`
     - rowbounds: A tuple of the form (min, max) containing the
       minimum and maximum rows. The min or max value can be set to
       `None`. 
     - colbounds: A tuple of the form (min, max) containing the minimum and maximum columns.
     - nzbounds: A tuple of the form (min, max) containing the minimum and maximum non-zero values.
     - dtype: The matrix data type, one of `real`, `complex` or `binary`.
     - is2d3d: If true, only selects matrices arising from 2D and 3D discretizations.
     - isspd: If true, only selects SPD matrices.
     - kind: A string describing the problem domain, see http://www.cise.ufl.edu/research/sparse/matrices/kind.html
     - limit: Number of matrices to return, defaults to 10.

If `name_or_id` is specified, it overrides any conflicting key-value settings in `**kwargs`.

`PyUFGet.search` returns a list of `Matrix` objects where each
`Matrix` instance simply contains the metadata about the matrix such
as the number of rows, the number of columns, datatype etc. To
download a `Matrix` object to disk, use `Matrix.download()`; to view
its location in the UFL website, use `Matrix.url()`.

In `PyUFGet.fetch`, `format` can be one of 'MM', 'MAT' or 'RB'; 'MM'
is the default if `format` is omitted.  Finally, `location` refers
to the directory where the matrices will be downloaded on the local
machine. It defaults to `%APPDATA%/PyUFGet` on Windows and
`~/.PyUFGet` on Unix-like platforms.

In addition to its usage as a Python library, PyUFGet can be run from
the command line as follows ::

  python PyUFGet
  Usage: PyUFGet [NameOrID] [options]

     NameOrID             A numerical matrix ID or a pattern matching the name of
                          the matrix.
  
  Options:
    -h, --help            show this help message and exit
    -i MATID, --id=MATID  Download a matrix with the given ID.
    -g GROUP, --group=GROUP
                          The matrix group.
    -n NAME, --name=NAME  The name or a pattern matching the name of the
                          matrix/matrices.
    -d DTYPE, --data-type=DTYPE
                          The element type of the matrix/matrices, can be one of
                          'real', 'complex' or 'binary'.
    -s, --spd             Only selects SPD matrices.
    -f FORMAT, --format=FORMAT
                          The format in which to download the matrix/matrices.
                          Can be one of 'MM', 'MAT' or 'RB' for MatrixMarket,
                          MATLAB or Rutherford-Boeing formats respectively.
                          Defaults to 'MM'.
    -l LIMIT, --limit=LIMIT
                          The maximum number of matrices to be downloaded.
                          Defaults to 10.
    -o LOCATION, --outdir=LOCATION
                          The directory in the local machine where matrices will
                          be downloaded to. Defaults to
                          C:\Users\PappuHari\AppData\Roaming\PyUFGet
  
    Size and Non-zero filters:
      These options may be used to restrict the shape or number of non-zero
      elements of the matrices to be downloaded
  
      --min-rows=MIN_ROWS
                          The minimum number of rows in the matrix/matrices.
      --max-rows=MAX_ROWS
                          The maximum number of rows in the matrix/matrices.
      --min-cols=MIN_COLS
                          The minimum number of columns in the matrix/matrices.
      --max-cols=MAX_COLS
                          The maximum number of columns in the matrix/matrices.
      --min-nnzs=MIN_NNZS
                          The minimum number of non-zero values in the
                          matrix/matrices.
      --max-nnzs=MAX_NNZS
                          The maximum number of non-zero values in the
                          matrix/matrices.
'''
from query import search, fetch, cli
__all__ = ["query"]
