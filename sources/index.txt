patchit
=======

.. automodule:: patchit

    .. autoexception:: PatchSyntaxError

    .. autoexception:: PatchConflictError

    .. autoclass:: Hunk

        .. automethod:: merge

        .. autoclass:: patchit::Hunk.Operation

            Describes a single instruction within a hunk.

            .. attribute:: symbol

                Specifies whenever the given text shall match, be deleted from
                or inserted into the given stream.

            .. attribute:: text

                Specifies the text to insert or match for equality or deletion

    .. autoclass:: Patch
        :members:

        .. attribute:: hunks

            Ordered collection of :class:`Hunk` instances.

        .. attribute:: source_filename

            Old file name

        .. attribute:: source_comment

            Comment relating old file name (i.e. last time of change)

        .. attribute:: target_filename

            New file name

        .. attribute:: target_comment

            Comment relating new file name (i.e. last time of change)

        .. attribute:: metadata

            VCS related metadata (like diff parameters or commit id)

    .. autoclass:: PatchSet
        :members:

        .. attribute:: patches

            Collection of :class:`Patch` instances.

    .. autoclass:: PatchSetReader
        :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

