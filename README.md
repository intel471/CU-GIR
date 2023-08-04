# **INTEL 471**
## **Cyber Underground General Intelligence Requirements (CU-GIRs)**


### What is CU-GIR?

The Cyber Underground General Intelligence Requirements framework (CU-GIR) is a baseline tool to assist in organizing, prioritizing, producing and measuring production of cyber underground intelligence. Central to this framework are General Intelligence Requirements (GIRs) — a compilation of frequently asked questions applicable to the cyber underground (i.e., illicit forums, instant messaging channels, marketplaces, products, services and adversaries). Each GIR includes a definition and the essential elements of information (EEIs) needed to answer the basic questions who, what, when, where, why and how.

### Who is it for?

Primary users of the CU-GIR framework are cyber threat intelligence (CTI) planners, analysts, researchers and collection managers.

## How is it used?

The CU-GIR framework can be used in a variety of ways. An analyst or researcher can use this as a hip-pocket reference to spot ad-hoc collection opportunities in the underground. An intelligence planner or manager can use this to support the development of intelligence requirements and to measure the intel team’s value to its stakeholders and organization.

## How does Intel 471 Use the CU-GIRs?

Intel 471 shapes its intelligence collection focus and production based largely on GIRs that have been prioritized by our customers. Using the CU-GIR framework, each customer selects and ranks a subset of GIRs that Intel 471 uses to task collection and synchronize reporting.

### How does Intel 471 Share the CU-GIRs?

Intel 471 shares the CU-GIR framework in two formats:

- The first format is a PDF handbook (CU-GIRh) that can be accessed via the following link : https://intel471.com/resources/cyber-underground-handbook.

- The second format of the CU-GIR framework can be accessed directly from a STIX JSON file hosted on this GitHub. The current version of the CU-GIR framework will always be hosted in the /STIX/Current/intel471_cu-gir.json file. This file will be automatically updated with each CU-GIR version release and therefore consideration of potential breaking changes to your environment should be taken if ingesting this file directly. The current version will also be hosted in the /STIX/Historic directory alongside any other previous versions.

## STIX

The current version of the CU-GIR framework utilizes STIX version 2.1.

The STIX namespace (see: https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070594) used for all GIR SDOs is "19213586-e154-47c6-94c0-76c929cc7890". All GIR SDO UUIDs (UUIDv5) are generated using this namespace and the GIR ID. Each GIR SDO will have a custom STIX field named "x_gir_id" containing the Intel 471 GIR ID (eg, ATM Malware = x_gir_id:1.1.10), as well as a custom STIX field named "x_deprecated" that holds a boolean value representing the items state.

### STIX Domain Objects (SDO):

    - The Top Level GIRs are of the SDO type Grouping.
    - The GIR #1 (Malware) tree are of the SDO type Malware.
        - Malware tools are of the SDO type Tool.
    - The GIR #2 (Vuln. and Exploits) tree are of the SDO type Vulnerability.
    - The GIR #3 (Infrastructure) tree are of the SDO type Infrastructure.
    - The GIR #4 (Fraud, Identity Theft and Unauthorized Access) tree are of mixed SDO types.
    - The GIR #5 (Adversary Tactics and Activities):
        - All GIR TTPs are of the SDO type Attack Pattern
        - Where applicable, each Attack Pattern has been linked, via external reference, to MITRE ATT&CK IDs and/or KillChain Phases.
    - The GIR #6 (Threats Impacting Industry or Region):
        - Regions are of the SDO type Location.
            - Each country is linked to their respective ISO 3166-1 alpha-2 code.
        - Industry and Sectors are of the SDO type Identity.
   
    - Extra information for each GIR has been linked in the following way:
        - Stakeholder information is of the SDO type Note.
        - Courses of Action are of the SDO type Course of Action (Mitigates).
            - EEIs are of the SDO type Note and are linked to Courses of Action (not directly to a GIR).
            - EEIs have a custom STIX field named "x_coa_uuid" containing the UUID of the linked CoA.
        - Common Use Cases are of the SDO type Course of Action (Investigates).
        - Child GIRs inherit Extra information from their parents through STIX Relationship Object (SRO) type Relationship.
   
### STIX Relationship Objects (SRO):

    - Each GIR has an SRO, type Relationship, linking to its parent and child.
    - SRO Relationship IDs are a concatenation of the source_ref and target_ref IDs, separated by a hyphen (-).
    - Extra Information for each GIR (EEIs, Stakeholders etc) is linked to each GIR via SRO type Relationship.

## New to Cyber Threat Intelligence Frameworks?

If you're new to CTI or new to utilizing frameworks to aid in combatting threats, sign up to attend an Intelligence Planning Workshop hosted by Intel 471 (https://go.intel471.com/intelligence-planning-workshop). The following articles may also be of interest:

- https://intel471.com/blog/introducing-intel-471s-cybercrime-underground-general-intelligence-requirements-cu-gir-a-common-framework-to-address-a-common-challenge

- https://intel471.com/resources/whitepapers/using-cyber-frameworks-to-action-cti-and-enhance-your-security-posture

## Contribute

Want to help? Have some ideas? We're all ears... Contact us at gir-suggestions@intel471[.]com.
