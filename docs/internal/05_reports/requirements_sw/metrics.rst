SW Requirements Metrics
=================================================================================================================

Summary
-----------------------------------------------------------------------------------------------------------------

| All:                                  :need_count:`type in ['req-sw']`
| Relevant:                             :need_count:`type in ['req-sw'] and status not in ['n/a', 'obsolete', 'rejected']`
| Non-relevant (obsolete|rejected|n/a): :need_count:`type in ['req-sw'] and status     in ['n/a', 'obsolete', 'rejected']`


Metrics
-----------------------------------------------------------------------------------------------------------------

.. needpie:: SW Requirement Status (all)
    :labels: Accepted, Draft, Obsolete, Rejected
    :explode: 0.1, 0.1, 0.1, 0.1
    :colors: #278d3e, #06abd2, #2c3075, #5a3b8e
    :text_color: w
    :legend:

    type in ['req-sw'] and status == 'accepted'
    type in ['req-sw'] and status == 'draft'
    type in ['req-sw'] and status == 'obsolete'
    type in ['req-sw'] and status == 'rejected'

.. needpie:: SW Requirements --> System requirements Linkage Status
    :labels: Linked,  Not Linked
    :explode: 0, 0.1
    :colors: #278d3e, #b2253b
    :text_color: w
    :legend:

    (type=='req-sw') and (not(satisfies is None or len(satisfies)==0))
    (type=='req-sw') and (   (satisfies is None or len(satisfies)==0))

.. needpie:: SW Requirements --> Implementation Linkage Status
    :labels: Linked,  Not Linked
    :explode: 0, 0.1
    :colors: #278d3e, #b2253b
    :text_color: w
    :legend:

    (type=='req-sw') and (not(implements_back is None or len(implements_back)==0))
    (type=='req-sw') and (   (implements_back is None or len(implements_back)==0))

.. needpie:: SW Requirements --> Test case Linkage Status
    :labels: Linked,  Not Linked
    :explode: 0, 0.1
    :colors: #278d3e, #b2253b
    :text_color: w
    :legend:

    (type=='req-sw') and (not(verify_back is None or len(verify_back)==0))
    (type=='req-sw') and (   (verify_back is None or len(verify_back)==0))

SW Requirements not linked to System Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req-sw
   :columns: id, status
   :colwidths: 5, 5
   :filter: (satisfies is None or len(satisfies)==0)
   :style: datatables

SW Requirements not linked to Architectural Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req-sw
   :columns: id, status
   :colwidths: 5, 5
   :filter: (specified_by_back is None or len(specified_by_back)==0)
   :style: datatables

SW Requirements not linked to Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req-sw
   :columns: id, status
   :colwidths: 5, 5
   :filter: (implements_back is None or len(implements_back)==0)
   :style: datatables

SW Requirements not linked to Test Case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req-sw
   :columns: id, status
   :colwidths: 5, 5
   :filter: (verify_back is None or len(verify_back)==0)
   :style: datatables
