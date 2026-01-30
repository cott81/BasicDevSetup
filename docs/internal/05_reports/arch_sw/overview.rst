Software Architecture Overview
================================

.. needflow::
   :config: lefttoright
   :show_link_names:
   :types: arch-composite, arch-swc

.. needtable:: Software Components (all)
    :types: arch-swc
    :columns: id, title, status, specified_by as "Requirements", specified_by_back as "Implementation"
    :filter: is_need
    :style: datatables

.. needtable:: Software Composites (all)
    :types: arch-composite
    :columns: id, title, status, part_of as "Parts"
    :filter: is_need
    :style: datatables
