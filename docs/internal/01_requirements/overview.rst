.. _requirements:

Requirements Overview
==========================


Overview
--------------------------------

.. starts a vertical scrollable div   
.. raw:: html

   <div class="v-scrollable-div">

.. needflow::
   :filter: type == 'strat-req' or type == 'req-sw' or type == 'sh-req' or type == 'sys-req' or (type == 'issue' and 'epic' in tags)
   :show_link_names:

.. ends a vertical scrollable div
.. raw:: html
   
   </div>

Status Summary
--------------------------------

Requirement Status Overview: 

.. needpie::
   :labels: draft, in discussion, agreed, rejected, no status
   :legend:

   (type == 'sh-req' or type == 'sys-req' or type == 'req-sw' or (type == 'issue' and 'epic' in tags)) and status == 'draft'
   (type == 'sh-req' or type == 'sys-req' or type == 'req-sw' or (type == 'issue' and 'epic' in tags)) and status == 'in discussion'
   (type == 'sh-req' or type == 'sys-req' or type == 'req-sw' or (type == 'issue' and 'epic' in tags)) and status == 'agreed'
   (type == 'sh-req' or type == 'sys-req' or type == 'req-sw' or (type == 'issue' and 'epic' in tags)) and status == 'rejected'
   (type == 'sh-req' or type == 'sys-req' or type == 'req-sw' or (type == 'issue' and 'epic' in tags)) and (status != 'rejected') and (status != 'agreed') and (status != 'in discussion') and (status != 'draft')

Requirement Summary List: 

.. needtable::
   :columns: id, title, status, refines
   :filter: type == 'req-sw' or type == 'sh-req' or type == 'sys-req' or (type == 'issue' and 'epic' in tags)
   :sort: id


.. toctree::
    :maxdepth: 1
    :hidden:

    software/software.rst
    /src/moduleA/docs/moduleA_requirements.rst
    /src/moduleB/docs/moduleB_requirements.rst