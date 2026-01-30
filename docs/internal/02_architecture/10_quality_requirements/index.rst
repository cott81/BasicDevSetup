.. _swa-quality_requirements:

Quality Requirements
==============================


.. container:: sidebar

   .. container:: formalpara

      This section contains all relevant quality requirements.

   The most important of these requirements have already been described
   in section 1.2. (quality goals), therefore they should only be
   referenced here. In this section 10 you should also capture quality
   requirements with lesser importance, which will not create high risks
   when they are not fully achieved (but might be *nice-to-have*).

   .. container:: formalpara

      Since quality requirements will have a lot of influence on
      architectural decisions you should know what qualities are really
      important for your stakeholders, in a specific and measurable way.

   .. container::

      - See `Quality
        Requirements <https://docs.arc42.org/section-10/>`__ in the
        arc42 documentation.

      - See the extensive `Q42 quality model on
        https://quality.arc42.org <https://quality.arc42.org>`__.

.. _`_quality_requirements_overview`:

Quality Requirements Overview
-----------------------------

.. container:: sidebar

   .. container:: formalpara

      An overview or summary of quality requirements.

   .. container:: formalpara

      Often we encounter dozens (or even hundreds) of detailed quality
      requirements. In this overview section you should try to
      summarize, e.g. by describing categories or topics (as suggested
      by `ISO
      25010:2023 <https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:ed-2:v1:en>`__
      or `Q42 <https://quality.arc42.org>`__)

   If these summary descriptions are already precise, specific enough
   and measurable, you may skip section 10.2.

   .. container:: formalpara

      Use a simple table in which each line contains a category or topic
      and a short description of the quality requirement. Alternatively,
      you may use a mindmap to structure these quality requirements. In
      literature, the idea of a *quality attribute tree* has also been
      described, which puts the generic term "quality" as the root and
      uses a tree-like refinement of the term "quality". [Bass+21]
      introduced the term "Quality Attribute Utility Tree" for this
      purpose.

.. _`_quality_scenarios`:

Quality Scenarios
-----------------

.. container:: sidebar

   .. container:: formalpara

      Quality scenarios make quality requirements concrete and allow to
      decide whether they are fulfilled (in the sense of acceptance
      criteria). Ensure that your scenarios are specific and measurable.

   Two kinds of scenarios are especially useful:

   - *Usage scenarios* (also called application scenarios or use case
     scenarios) describe the system’s runtime reaction to a certain
     stimulus. This also includes scenarios that describe the system’s
     efficiency or performance. Example: The system reacts to a user’s
     request within one second.

   - *Change scenarios* describe the desired effect of a modification or
     extension of the system or of its immediate environment. Example:
     Additional functionality is implemented or requirements for a
     quality attribute change, and the effort or duration of the change
     is measured.

   .. container:: formalpara

      Typical information for detailed scenarios include the following:

   In short form (favoured in the Q42 model):

   - **Context/Background**: What kind of system or component, what is
     the envirionment or situation?

   - **Source/Stimulus**: Who or what initiates or triggers a behaviour,
     reaction or action.

   - **Metric/Acceptance Criteria**: A response including a *measure* or
     *metric*

   The long form of scenarios (favoured by the SEI and [Bass+21]) is
   more detailed and includes the following information:

   - **Scenario ID**: A unique identifier for the scenario.

   - **Scenario Name**: A short, descriptive name for the scenario.

   - **Source**: The entity (user, system, or event) that initiates the
     scenario.

   - **Stimulus**: The triggering event or condition the system must
     address.

   - **Environment**: The operational context or condition under which
     the system experiences the stimulus.

   - **Artifact**: The building-blocks or other elements of the system
     affected by the stimulus.

   - **Response**: The outcome or behavior the system exhibits in
     reaction to the stimulus.

   - **Response Measure**: The criteria or metric by which the system’s
     response is evaluated.

   .. container:: formalpara

      See `the Q42 quality model website <https://quality.arc42.org>`__
      for detailes examples of quality requirements.

   .. container::

      - Len Bass, Paul Clements, Rick Kazman: "Software Architecture in
        Practice", 4th Edition, Addison-Wesley, 2021.




This table shows again the quality goal definitions from Section "Introduction and Goals" and adds the related quality scenarios as references.

.. TODO: test a need table ... how to add quality scenarios into it ???s

Here comes a table out of quality requirements

.. 
  .. needtable:: Mapping of Quality Goals and Sub Quality Goals to Quality Scenarios
    :types: bcr2-req
    :filter: id.startswith("REQ_QG_")
    :columns: misc as "Prio", title, brief as "Description",status
    :colwidths: 5,10,40,5
    :style: table
    :sort: misc

All details about the used method and the inputs can be found on the `Quality Goal Refinement miro board <https://miro.com/app/board/uXjVOjBMFrU=/>`_.

.. TODO: one needflow for each top-level item (better vis)

.. 
  .. needflow:: Quality Goal Tree
    :types: bcr2-req
    :filter: id.startswith("REQ_QG_")
    :link_types: requires
    :show_link_names:


.. _swa-quality_tree:

Quality Tree
~~~~~~~~~~~~~

The quality tree (as defined in ATAM – Architecture Tradeoff Analysis Method) with quality scenarios references as leafs.

..  figure:: https://wiki.bsh-sdd.com/rest/gliffy/1.0/embeddedDiagrams/9ae03ab5-99aa-4ac5-8ad8-0c11c499a7f5.png
   :name: img-bcr2-quality-tree
   :alt: Here an image of the bcr2 quality tree
   :width: 100%
   :align: center

You find the formulated quality scenarion in the following section.
The tree structure with priorities provides an overview of bcr2 quality requirements.
The inner circle notes the quality goals. The more to the outside the more specific.
The most outer elements define related quality scenarios (QS).

.. _swa-quality_scenarios:

Quality Scenarios
~~~~~~~~~~~~~~~~~~~~

The quality scenarios are ordered by their primary relation to the quality goals.

Quality Scenarios for the TOP5 quality goals:
""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. TODO: define quality scenarios as needs objects
    only the quality scenarios here, "quality tree structure" as QG requirements (-> similar to high-level req?)

.. 
  .. needtable:: Summary of Quality Scenarios: Usability / UX
    :types: bcr2-req
    :filter: id.startswith("REQ_QSC_")
    :columns: id, title, brief, part_of, status
    :colwidths: 10, 10,40,10,5
    :style: table
    :sort: misc

.. next table for next top level quality goal

**Details of the TOP5 Quality Scenarios**

.. 
  .. bcr2-req:: Auto Cleaning Suggestion
    :id: REQ_QSC_AutoCleaningSuggestion
    :status: discussed
    :tags: qs_5
    :misc: 5
    :part_of: REQ_QG_AutoSuggestions
    :brief: Auto Suggestion for Regular Cleaning

      The robot recognizes a frequently manually triggered cleaning task (e.g. start every wednesday at 7pm).
      The robot notifies the user and makes a suggestion to schedule regular cleaning at the time.
      The user gets the message on the app, is able to understand the suggestion and can accept/deny or edit it.

