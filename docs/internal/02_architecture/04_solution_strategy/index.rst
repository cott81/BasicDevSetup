
.. _swa-solution-strategy:

Solution Strategy
--------------------

.. container:: sidebar

   .. container:: formalpara

      A short summary and explanation of the fundamental decisions and
      solution strategies, that shape system architecture. It includes

   - technology decisions

   - decisions about the top-level decomposition of the system, e.g.
     usage of an architectural pattern or design pattern

   - decisions on how to achieve key quality goals

   - relevant organizational decisions, e.g. selecting a development
     process or delegating certain tasks to third parties.

   .. container:: formalpara

      These decisions form the cornerstones for your architecture. They
      are the foundation for many other detailed decisions or
      implementation rules.

   .. container:: formalpara

      Keep the explanations of such key decisions short.

   Motivate what was decided and why it was decided that way, based upon
   problem statement, quality goals and key constraints. Refer to
   details in the following sections.

   .. container:: formalpara

      See `Solution Strategy <https://docs.arc42.org/section-4/>`__ in
      the arc42 documentation.
    

The solution strategy table is a highly condensed overview of the software architecture and its solutions to achieve the quality goals.
The solutions are just named with a short description of their positive contributions to the assigned quality goal.
The description is kept short on purpose to keep this table short and readable.
More details are linked in the description, if necessary or available.

**Disclaimer: Table at the moment just contains examples to get the idea**

.. list-table:: Solution Strategy Table
  :widths: 5 30 65
  :header-rows: 1

  * - Quality Goal
    - Architectural Solution
    - Description and Benefits

  * - e.g. Usability
    -
      1. **e.g. Behavior Tree (BT)**
    -
      1. **BT** allows a visual presentation (e.g. with the Groot tool) of the robot's behavior that is more intuitive to discuss (even with non-technical stakeholders) compared to a code-level walk-trough.


  * - e.g. Maintainability/Modifiability
    -
      1. **ROS2 development framework** (nodes, launch)
      2. **arc42-based software architecture documentation** using **docs-as-code**
    -
      1. **ROS2** is a defacto standard in robotic development. Its component-based philosophy (nodes) supports a clear modularization in the software and its launch system makes it easy to change and extend the robot system.
      2. **arc42** is an established standard to document your architecture. It provides a well-known and intuitive structure that supports comprehensibility (keep an overview).
         We implement it as docs-as-code (in Sphinx) to keep documentation close to the developers to lower the burden to keep it up to date.


  * - e.g. Reliability
    -
      1. **xray** test tooling
      2. **CI/CD** ecosystem
      3. **Quality Levels** checked with CI/CD governed by EPQ

    -
      1. **xray** supports to define and manage manual (and automated) tests and improves analysability and testability.
      2. **CI/CD** provides continuous automatic building and testing of every increment. Our ecosystem uses Jenkins as the main executor on a cloud-based setup to allow us to scale.
         Testing includes unit testing, simulation testing, quality tests, KPI tests, ...
      3. **Quality Levels** is an iterative approach to increase the development quality level by level per component. Each level extends existing or adds new quality requirements driven by the EPQ team.
         Quality levels are automatically checked (as far as possible) with a tool executed in our CI/CD.
