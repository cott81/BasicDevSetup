System Requirements Metrics
=================================================================================================================

Summary
-----------------------------------------------------------------------------------------------------------------

| All:                                  :need_count:`type in ['req-sys']`
| Relevant:                             :need_count:`type in ['req-sys'] and status not in ['n/a', 'obsolete', 'rejected']`
| Non-relevant (obsolete|rejected|n/a): :need_count:`type in ['req-sys'] and status     in ['n/a', 'obsolete', 'rejected']`


Metrics
-----------------------------------------------------------------------------------------------------------------

.. needpie:: Requirement Status (all)
    :labels: Accepted, Draft, Obsolete, Rejected
    :explode: 0.1, 0.1, 0.1, 0.1
    :colors: #278d3e, #06abd2, #2c3075, #5a3b8e
    :text_color: w
    :legend:

    type in ['req-sys'] and status == 'accepted'
    type in ['req-sys'] and status == 'draft'
    type in ['req-sys'] and status == 'obsolete'
    type in ['req-sys'] and status == 'rejected'

.. needpie:: System requirement --> SW Requirements Linkage Status
    :labels: Linked,  Not Linked
    :explode: 0, 0.1
    :colors: #278d3e, #b2253b
    :text_color: w
    :legend:

    (type=='req-sys') and (not(satisfies_back is None or len(satisfies_back)==0))
    (type=='req-sys') and (   (satisfies_back is None or len(satisfies_back)==0))

.. needpie:: System requirement --> Stakeholder Requirements Linkage Status
    :labels: Linked,  Not Linked
    :explode: 0, 0.1
    :colors: #278d3e, #b2253b
    :text_color: w
    :legend:

    (type=='req-sys') and (not(satisfies is None or len(satisfies)==0))
    (type=='req-sys') and (   (satisfies is None or len(satisfies)==0))

.. needpie:: System Requirements --> Test case Linkage Status
    :labels: Linked,  Not Linked
    :explode: 0, 0.1
    :colors: #278d3e, #b2253b
    :text_color: w
    :legend:

    (type=='req-sys') and (not(verify_back is None or len(verify_back)==0))
    (type=='req-sys') and (   (verify_back is None or len(verify_back)==0))
