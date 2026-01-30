UselessL2Cmp - Detailed Design (DRAFT)
=========================================

.. arch-swc:: UselessL2Cmp Component
   :id: SWC_UselessL2Cmp
   :status: draft
   :specified_by: REQ_SW_L2ComponentA
   :feature: FeatureX

   The level 2 component **UselessL2Cmp** is responsible for ... (one sentence summary of the component).


Purpose and Concept
---------------------------

.. Template Hints:
   - What is the purpose of the function to be designed?
   - What functionality is to be designed?
   - Is the function safety critical? If yes, describe what safety critical is.
   - The concept behind the function, algorithms, and high-level interactions

Requirements
---------------------------

.. Template Hints:
   - Link to the software requirements relevant to this component.
   - Optional: List of requirements (tags, numbers, heading)

.. needtable::
   :columns: id, title, safety_integrity, security_relevance, verification_criteria
   :filter: type == 'req-sw' and ('SWC_UselessL2Cmp' in specified_by_back)
   :sort: id


Integration into Software Architecture
------------------------------------------

.. Template Hints:
   - Block diagram: How are the new and/or adapted components integrated into the existing architecture (layers, interfaces, call sequence, storage, error handling, …) provided and required interfaces
   - Sequence diagrams showing interaction between this component and other components (if necessary)


Design Constraints
---------------------------

.. Template Hints:
   - Any constraints which impact the design. This may include:
      - Integration constraints (size, execution time, process raster)
      - interface specifications e.g. Corba, DCOM
      - resource considerations,
      - the use of a specific design pattern,
      - mandated re-use of existing elements,
      - Variant handling 


Component Design
---------------------------

.. Template Hints:
   - Description of the design
   - Component diagram for new and/or adapted modules with interface description
   - If architectural relevant, describe also the internals of the module
      - Class diagrams 
   - (showing interactions between internal sub-components)
   - Design of safety critical part
      - How is the initialization ensured?
      - What calibration is required? 

Configuration
---------------------------

.. Template Hints:
   - Configuration (e.g. Parameters like #defines etc.)


Errors
---------------------------

.. Template Hints:
   - Errors list of what the component can detect/return.


Testing
---------------------------

.. Template Hints:
   - Test description, not fully defined, only collection of test ideas
   - Description of tests to be performed 

UselessL2Cmp Implementations
================================

.. src-trace::
   :project: basic_dev_setup
   :directory: ./moduleA/l2/uselessL2Cmp