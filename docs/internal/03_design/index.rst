Design
======

.. needpie::
   :labels: draft, in discussion, agreed, rejected, no status
   :legend:

   type == 'arch-swc' and status == 'draft'
   type == 'arch-swc' and status == 'in discussion'
   type == 'arch-swc' and status == 'agreed'
   type == 'arch-swc' and status == 'rejected'
   type == 'arch-swc' and (status != 'rejected') and (status != 'agreed') and (status != 'in discussion') and (status != 'draft')

List of Software Components:

.. needtable::
   :columns: id, title, status
   :filter: type == 'arch-swc'
   :sort: id



.. toctree::
    :maxdepth: 1
    :hidden:

    /src/moduleA/l1/uselessCmp/docs/detailed_design.rst
    /src/moduleA/l2/uselessL2Cmp/docs/detailed_design.rst
