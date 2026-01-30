.. _swa-decisions:

Architecture Decisions
------------------------

.. TODO: Add some description of what is a architectural decision ... and how to come to it?

.. container:: sidebar

   .. container:: formalpara

      Important, expensive, large scale or risky architecture decisions
      including rationales. With "decisions" we mean selecting one
      alternative based on given criteria.

   Please use your judgement to decide whether an architectural decision
   should be documented here in this central section or whether you
   better document it locally (e.g. within the white box template of one
   building block).

   Avoid redundancy. Refer to section 4, where you already captured the
   most important decisions of your architecture.

   .. container:: formalpara

      Stakeholders of your system should be able to comprehend and
      retrace your decisions.

   .. container:: formalpara

      Various options:

   - ADR (`Documenting Architecture
     Decisions <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>`__)
     for every important decision

   - List or table, ordered by importance and consequences or:

   - more detailed in form of separate sections per decision

   .. container:: formalpara

      See `Architecture Decisions <https://docs.arc42.org/section-9/>`__
      in the arc42 documentation. There you will find links and examples
      about ADR.

This section documents important, expensive, critical, large scale or risky design decision and states the reasons behind the decision.

Software architecture relevant decisions are documented in the following.


Decision Overview
~~~~~~~~~~~~~~~~~~~~

.. list-table:: Architecture Decision Overview Table
   :widths: 5 95
   :header-rows: 1

   *  - #
      - Decision


   *  - 1
      - Use ros2 as the development framework.

   *  - 2
      -

.. _swa-decision-development_framework:

#1 Development Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

More details will come ...

.. _swa-decision-title:

#2 Decision Title
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

More details will come ...

.. _swa-decision-template:

Decision Template (Please Copy Me)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please use this template to document the software architecture decisions.

Problem Description
"""""""""""""""""""""""""""""""""

What is the problem?

Why is it relevant for the software architecture?

What impact has the decision?



Influencing Factors
"""""""""""""""""""""""""""""""""

What constrains do we have?

What quality attributes do we have to consider?

What risks are affected?


Assumptions
"""""""""""""""""""""""""""""""""

What assumptions have been made?

Which assumptions can be checked?

What new risks needs to be considered?


Alternatives
"""""""""""""""""""""""""""""""""

What solution options are considered?

How do we evaluate these options?

What options are deliberately not considered?

.. list-table:: Decision Alternatives for XY
   :widths: 30 60 60
   :header-rows: 1

   *  - Alternative
      - Pro
      - Con

   *  - <Alternative 1>
      -
         - good because A
         - good because B

      -
         - bad because A
         - bad because B

   *  - <Alternative 2>
      -
         - good because A
         - good because B

      -
         - bad because A
         - bad because B

Decision
"""""""""""""""""""""""""""""""""

   When is the decision made?
   Who took the decision?
   How is it justified?

Decision was taken in a decision meeting: dd.mm.yyyy "title of the meeting"

Participants:

   - Name (role)
   - Name (role)

Decision: Name of the alternative from the table. (Please update overview tables as well)

..
   .. container:: formalpara-title

      **Contents**

   Important, expensive, large scale or risky architecture decisions
   including rationals. With "decisions" we mean selecting one alternative
   based on given criteria.

   Please use your judgement to decide whether an architectural decision
   should be documented here in this central section or whether you better
   document it locally (e.g. within the white box template of one building
   block).

   Avoid redundancy. Refer to section 4, where you already captured the
   most important decisions of your architecture.

   .. container:: formalpara-title

      **Motivation**

   Stakeholders of your system should be able to comprehend and retrace
   your decisions.

   .. container:: formalpara-title

      **Form**

   Various options:

   -  ADR `Architecture Decision
      Record <https://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions>`__
      for every important decision

   -  List or table, ordered by importance and consequences or:

   -  more detailed in form of separate sections per decision

   See `Architecture Decisions <https://docs.arc42.org/section-9/>`__ in
   the arc42 documentation. There you will find links and examples about
   ADR.
