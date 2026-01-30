#########################
Documentation Guidelines
#########################

This page provides some basic guidelines to be followed while creating documentation using reStructuredText.
This guide helps bring consistency to your documents that will maximize efficiency, improve readability and minimize maintenance.

For detailed reStructuredText help, see `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.

Markdown is also allowed. The supported Markdown flavor is `MyST <https://mystmd.org/guide/quickstart-myst-markdown>`_.

File and folder names
=====================

- Use only lowercase alphanumeric characters and `_` (underscore) as connector. This is called `snake_case <https://en.wikipedia.org/wiki/Snake_case>`_
- Do not use numbering for files or folders as prefix for sorting. (except for the templated ones).

Usage of whitespace
===================

All rST files use an indentation of 3 spaces; no tabs are allowed.

The indentation is used, for example.

.. code-block:: rst

   .. req-sw::
      :id: REQ_SW_001
      :status: draft

      The system shall do something.

``:id:`` and ``status`` within ``.. req-sw::`` above is indented with 3 spaces.

.. _internal/90_process/doc_guidelines:page_labels:

Page labels
===========

You can reference sections within a document using labels.

A label is created by placing the following code before a section header:

.. code-block:: rst

   .. _label_name:


The label must be unique in the entire documentation. Therefore the following format is recommended: ``doc_path:name``

Where ``doc_path`` is the path to the document from the documentation root (without the file extension) and ``name`` is a unique name for the section.

To reference a section with a label, use the following syntax:

.. code-block:: rst

   :ref:`label_name`

Example:

   This section has the label: ``internal/90_process/doc_guidelines:page_labels``, so it can be referenced as:

   ``:ref:`internal/90_process/doc_guidelines:page_labels``

   with the following result: :ref:`internal/90_process/doc_guidelines:page_labels`.

.. note::

   ``internal/*`` must never be referenced in the external documentation, as they will not be available.

   ``external/*`` can be referenced in the internal documentation, since both are built together.



Section headers
===============

Any alphanumeric character can be used as over- and underlining.
Normally, there are no heading levels assigned to certain characters as the structure is determined from the succession of headings.
However, here is a suggested convention:

* ``#`` with under and overline for H1, e.g., parts
* ``=`` for H2, e.g., chapters
* ``-`` for H3, e.g., sections
* ``~`` for H4, e.g., subsections
* ``^`` for H5, e.g., subsubsections
* ``'`` for H6, e.g., paragraphs

A full example would be:

.. code-block:: rst

    ##########
    Sample H1
    ##########

    Sample content for H1.

    Sample H2
    =========

    Sample content for H2.

    Sample H3
    ---------

    Sample content for H3.

    Sample H4
    ~~~~~~~~~

    Sample content for H4.

    Sample H5
    ^^^^^^^^^

    Sample content for H5.

    Sample H6
    '''''''''

    Sample content for H6.

.. tip::

    If you need more than heading level 4 (i.e. H5 or H6), then you should consider
    creating a new document.

.. hint:: There should be only one H1 in a document.

Images
======

It is recommended to use PNG for bitmaps (e.g. screenshots) and SVG for vector graphics images.
When making screenshots, try to crop out unnecessary content (browser window, desktop, etc).
Mask out personal details like username etc.
Avoid scaling the images, as the Sphinx theme automatically resizes large images.

For self-created diagrams use ``drawio`` editor in Visual Studio Code, saved as SVG (.drawio.svg).

Store images within a folder named ``images`` parallel to where the reST file is present.
For example,:

| help
| ├── images
| │   ├── image.svg
| │   ├── image.png
| └── myfile.rst

Linking
========

Links to other pages should never be titled as "here".
Sphinx makes this easy by automatically inserting the title of the linked document.

To insert a link to an external website::

   `Text of the link <http://example.com>`__

The resulting link would look like this: `Text of the link <http://example.com>`__

.. warning:: It is very easy to have two links with the same text resulting in the following error::

   **(WARNING/2) Duplicate explicit target name:foo**

   To avoid these warnings use of a double `__` generates an anonymous link.
