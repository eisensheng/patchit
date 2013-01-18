Patchit
=======

.. image:: https://travis-ci.org/EisenSheng/patchit.png?branch=develop
    :target: https://travis-ci.org/EisenSheng/patchit
    :alt: ci build status

Patchit is an MIT Licensed unified diff parsing and merge tool written in
Python for anyone who needs a finer grain of control over unified diff
content and to merge the diff with an arbitrary stream of lines.


Motivation
----------

The motivation for this package arose from the

- overwhelming complexity of other patching tools written in Python,
- their absence from the PyPI,
- their inability to inspect the unified diff content and
- missing support to merge the patch with an arbitrary stream of lines.


Installation
------------

To install patchit just run from the root of the project:

.. code-block:: bash

    $ python setup.py install


Testing
-------

Tests are located at the `tests.py` file. In order to test your new
contribution to patchit just run from your shell

.. code-block:: bash

    $ python setup.py test


Contribute
----------

Unfortunately, I wasn't able to make it much better myself. Therefore I'm
asking anyone who is interested in a patch functionality for Python to
improve this package and hand in patches by mail or pull requests.

The preferred method of development is a test driven approach and following
the nvie git flow branching model. Please be so kind to bear these things in
mind when handing in improvements. Thank you very much.
