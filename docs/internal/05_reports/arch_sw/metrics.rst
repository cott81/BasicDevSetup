Software Architecture Metrics
=================================================================================================================

Summary
-----------------------------------------------------------------------------------------------------------------

| All SW Req       : :need_count:`(type=='req-sw') and 'devsuite' not in tags`
| All SW Arch Elements     : :need_count:`(type=='arch-composite' or type=='arch-swc')`
| Software Composites      : :need_count:`(type=='arch-composite')`
| Software Components      : :need_count:`(type=='arch-swc')`

Metrics
-----------------------------------------------------------------------------------------------------------------

.. needpie:: SW Components --> SW Requirements Linkage Status
    :labels: Linked,  Not Linked
    :explode: 0, 0.1
    :colors: #278d3e, #b2253b
    :text_color: w
    :legend:

    (type=='arch-swc') and (not(specified_by is None or len(specified_by)==0))
    (type=='arch-swc') and (   (specified_by is None or len(specified_by)==0))

.. needpie:: SW Components --> Implementation Linkage Status
    :labels: Linked,  Not Linked
    :explode: 0, 0.1
    :colors: #278d3e, #b2253b
    :text_color: w
    :legend:

    (type=='arch-swc') and (not(specified_by_back is None or len(specified_by_back)==0))
    (type=='arch-swc') and (   (specified_by_back is None or len(specified_by_back)==0))


Traceability Summary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: arch-swc
   :columns: id, specified_by, status
   :colwidths: 5, 5, 5
   :filter: (is_need)
   :style: datatables

SW Requirements not linked to SW Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req-sw
   :columns: id, status
   :colwidths: 5, 5
   :filter: (specified_by_back is None or len(specified_by_back)==0)
   :style: datatables

SW Components not linked to SW Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: arch-swc
   :columns: id, status
   :colwidths: 5, 5
   :filter: (specified_by is None or len(specified_by)==0)
   :style: datatables
