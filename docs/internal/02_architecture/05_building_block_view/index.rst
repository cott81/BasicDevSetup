.. _swa-building-block-view:

Building Block View
--------------------

.. container:: sidebar

   Here you describe the decomposition of the overall system using the
   following white box template. It contains

   - an overview diagram

   - a motivation for the decomposition

   - black box descriptions of the contained building blocks. For these
     we offer you alternatives:

     - use *one* table for a short and pragmatic overview of all
       contained building blocks and their interfaces

     - use a list of black box descriptions of the building blocks
       according to the black box template (see below). Depending on
       your choice of tool this list could be sub-chapters (in text
       files), sub-pages (in a Wiki) or nested elements (in a modeling
       tool).

   - (optional:) important interfaces, that are not explained in the
     black box templates of a building block, but are very important for
     understanding the white box. Since there are so many ways to
     specify interfaces why do not provide a specific template for them.
     In the worst case you have to specify and describe syntax,
     semantics, protocols, error handling, restrictions, versions,
     qualities, necessary compatibilities and many things more. In the
     best case you will get away with examples or simple signatures.


The building block view shows the static decomposition of the system
into building blocks (modules, components, subsystems, classes,
interfaces, packages, libraries, frameworks, layers, partitions, tiers,
functions, macros, operations, datas structures, etc) as well as their
dependencies (relationships, associations, etc)

This view is mandatory for every architecture documentation. In analogy
to a house this is the *floor plan*.

Technical context diagram gives the level 0 overview over the complete system.
Level 1 perspectives give a white box view into the level 0 entities (software execution devices).

.. _swa-rcb_block_diagram:

Level 1 - Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here comes a block diagram that shows lvl1 blocks and their dependencies

.. 
  .. bcr2-sw-arc:: RCB Block Diagram
    :id: SW_ARC_Embedded_RCB
    :describes: SW_BBE_Embedded_RCB
    :brief: Block Diagram of the Basis Software of the RCB

    This diagrams gives a high level view on the RCB. Highest level elements are the Base OS (pantacor) and the deployed containers ( N&B, HCC, ... are there more?).
    The diagram further shows their principle interactions.

    ..  figure::  https://wiki.bsh-sdd.com/rest/gliffy/1.0/embeddedDiagrams/9507271d-304d-4e7d-b944-0ecacccac8a4.png
        :name: img-RCB-static-block-diagram-container-level
        :alt: Here an image of RCB static block diagram that shows a container view
        :width: 100%
        :align: center

    .. list-table:: StaticBlockDiagRCB
        :widths: 15 70
        :header-rows: 1

        * - Entity
          - Responsibility Description

        * - **pantacor containers**
          -

        * - Navigation and Behaviour (N&B) Container
          - Provides the autonomous cleaning behaviour and user interaction (UI)

        * - Video and AI Container
          - Under consideration wether it comes as an own container or if it is integrated in the N&B container. Security considerations are necessary, because video streaming has its own internet connection (out of latency reasons). Ros2 as framework is desired. Security impacts have to be discussed as well.

        * - uservices Container
          - TODO: have to be further clarified

        * - EOL Test Robotic Container
          - Under consideration

        * - Self Test Robotic Container
          - Under consideration

        * - comapp / Home Connect Client (HCC) Container
          - Implement the interface to Home Connect

        * - **OS and pantacor infrastructure**
          -

        * - Linux DBUS
          - Implements inter-container communication. Libraries are provided by GDE.

        * - bootloader, pantocor, OS, SyMaNA
          - Provide the support for pantocor hypervisor to run the containers, implement the HW interfaces.


.. _swa-nb_container_block_diagram:

Level 2 - N&B Container Block Diagram
""""""""""""""""""""""""""""""""""""""""""""""""""""

..

This diagram shows the principle building blocks of the N&B Container and their principle data flows.
Note that a building block is an abstract entity and may consist of other (executable) software building blocks (here ros nodes).
Building blocks with high inherent complexity are treated as subsystems and get a level 3 white box diagram.
For others further design information are found in the detailed design documentation.

**Architecture Style: Sense-Plan-Act** ... perhaps some words here if applicable


.. 
  .. bcr2-sw-arc:: N&B Block Diagram
    :id: SW_ARC_NBContainer
    :describes: SW_BBE_Robot
    :brief: Block Diagram of the N&B Container

    .. figure:: https://wiki.bsh-sdd.com/rest/gliffy/1.0/embeddedDiagrams/da8093f0-8b48-4ae0-bae9-2c63b629138f.png
      :name: img-NnB-static-block-diagram-feature-level
      :alt: Here an image of N&B static block diagram
      :width: 100%
      :align: center

    .. needtable:: Static Block Diagram of N&B: Perception Area
      :types: bcr2-sw-bbe
      :filter: 'SW_BBE_SensePerception' in part_of or 'SW_BBE_SensePerception' in part_of_back
      :columns: id as "Elements in Perception", brief as "Description", misc as "Node Pkg"
      :colwidths: 10, 40, 10
      :style: table




.. _swa-cpm_block_diagram:

Level 1 - another  Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This give a short overview of the CPM software architecture.
