2025-11-25 13:52:15,326 - INFO - detected formats: [<InputFormat.PDF: 'pdf'>]
2025-11-25 13:52:15,333 - INFO - Going to convert document batch...
2025-11-25 13:52:15,335 - INFO - Initializing pipeline for StandardPdfPipeline with options hash 44ae89a68fc272bc7889292e9b5a1bad
2025-11-25 13:52:15,336 - INFO - rapidocr cannot be used because onnxruntime is not installed.
2025-11-25 13:52:15,337 - INFO - easyocr cannot be used because it is not installed.
2025-11-25 13:52:16,064 - INFO - Accelerator device: 'cpu'
[INFO] 2025-11-25 13:52:16,086 [RapidOCR] base.py:22: Using engine_name: torch
[INFO] 2025-11-25 13:52:16,099 [RapidOCR] download_file.py:68: Initiating download: https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.4.0/torch/PP-OCRv4/det/ch_PP-OCRv4_det_infer.pth
[INFO] 2025-11-25 13:52:21,011 [RapidOCR] download_file.py:82: Download size: 13.83MB
[INFO] 2025-11-25 13:52:21,158 [RapidOCR] download_file.py:95: Successfully saved to: /home/ubuntu/rhai_se/.venv/lib/python3.12/site-packages/rapidocr/models/ch_PP-OCRv4_det_infer.pth
[INFO] 2025-11-25 13:52:21,162 [RapidOCR] torch.py:54: Using /home/ubuntu/rhai_se/.venv/lib/python3.12/site-packages/rapidocr/models/ch_PP-OCRv4_det_infer.pth
[INFO] 2025-11-25 13:52:21,461 [RapidOCR] base.py:22: Using engine_name: torch
[INFO] 2025-11-25 13:52:21,462 [RapidOCR] download_file.py:68: Initiating download: https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.4.0/torch/PP-OCRv4/cls/ch_ptocr_mobile_v2.0_cls_infer.pth
[INFO] 2025-11-25 13:52:22,582 [RapidOCR] download_file.py:82: Download size: 0.56MB
[INFO] 2025-11-25 13:52:22,591 [RapidOCR] download_file.py:95: Successfully saved to: /home/ubuntu/rhai_se/.venv/lib/python3.12/site-packages/rapidocr/models/ch_ptocr_mobile_v2.0_cls_infer.pth
[INFO] 2025-11-25 13:52:22,595 [RapidOCR] torch.py:54: Using /home/ubuntu/rhai_se/.venv/lib/python3.12/site-packages/rapidocr/models/ch_ptocr_mobile_v2.0_cls_infer.pth
[INFO] 2025-11-25 13:52:22,690 [RapidOCR] base.py:22: Using engine_name: torch
[INFO] 2025-11-25 13:52:22,691 [RapidOCR] download_file.py:68: Initiating download: https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.4.0/torch/PP-OCRv4/rec/ch_PP-OCRv4_rec_infer.pth
[INFO] 2025-11-25 13:52:24,290 [RapidOCR] download_file.py:82: Download size: 25.67MB
[INFO] 2025-11-25 13:52:24,595 [RapidOCR] download_file.py:95: Successfully saved to: /home/ubuntu/rhai_se/.venv/lib/python3.12/site-packages/rapidocr/models/ch_PP-OCRv4_rec_infer.pth
[INFO] 2025-11-25 13:52:24,599 [RapidOCR] torch.py:54: Using /home/ubuntu/rhai_se/.venv/lib/python3.12/site-packages/rapidocr/models/ch_PP-OCRv4_rec_infer.pth
2025-11-25 13:52:24,919 - INFO - Auto OCR model selected rapidocr with torch.
2025-11-25 13:52:24,920 - INFO - Accelerator device: 'cpu'
2025-11-25 13:52:25,307 - INFO - Accelerator device: 'cpu'
2025-11-25 13:52:26,809 - INFO - Processing document mil_std_1316f.pdf
[INFO] 2025-11-25 13:52:32,353 [RapidOCR] download_file.py:68: Initiating download: https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.4.0/resources/fonts/FZYTK.TTF
[INFO] 2025-11-25 13:52:33,532 [RapidOCR] download_file.py:82: Download size: 3.09MB
[INFO] 2025-11-25 13:52:33,569 [RapidOCR] download_file.py:95: Successfully saved to: /home/ubuntu/rhai_se/.venv/lib/python3.12/site-packages/rapidocr/models/FZYTK.TTF
2025-11-25 13:54:44,274 - INFO - Finished converting document mil_std_1316f.pdf in 148.95 sec.
NOT MEASUREMENT SENSITIVE

## MIL-STD-1316F 18 August 2017 MIL-STD-1316E

## SUPERSEDING 10 JULY 1998

## DEPARTMENT OF DEFENSE DESIGN CRITERIA STANDARD

## FUZE DESIGN, SAFETY CRITERIA FOR

<!-- image -->

## AMSC N/A FSC 13GP DISTRIBUTION STATEMENT A. Approved for public release; distribution is unlimited.

## MIL-STD-1316F

## FOREWORD

1. This standard is approved for use by all Departments and Agencies of the Department of Defense (DoD).
2. This standard establishes specific design safety criteria for fuzes.  It applies primarily to the safety and arming functions performed by fuzes for use with munitions.  The safety and arming requirements specified herein are mandatory fundamental elements of design, engineering, production, and procurement of fuzes.  Fuzes shall provide safety that is consistent with assembly, handling, storage, transportation, and disposal.
3. This revision has resulted in many changes to MIL-STD-1316E, but the most significant ones include the following:
- a. Paragraph on logic functions (see 4.11) is introduced to address the use of logic devices.
- b. Requirements for safety qualification of fuzes is changed to the applicable Joint Ordnance Test Procedures (JOTPs).
- c. Explosive Ordnance Disposal (EOD) features is updated.
- d. Significant changes are made for non-interrupted explosive train control (see 5.3.4) that addresses energy interrupters.
- e. The guidance for non-armed condition assurance (see 4.6.6) is modified.
- f. Other requirements for maximum allowable electrical sensitivity (MAES) requirements (see 5.6), and munitions that include sub-munitions (see 5.7) are incorporated.
- g. New guidance for non-interrupted explosive train control (see 5.3.4) is incorporated.
- h. Definitions such as enabling, explosive train, common mode failures, initiator, maximum no-fire stimulus (MNFS) are revised and a definition for common cause failures is added.
- i. On fuze safety system (see 4.2), clarification is provided for operation of safety features and arming of submunitions while new guidance is provided for safety architecture distribution and status checks.
- j. Modifications to the safety system failure rate (see 4.3) introduces additional evaluation.
- k. Explosives listed for inline use (see Table I) approved by all services is revised.
- l. New advisory guidance for addressing electronics counterfeit and cybersecurity concerns are referenced (see 6.0).
- m. Inclusion of software development procedures is now identified in analyses (see 4.3.1) and in design for quality control, inspection, and maintenance (see 4.4).
- n. Clarification is made for design features (see 4.6) for stored energy, compatibility of fuzes, and electrical firing energy dissipation.
- o. On electrical and electromagnetic environments (see 4.8), several new JOTPs are introduced.
- p. Visual indication requirement is added for bomb fuzes that utilize internal stored energy.

## MIL-STD-1316F

4. Comments, suggestions, or questions regarding this document should be addressed to: Commander, U.S. Army ARDEC, ATTN: RDAR-EIQ-SA, Picatinny Arsenal, New Jersey 07806-5000 or e-mailed to usarmy.picatinny.ardec.list.ardec-stdznbranch@mail.mil  Since contact information can change, the currency of this address information may be verified using the ASSIST Online database at https://assist.dla.mil.

PARAGRAPH

PAGE

1. SCOPE  ................................................................................................................................  1

1.1 Scope . ..............................................................................................................................  1

1.2 Applicability  . ..................................................................................................................  1

1.3 Excluded munitions ..........................................................................................................  1

2. APPLICABLE DOCUMENTS ..........................................................................................  2

2.1 General

..................................................................................................................  2

2.2 Government documents  ....................................................................................................  2

2.2.1 Specifications, standards and handbooks ......................................................................  2

2.2.2 Other Government documents, drawings and publications  .........................................  4

2.3 Non-Government publications ........................................................................................  5

2.4 Order of precedence  ..........................................................................................................  5

3. DEFINITIONS ...................................................................................................................  6

3.1 Armed

..................................................................................................................  6

3.2 Arming delay.. ..................................................................................................................  6

3.3 Assembled fuze.................................................................................................................  6

3.4 Booster and lead explosives .............................................................................................  6

3.5 Common cause failures ....................................................................................................  6

3.6 Common mode failures ....................................................................................................  6

3.7 Credible environment .......................................................................................................  6

3.8 Credible failure mode. ......................................................................................................  7

3.9 Dud

..................................................................................................................  7

3.10 Enabling

. ..................................................................................................................  7

3.11 Environment. ..................................................................................................................  7

3.12 Environmental stimulus  ..................................................................................................  7

3.13 Explosive ordnance disposal ..........................................................................................  7

3.14 Explosive train  ................................................................................................................  7

3.15 Fail-safe design  ...............................................................................................................  7

3.16 Function

..................................................................................................................  7

3.17 Fuze (Fuzing System)  .....................................................................................................  7

3.18 Fuze installation  ..............................................................................................................  7

3.19 Fuze safety system  ..........................................................................................................  7

<!-- image -->

## CONTENTS

## MIL-STD-1316F

| 3.20 Independent safety feature..............................................................................................7                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.21 Initiator ..................................................................................................................7                                                                                                                   |
| 3.22 Interrupted explosive train..............................................................................................8                                                                                                                      |
| 3.23 Launch cycle...................................................................................................................8                                                                                                                |
| 3.24 Main charge . ..................................................................................................................8                                                                                                               |
| 3.25 Maximum no-fire stimulus (MNFS)...............................................................................8                                                                                                                                 |
| 3.26 Premature function .........................................................................................................8                                                                                                                   |
| 3.27 Primary explosives. ........................................................................................................8                                                                                                                   |
| 3.28 Safe separation distance..................................................................................................8                                                                                                                     |
| 3.29 Safety and arming device ...............................................................................................8                                                                                                                       |
| 3.30 Safety feature..................................................................................................................9                                                                                                               |
| 3.31 Safety system failure ......................................................................................................9                                                                                                                   |
| 3.32 Sensor, environmental ....................................................................................................9                                                                                                                     |
| 3.33 Sterilization                                                                                                                                                                                                                                   |
| ..................................................................................................................9 4. GENERAL REQUIREMENTS........................................................................................10                |
| 4.1 General ................................................................................................................10                                                                                                                       |
| 4.2 Fuze safety                                                                                                                                                                                                                                      |
| system .........................................................................................................10                                                                                                                                   |
| 4.2.1 Inclusion of safety features..........................................................................................10                                                                                                                       |
| 4.2.2 Operation of safety features using environmental stimuli...........................................10                                                                                                                                          |
| 4.2.3 Arming delay. ..............................................................................................................11                                                                                                                 |
| 4.2.4 Arming of submunitions..............................................................................................11                                                                                                                         |
| 4.2.5 Safety architecture distribution....................................................................................11                                                                                                                         |
| 4.2.6 Manual arming.............................................................................................................11                                                                                                                   |
| 4.2.7 Status checks...............................................................................................................11                                                                                                                 |
| 4.3 Safety system failure rate ...............................................................................................11                                                                                                                     |
| 4.3.1 Analyses ................................................................................................................12                                                                                                                    |
| 4.4 Design for quality control, inspection, and maintenance ...............................................12                                                                                                                                        |
| 4.6 Design features. ..............................................................................................................13                                                                                                                |
| 4.5 Design approval..............................................................................................................13                                                                                                                  |
| elements....................................................................................13                                                                                                                                                       |
| 4.6.2 Compatibility of fuze                                                                                                                                                                                                                          |
| 4.6.3 Manually enabled safety features. ...............................................................................14 4.6.4 Electrical firing energy dissipation..............................................................................14 |
| 4.6.5. Explosive ordnance disposal (EOD) reviewing authority ..........................................14 features...........................................................14                                                                      |
| 4.6.5.1 Explosive ordnance disposal (EOD)                                                                                                                                                                                                            |

6.1 Intended use

## MIL-STD-1316F

| 4.6.5.2 EOD procedures .......................................................................................................14       | 4.6.5.2 EOD procedures .......................................................................................................14       |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 4.6.6 Non-armed condition assurance ..................................................................................15               | 4.6.6 Non-armed condition assurance ..................................................................................15               |
| 4.6.6.1 Visual indication.......................................................................................................15     | 4.6.6.1 Visual indication.......................................................................................................15     |
| 4.6.6.2 Visual indicators for bomb fuzes..............................................................................15               | 4.6.6.2 Visual indicators for bomb fuzes..............................................................................15               |
| 4.7 Documentation................................................................................................................15    | 4.7 Documentation................................................................................................................15    |
| 4.7.1 Critical components and characteristics ......................................................................16                 | 4.7.1 Critical components and characteristics ......................................................................16                 |
| 4.8 Electrical and electromagnetic environments.................................................................16                     | 4.8 Electrical and electromagnetic environments.................................................................16                     |
| 4.9 Reviewing authority .......................................................................................................16      | 4.9 Reviewing authority .......................................................................................................16      |
| 4.10 Qualification of fuzes. ..................................................................................................17      | 4.10 Qualification of fuzes. ..................................................................................................17      |
| 4.11 Logic functions.............................................................................................................17    | 4.11 Logic functions.............................................................................................................17    |
| 4.11.1 Logic devices.............................................................................................................17    | 4.11.1 Logic devices.............................................................................................................17    |
| 4.11.2 Safety features in logic devices .................................................................................17            | 4.11.2 Safety features in logic devices .................................................................................17            |
| 4.11.3 Logic state verification. .............................................................................................17       | 4.11.3 Logic state verification. .............................................................................................17       |
| 4.11.4 Implementation review.............................................................................................17            | 4.11.4 Implementation review.............................................................................................17            |
| 4.12 Active hazard mitigation device..................................................................................17               | 4.12 Active hazard mitigation device..................................................................................17               |
| 5. DETAILED REQUIREMENTS ....................................................................................18                        | 5. DETAILED REQUIREMENTS ....................................................................................18                        |
| 5.1 General ................................................................................................................18         | 5.1 General ................................................................................................................18         |
| 5.2 Post-safe-separation safety .............................................................................................18        | 5.2 Post-safe-separation safety .............................................................................................18        |
| 5.3 Explosive materials and trains........................................................................................18           | 5.3 Explosive materials and trains........................................................................................18           |
| 5.3.1 Explosive compositions.............................................................................................              | 18                                                                                                                                     |
| 5.3.2 Explosive sensitivity of lead and booster explosives ..................................................18                        | 5.3.2 Explosive sensitivity of lead and booster explosives ..................................................18                        |
| 5.3.3 Explosive train interruption.........................................................................................20          | 5.3.3 Explosive train interruption.........................................................................................20          |
| 5.3.4 Non-interrupted explosive train control ......................................................................20                 | 5.3.4 Non-interrupted explosive train control ......................................................................20                 |
| 5.3.4.1 Electrical initiator .....................................................................................................21   | 5.3.4.1 Electrical initiator .....................................................................................................21   |
| 5.3.4.1.1 Electrical initiator sensitivity.................................................................................21          | 5.3.4.1.1 Electrical initiator sensitivity.................................................................................21          |
| 5.3.4.1.2 Maximum allowable electrical sensitivity (MAES) requirement..........................21                                      | 5.3.4.1.2 Maximum allowable electrical sensitivity (MAES) requirement..........................21                                      |
| 5.4 Sterilization . ................................................................................................................21 | 5.4 Sterilization . ................................................................................................................21 |
| 5.4.1 Sterilization of torpedoes and sea mines .....................................................................22                 | 5.4.1 Sterilization of torpedoes and sea mines .....................................................................22                 |
| 5.5 Self-destruction...............................................................................................................22  | 5.5 Self-destruction...............................................................................................................22  |
| 5.6 Electro-explosive device (EED) no-fire threshold safety margins.................................22                                 | 5.6 Electro-explosive device (EED) no-fire threshold safety margins.................................22                                 |
| 5.7 Munitions including sub-munitions................................................................................22                | 5.7 Munitions including sub-munitions................................................................................22                |
| 5.8 Fail-safe design...............................................................................................................22  | 5.8 Fail-safe design...............................................................................................................22  |
| 5.9 Fuze setting ................................................................................................................22    | 5.9 Fuze setting ................................................................................................................22    |
| 6. NOTES............................................................................................................................23 | 6. NOTES............................................................................................................................23 |

................................................................................................................  23

## MIL-STD-1316F

| 6.2 Acquisition Requirements ..............................................................................................23        | 6.2 Acquisition Requirements ..............................................................................................23        |
|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 6.3 Additional criteria...........................................................................................................23 | 6.3 Additional criteria...........................................................................................................23 |
| 6.4 Custodian of service-approvals for lead and booster explosives....................................24                             | 6.4 Custodian of service-approvals for lead and booster explosives....................................24                             |
| 6.5 Hazard analyses ..............................................................................................................24 | 6.5 Hazard analyses ..............................................................................................................24 |
| 6.6 Electronic device material management.........................................................................24                 | 6.6 Electronic device material management.........................................................................24                 |
| 6.7 Subject term (key word) listing. .....................................................................................24         | 6.7 Subject term (key word) listing. .....................................................................................24         |
| 6.8 International standardization agreements. ......................................................................25               | 6.8 International standardization agreements. ......................................................................25               |
| 6.9 Changes from previous issue..........................................................................................25          | 6.9 Changes from previous issue..........................................................................................25          |
| TABLE                                                                                                                                | TABLE                                                                                                                                |
| Table I                                                                                                                              | Approved Explosives ....................................................................................19                           |

## 1. SCOPE

- 1.1 Scope.  This standard establishes design safety criteria for fuzes and Safety and Arming (S&amp;A) devices that are subsystems of fuzes.
- 1.2 Applicability.  This standard applies to the design of fuzes and S&amp;A devices.
- 1.3 Excluded munitions.  This standard does not apply to fuzes and S&amp;A devices for the following:
- a. Nuclear weapon systems and trainers.
- b. Hand grenades.
- c. Flares and signals dispensed by hand-held devices.
- d. Hand-emplaced, remotely controlled or networked munitions.
- e. Pyrotechnic countermeasure devices.

## MIL-STD-1316F

## 2. APPLICABLE DOCUMENTS

- 2.1 General.  The documents listed in this section are specified in sections 3, 4, or 5 of this standard.  This section does not include documents cited in other sections of this standard or recommended for additional information or as examples.  While every effort has been made to ensure the completeness of this list, document users are cautioned that they must meet all specified requirements of documents cited in sections 3, 4, or 5 of this standard, whether or not they are listed.

## 2.2 Government documents.

- 2.2.1 Specifications, standards and handbooks.  The following specifications, standards, and handbooks form a part of this document to the extent specified herein.  Unless otherwise specified, the issues of these documents are those cited in the solicitation or contract.

## INTERNATIONAL STANDARDIZATION AGREEMENTS

| STANAG 4157   | -   | Safety, Arming and Functioning Systems (SAF Systems) Testing Requirements                           |
|---------------|-----|-----------------------------------------------------------------------------------------------------|
| STANAG 4170   | -   | Principles and Methodology for the Qualification of Explosive Materials for Military Use            |
| STANAG 4518   | -   | Safe Disposal of Munitions, Design Principles and Requirements, and Safety Assessment               |
| AOP 7         | -   | Manual of Data Requirements and Tests for the Qualification of Explosive Materials for Military Use |
| AOP 20        | -   | Safety, Arming and Functioning Systems Manual of Tests                                              |
| AOP 52        | -   | Guidance on Software Safety Design and Assessment of Munition Related Computing Systems             |

## MIL-STD-1316F

## MIL-STD-1316F

## DEPARTMENT OF DEFENSE SPECIFICATIONS

| MIL-DTL-440   | -   | Compositions A3 and A4                                          |
|---------------|-----|-----------------------------------------------------------------|
| MIL-DTL-14970 | -   | Explosive Composition A5                                        |
| MIL-C-21723   | -   | Composition CH-6                                                |
| MIL-DTL-23659 | -   | Initiator, Electric, General Design Specification               |
| MIL-DTL-32064 | -   | Explosive, Plastic-Bonded, Pressed, PBXN-11                     |
| MIL-DTL-32387 | -   | Explosive, Ink: EDF-11                                          |
| MIL-H-48358   | -   | HMX/Resin Explosive Composition LX-14-0 (For Use in Ammunition) |
| MIL-E-81111   | -   | Explosive, Plastic-Bonded Molding Powder (PBXN-5)               |
| MIL-E-82740   | -   | Explosive, Plastic Bonded, Injection Moldable (PBXN-301)        |
| MIL-DTL-82874 | -   | Explosive, Plastic-Bonded, Pressed, PBXN-7                      |
| MIL-DTL-82875 | -   | Explosive, Plastic-Bonded, Pressed, PBXN-9                      |
| MIL-E-82903   | -   | Explosives, HNS-IV and HNS-V                                    |

## DEPARTMENT OF DEFENSE STANDARDS

- MIL-STD-331 -Fuzes, Ignition Safety Devices and Other Related Components, Environmental and Performance Tests For
- MIL-STD-461 -Requirements for the Control of Electromagnetic Interference Characteristics of Subsystems and Equipment
- MIL-STD-464 -Electromagnetic Environmental Effects Requirements for Systems

(Copies of these documents are available online at http://quicksearch.dla.mil.)

## MIL-STD-1316F

## DEPARTMENT OF DEFENSE HANDBOOKS

No Designator

- -Joint Software System Safety Engineering Handbook

(Copies of this document are available online at http://system-safety.org/links/.)

2.2.2 Other Government documents, drawings and publications.  The following other Government documents, drawings and publications form a part of this document to the extent specified herein.  Unless otherwise specified, the issues are those cited in the solicitation.

## JOINT ORDNANCE TEST PROCEDURE (JOTP)

| JOTP-050   | -   | Safety Design Requirements for Active Hazard Mitigation Device (AHMD) Employed to Address Fast and Slow Cook-off Thermal Threats   |
|------------|-----|------------------------------------------------------------------------------------------------------------------------------------|
| JOTP-051   | -   | Technical Manual for the Use of Logic Devices in Safety Features                                                                   |
| JOTP-052   | -   | Guideline for Qualification of Fuzes, Safe and Arm (S&A) Devices, and Ignition Safety Devices                                      |
| JOTP-053   | -   | Electrical Stress Test                                                                                                             |
| JOTP-061   | -   | Hazards of Electromagnetic Radiation to Ordnance (HERO) Safety Test                                                                |
| JOTP-062   | -   | Personnel-borne ElectroStatic Discharge (PESD) and Helicopter-borne ElectroStatic Discharge (HESD) Requirements for Ordnance       |

(Copies of these documents are available online at http://quicksearch.dla.mil).

## NAVY WEAPON SPECIFICATION

| WS-4660   | - Dipam Explosive   |
|-----------|---------------------|
| WS-5003   | - HNS Explosive     |

## MIL-STD-1316F

WS-12604 -

Explosive Plastic-Bonded Powder (PBXN-6)

WS-35173 -

Explosive, Pressed, RSI-007

(Unless otherwise indicated, copies of Navy Weapon Specifications are available from Commander, Indian Head Division, Naval Surface Warfare Center, Document Control, (Code E12P), Suite 103 Indian Head, MD 20640-5085

- 2.3 Non-Government publications.  The following documents form a part of this document to the extent specified herein.  Unless otherwise specified, the issues of these documents are those cited in the solicitation or contract.

## SAE INTERNATIONAL

| Colors Used in   | Fluorescent green, Color No. 38901   |
|------------------|--------------------------------------|
| Government       | Fluorescent red, Color No. 38905     |
| SAE-AMS-STD-595  | Fluorescent orange, Color No. 38903  |

(Copies of this document are available from the SAE International at SAE Customer Service, 400 Commonwealth Drive, Warrendale, PA 15096-0001, or from www.sae.org.)

- 2.4 Order of precedence.  Unless otherwise noted herein or in the contract, in the event of a conflict between the text of this document and the references cited herein, the text of this document takes precedence (see 6.2).  Nothing in this document, however, supersedes applicable laws and regulations unless a specific exemption has been obtained.

## 3.  DEFINITIONS

For interpretation of this standard, the following specific definitions apply.

- 3.1 Armed.  A fuze is armed when any firing stimulus can produce fuze function.  A fuze is considered armed when if either of the following is true:
- a. A fuze employing explosive train interruption (see 5.3.3) is considered armed when the interrupter(s) position is ineffective in preventing propagation of the explosive train at a rate equal to or exceeding 0.5 percent at a confidence level of 95 percent.
- b. A fuze employing a non-interrupted explosive train (see 5.3.4) is considered armed when the stimulus available for delivery to the initiator equals or exceeds the initiator's maximum no-fire stimulus (MNFS).
- 3.2 Arming delay.  The time elapsed, or distance traveled by the munition, from launch to arming (see 3.19, 3.26 and 4.2.3).
- 3.3 Assembled fuze.  The completed fuze with all component parts put together; a fuze requiring no added components or parts to prepare it for installation into the munition in which it is to function.  Assembling the fuze is the process of putting the parts and components together.
- 3.4 Booster and lead explosives.  Booster and lead explosives are compounds or formulations, such as those explosives listed (see Table I), which are used to transmit and augment the detonation reaction.
- 3.5 Common cause failures.  Failures that occur in more than one component, that result from a single cause, condition, or a single environment.  For example, two or more components may fail due to the single cause of heating.  The failure modes of the components may or may not be the same.  For example, two or more components, such as transistors, may fail in different ways (separation of dielectric and leads in one, and fusing of leads in another) due to the single cause of heating, or the failure of two gates on a single digital integrated circuit due to a loss of the ground lead to the chip.
- 3.6 Common mode failures.  The same failures that occur in more than one component, that result from, or are caused by the same or different conditions or environments applied to each component.  The components may be different in nature, but fail in the same manner.
- 3.7 Credible environment.  An environment that a device may be exposed to during its life cycle (manufacturing to tactical employment, or eventual demilitarization).  These include extremes of temperature and humidity, electromagnetic effects, line voltages, etc. Combinations of environments that can be reasonably expected to occur must also be considered within the context of credible environments.

## MIL-STD-1316F

## MIL-STD-1316F

- 3.8 Credible failure mode.  A failure mode of either a single component or the combination of multiple components that has a reasonable probability of occurring during a fuzing system's life cycle.
- 3.9 Dud.  A munition which has failed to function, although functioning was intended.
- 3.10 Enabling.  Changing the state of a safety feature to permit arming.
- 3.11 Environment.  A specific physical condition to which the fuze may be exposed.
- 3.12 Environmental stimulus.  A specific stimulus obtained from an environment.
- 3.13 Explosive ordnance disposal.  The detection, identification, field evaluation, rendering safe, recovery, and final disposal of hazardous unexploded explosive ordnance.
- 3.14 Explosive train.  The detonation or deflagration train (i.e., transfer mechanism), beginning with the first explosive or pyrotechnic element, even in the case of a distributed system where the energy conversion may occur at some distance and in a physically different module from the explosive or pyrotechnic element and terminating in the main charge (e.g., munition functional mechanism, high explosive, pyrotechnic compound).
- 3.15 Fail-safe design.  A characteristic of a fuze system or part thereof designed to prevent fuze function when components fail.
- 3.16 Function.  A fuze 'functions' when it produces an output capable of initiating a train of fire or detonation in an associated munition.
- 3.17 Fuze (Fuzing System).  A physical system designed to sense a target or respond to one or more prescribed conditions, such as elapsed time, pressure, or command, and initiate a train of fire or detonation in a munition.  Safety and arming are primary roles performed by a fuze to preclude initiation of the munition before the desired position or time.
- 3.18 Fuze installation.  The act of installing or inserting the assembled fuze into the munition in which it is to function.
- 3.19 Fuze safety system.  The aggregate of elements (e.g., environment sensors, launch event sensors, command functioned devices, arming energy interrupters, explosive train interrupter, etc.) included in the fuze to prevent arming and functioning of the fuze until a valid launch environment has been sensed and the arming delay has been achieved.
- 3.20 Independent safety feature.  A safety feature is independent if its integrity is not affected by the function or malfunction of other safety features.
- 3.21 Initiator.  The component or components which convert the firing energy

## MIL-STD-1316F

resulting in initiation of the first explosive or pyrotechnic element, even in the case of a distributed system where the energy conversion may occur at some distance and in a physically different module from the explosive or pyrotechnic element.  The first explosive or pyrotechnic element of the explosive train will always be considered as part of the initiator. Examples of Initiators include but are not limited to:

- a. Exploding Bridgewire (EBW) devices.
- b. Semi-Conductor Bridge (SCB) Initiators
- c. Laser diodes, the first component of the explosive or pyrotechnic train, and the in between (transfer) components.
- d. Exploding Foil Initiators (EFI), including the bridge and explosive component.
- e. Stab detonators.
6. 3.22 Interrupted explosive train.  An explosive train in which the explosive path between the primary explosives and the lead and booster (secondary) explosives is functionally separated until arming.
7. 3.23 Launch cycle.  The period between the time the munition is irreversibly committed to launch and the time it leaves the launcher.
8. 3.24 Main charge.  The explosive charge which is provided to accomplish the end result in the munition; e.g., bursting a casing to produce blast and fragmentation, splitting a canister to dispense submunitions, or producing other effects for which it may be designed. Main charge explosives are compounds or formulations, which are used as the final charge in any explosive application.
9. 3.25 Maximum no-fire stimulus (MNFS).  The stimulus level at which the probability of functioning the initiator is 0.005 at the 95% single sided lower confidence. Stimulus refers to the characteristic(s) which is (are) most critical in defining the no-fire performance of the initiator.
10. 3.26 Premature function.  A fuze function before completion of the arming delay.
11. 3.27 Primary explosives.  Primary explosives are sensitive materials, such as lead azide or lead styphnate, which are used to initiate detonation.  They are used in primers or detonators, are sensitive to heat, impact or friction and undergo a rapid reaction upon initiation.
12. 3.28 Safe separation distance.  The minimum distance between the delivery system (or launcher) and the launched munition beyond which the hazards to the delivery system and its personnel resulting from the functioning of the munition are acceptable.
13. 3.29 Safety and arming device.  A device that prevents fuze arming until an

acceptable set of conditions has been achieved and subsequently effects arming and allows functioning.

- 3.30 Safety feature.  An element or combination of elements that prevents unintentional arming or functioning.
- 3.31 Safety system failure.  A failure of the fuze safety system to prevent unintentional arming or functioning.
- 3.32 Sensor, environmental.  A component or series of components designed to detect and respond to a specific environment.
- 3.33 Sterilization.  A design feature that permanently prevents a fuze from functioning.

## 4.  GENERAL REQUIREMENTS

- 4.1 General.  The following general requirements apply to all fuzes and fuze components within the scope of this document.
- 4.2 Fuze safety system.  In order to preclude unintended fuze arming, the fuze safety system shall:
- a. not initiate the arming sequence except as a consequence of an intentional launch.
- b. not be susceptible to common cause or common mode failures.
- c. not contain any single-point failure mode prior to or at the initiation of the arming cycle.
- d. reduce to a minimum single-point failure modes during the arming cycle.  The time window associated with these single-point failures shall be reduced to a minimum and shall exist only at or near the expiration of the intended arming delay.

In addition, the fuze design shall prohibit premature fuze arming or functioning if any or all electrical safety or energy control features fail in any given state or credible mode.  These failure modes include both random and induced failures that occur prior to, during, or after application of electrical power to the fuze.

- 4.2.1 Inclusion of safety features.  Fuzing systems shall include at least two independent safety features, each capable of preventing unintentional arming.  The design shall minimize common cause failures.  Control and operation of safety features are to be functionally isolated from other processes within the munition system and each safety feature shall be capable of preventing unintentional arming of the fuzing system.  All items, including software, used to enable the fuze safety features shall be considered part of the fuzing system and must meet the requirements of this standard.  The rationale for not complying with independence and/or isolation of at least two safety features shall be provided to the appropriate review authority (see 4.9) for approval.
- 4.2.2 Operation of safety features using environmental stimuli.  The stimuli which enable the independent safety features to operate shall be derived from different environments or different combinations of environments or both; where combinations are used each combination shall be different.  The environments selected and sensed by the fuzing system shall be robust such that they do not include any environment or levels of environmental stimulus that may be experienced by the fuze prior to the commencement of the launch cycle.  Operation of at least one of the independent safety features shall depend on sensing an environment after first motion in the launch cycle or on sensing a post launch environment.  In the absence of a robust launch environment, launch events may be used if

such events irreversibly commit the munition to complete the launch cycle.  The events shall be time windowed and sequenced.  Munitions that are designed to be jettisoned shall not have safety compromised by the action of such release.

- 4.2.3 Arming delay.  One or more features of the fuze safety system shall prevent arming after launch or deployment until the specified safe separation distance or equivalent arming delay has been achieved for all operational conditions.
- 4.2.4 Arming of submunitions.  The fuzing system shall be designed so that no submunition can arm solely as a result of dispersing from the carrier munition during a credible accident before launch of the carrier munition.
- 4.2.5 Safety architecture distribution.  The elements of the fuzing system that prevent arming until valid launch environments have been satisfied and the proper arm delay expended should be collocated to the maximum extent practical.  Signals that contribute to fuze arming shall not be susceptible to subversion due to the effects of system or lifecycle environmental stimuli.  For systems that employ non-collocated fuze safety, the appropriate review authority (see 4.9) shall be consulted.
- 4.2.6 Manual arming.  The fuze safety system design shall ensure that fuzing systems are not capable of being armed manually.
- 4.2.7 Status checks.  The final tactical configuration of the fuze safety system shall not have the capability to subvert safety features (e.g., provide power to any safety switches prior to intended arming) as a result of any status checks.  In addition, stimuli shall not be provided to initiators except for the purpose of their initiation or after intended arming.  For applications performing status checks on safety systems prior to irrevocable intent to launch, consult with the appropriate review authority (see 4.9).
- 4.3 Safety system failure rate.  The fuze safety system failure rate shall be calculated for all logistic and tactical phases from fuze manufacture to safe separation or to the point at which friendly forces and equipment no longer need protection.  The safety system failure rate shall be verified to the extent practical by test and analysis during fuze evaluation and shall not exceed the rates given for the following phases:
- a. Prior to intentional initiation of the arming sequence:  one failure to prevent arming or functioning (irrespective of arming) in one million fuzes.
- b. Prior to tube exit: one failure to prevent arming in ten thousand fuzes, and one failure to prevent functioning in one million fuzes.  Rationale for not meeting the requirements shall be provided to the appropriate safety authority (see 4.9).
- c. Between initiation of the arming sequence or tube exit, if tube launched, and safe separation:  one failure to prevent arming in one thousand fuzes.  The rate of fuze functioning during this period shall be as low as practical and consistent with the risk established as acceptable for premature munition functioning.

- d. The design of each safety feature shall be robust enough to permit exposure of the fuze system to the environments and handling stresses anticipated in its life cycle with no deterioration or degradation of the fuze safety system.  The robustness of each safety feature and its contribution to the overall safety of the fuzing system shall be assessed through analysis and testing (such as subverted safety tests) and its acceptability shall be determined by the appropriate review authority (see 4.9).
2. 4.3.1 Analyses.  The following analyses shall be performed to identify hazardous conditions for the purpose of their elimination or control.
- a. A preliminary hazard analysis shall be conducted to identify and classify hazards of normal and abnormal environments, as well as conditions and personnel actions that may occur in the phases before safe separation.  This analysis shall be used in the preparation of system design, test and evaluation requirements.
- b. System hazard analyses shall be conducted to arrive at an estimate of the safety system failure rate and to identify any credible failure modes.  Detailed analyses such as fault trees as well as failure modes, effects and criticality analysis shall be conducted as a minimum in order to identify hazardous conditions for the purpose of their elimination or control.
- c. For fuzing systems containing an embedded computer, microprocessor, microcontroller or other computing device, the system hazard analyses shall include a determination of the contribution of all elements (including hardware and software) to the enabling of a safety feature. Where software is shown to directly control or enable elements of the fuze safety system, detailed analyses and testing of the software is required following the appropriate guidelines, such as AOP-52 or Joint Software System Safety Engineering Handbook.
6. 4.4 Design for quality control, inspection, and maintenance.
- a. Fuzes shall be designed and documented to facilitate application of effective quality control and inspection procedures.  Design characteristics critical to fuze safety shall be identified to assure that the designed safety is maintained.
- b. The design of the fuze shall facilitate the use of inspection and test equipment for monitoring all characteristics which assure the safety and intended functioning of the fuze at all appropriate stages.  The fuze design should facilitate the use of automatic inspection equipment.
- c. Software development shall be in accordance with accepted high quality software development procedures, such as AOP-52 or Joint Software System Safety Engineering Handbook, and shall be submitted to the appropriate review authority (see 4.9) for approval.

## MIL-STD-1316F

- 4.5 Design approval.  At the inception of engineering development, the developing agency should obtain approval from the appropriate review authority of both the design concept and the methodology for assuring compliance with safety requirements.  At the completion of engineering development, the developing agency shall present a safety assessment to the appropriate safety authority (see 4.9) for review to obtain approval of the design.

## 4.6 Design features.

- 4.6.1 Stored energy.  Fuzing systems shall use environmentally derived energy generated after initiation of the launch or deployment cycle in preference to pre-launch stored energy to enable or arm the system. If this cannot be practically achieved and stored energy is used, then the system safety hazard analyses shall demonstrate that no failure mode for that source of energy will degrade the safety system failure rates beyond acceptable levels.  Additionally, where practical, the same stored energy source shall not be used to both remove a lock and arm the S&amp;A.

Examples of stored energy components are:

- a. Batteries
- b. Charged capacitors
- c. Compressed gas devices
- d. Explosive actuators
- e. Biased springs
6. 4.6.2 Compatibility of fuze elements.  All fuze materials shall be chosen to be compatible and stable so that under all life-cycle conditions none of the following shall occur in an unarmed fuze:
- a. Premature arming.
- b. Dangerous ejection of material.
- c. Deflagration or detonation of the lead or booster.
- d. Formation of dangerous or incompatible compounds. Material that could contribute to the formation of more volatile or more sensitive compounds should not be used. Materials shall be treated, located, or contained to prevent the formation of a hazardous compound.
- e. Compromise or degradation of safety, self-destruct, or sterilization features.
- f. Production of unacceptable levels of toxic or other hazardous materials.

## MIL-STD-1316F

- 4.6.3 Manually enabled safety features.  When manually operable safety features critical to fuzing system safety are used, their design shall minimize the occurrence of inadvertent or unintended manual enabling actions.
- 4.6.4 Electrical firing energy dissipation.  For electrically initiated fuzing systems, the fuze design shall include a provision to dissipate the firing energy after the expiration of the operating lifetime of the fuze, or a fuze failure. The timeframe associated with the dissipation should be as short as practical based on operational requirements.  The means of dissipation shall not be susceptible to single-point, common-mode, or common-cause failures and shall not degrade the overall safety of the fuze before initiation of the arming sequence.
- 4.6.5. Explosive ordnance disposal (EOD) reviewing authority.  All new or altered fuze designs, new applications of existing designs, or replacement or substitution of energetic materials, or power sources, shall be presented to the appropriate service's EOD Research, Development, Test and Evaluation (RDT&amp;E) authority noted below for technical advice and assistance in determining viable design approaches or trade-offs to satisfy EOD requirements:
- 4.6.5.1 Explosive ordnance disposal (EOD) features.  When required, features shall be incorporated in the fuze to facilitate the fuze being rendered safe by EOD tools, equipment, and procedures even if sterilization or self-destruction features are incorporated.
- 4.6.5.2 EOD procedures.  Fuzes will be tested and evaluated by the appropriate service's EOD RDT&amp;E authority to develop Joint Service approved EOD procedures. Additional requirements for the implementation and assessment of safety related EOD features is given in STANAG 4518.

- a. For Army:

US Army RDECOM-ARDEC ATTN:  RDAR-MEX-P/ Bldg 91N Picatinny Arsenal, NJ  07806-5000

- b. For Navy and

Commanding Officer NSWC IHEODTD ATTN:  US Program Analyst (D-11A) 2008 Stump Neck Road Indian Head, MD  20640-5070

Marine Corps:

- c. For Air Force:

Commander ATTN:  AFCEC/CXE 2008 Stump Neck Road

Indian Head, MD  20640-5070

## MIL-STD-1316F

- 4.6.6 Non-armed condition assurance.  Fuzing system designs shall incorporate one or more of the following:
- a. A feature that prevents assembly of the fuzing system in an armed condition.
- b. A feature that provides a positive means of determining that the fuzing system is not armed after final fuze assembly. Where the fuzing system is accessible prior to or after installation into the munition, the positive means of determination shall also be available. For fuzing systems with non-interrupted explosive trains, the means used shall positively prevent the accumulation of energy, of the type used for arming, in the system prior to installation in the munition. Any means employed to comply with this paragraph shall not unacceptably degrade safety.
- c. A feature that prevents installation of an armed, assembled fuzing system into a munition.
- d. If arming and reset of the assembled fuzing system in tests is a normal procedure in manufacturing, inspection, or at any time prior to its installation into a munition, subparagraph a is not sufficient and either subparagraph b or c must also be met.
- 4.6.6.1 Visual indication.  If visual indication of the non-armed or armed condition is employed in the fuze, visible indicators shall be designed to provide a positive, unambiguous indication of condition.  Indicator failure shall not result in a false nonarmed indication.  If color coding is used to represent condition, the colors and coding shall be as follows:
- a. Non-armed condition.  Fluorescent green background with the letter S or word SAFE superimposed thereon in white.  Colors shall be nonspecular.
- b. Armed condition.  Fluorescent red or fluorescent orange background with the letter A or the word ARMED superimposed thereon in black. Colors shall be nonspecular.
- c. Suggested color specifications.
- 1) Fluorescent green, Color No. 38901 per SAE-AMS-STD-595.
- 2) Fluorescent red, Color No. 38905 per SAE-AMS-STD-595.
- 3) Fluorescent orange, Color No. 38903 per SAE-AMS-STD-595.
- 4.6.6.2 Visual indicators for bomb fuzes.  For bomb fuzes utilizing stored energy internal to the fuze for arming, a visual indicator that is visible before and after installation into the munition is required.
- 4.7 Documentation.  The evaluation program used as the basis of the safety assessment that is prepared by the developing agency shall be documented in both detail

and summary form.

- 4.7.1 Critical components and characteristics.  Components of the fuzing system with characteristics that may be critical to safety shall be identified and appraised in a document that forms part of the fuzing system specification.  The evaluation of the critical components shall be presented as part of the design safety assessment of the fuzing system. The applicable drawings shall be annotated to show that the component is safety critical and cite the associated safety critical characteristics.
- 4.8 Electrical and electromagnetic environments.  Fuzes, in their normal life cycle configurations, shall not inadvertently arm or function during and after exposure to: hazards of electromagnetic radiation to ordnance (HERO), personnel electrostatic discharge (PESD), helicopter electrostatic discharge (HESD), precipitation-static (pstatic), electromagnetic pulse (EMP), electromagnetic interference (EMI), lightning effects (LE) or power supply transients (PST).  In addition, fuzes shall not exhibit unsafe operation during and after exposure to the above environments.  Fuzes shall be tested or evaluated for susceptibility in accordance with the following requirements and test procedures:
- 4.9  Reviewing authority.   All  new  or  altered  designs,  or  new  applications  of existing designs, shall be presented to the appropriate service safety review authority for a safety evaluation and/or certification of compliance with this standard:

- a. HERO -

per MIL-STD-464 / JOTP-061

- b. EMP and LE -

per MIL-STD-464

- c. EMI -

per MIL-STD-461

- d. PESD, HESD, p-static -

per MIL-STD-464 / JOTP-062

- e. PST -

per JOTP-053 (Electrical Stress Test)

- a. Army:

Chairman, Army Fuze Safety Review Board ATTN:  RDAR-EIZ Picatinny Arsenal, NJ  07806-5000

Email to: usarmy.pica.rdecom-ardec.mbx.afsrb@mail.mil

- b. Navy and Marine Corps

Chairman, Weapon System Explosives Safety Review Board, C/O Code N00ED 3817 Strauss Avenue Bldg D323 Suite 108 Indian Head, MD 20640 - 5151

- c. Air Force:

USAF Nonnuclear Munitions Safety Board

## MIL-STD-1316F

ATTN: 96TW/SES 1001 N 2 nd Street, Suite 366 Eglin Air Force Base, FL 32542-6838

- 4.10 Qualification of fuzes.  Safety qualification of fuzes shall adhere to Joint Ordnance Test Procedure JOTP-052 (Guideline for Qualification of Fuzes, Safe and Arm (S&amp;A) Devices, and Ignition Safety Devices (ISD)).  Testing shall be conducted in accordance with MIL-STD-331 and STANAG 4157 with AOP-20 as appropriate. Qualification test plans shall be submitted to the appropriate service safety reviewing authority (see 4.9) for approval.  To address unique program test requirements or issues, other test standards and procedures may be employed for qualification with the approval of the service safety reviewing authority.
- 4.11 Logic functions.  The design agency shall demonstrate that logic functions used in fuzing safety systems have been implemented in a safe manner.
- 4.11.1 Logic devices.  Any safety related logic implemented within the fuzing system shall not be erasable, alterable or reconfigurable by credible environments that the fuzing system would otherwise survive.  Additional requirements for the implementation of safety related logic is given in Joint Ordnance Test Procedure JOTP-051, Technical Manual for the Use of Logic Devices in Safety Features.
- 4.11.2 Safety features in logic devices.  Where logic devices are used to host safety features, the implementation will be evaluated in accordance with Joint Ordnance Test Procedure JOTP-051, Technical Manual for the Use of Logic Devices in Safety Features.
- 4.11.3 Logic state verification.  All logic states (e.g. state machines, etc.) in the fuze safety system must be capable of being identified and validated.
- 4.11.4 Implementation review.  The appropriate service safety review authority (see 4.9) will determine the acceptability of logic implementations.
- 4.12 Active hazard mitigation device.  Any active hazard mitigation devices used to reduce the severity of the munition's response when subjected to Insensitive Munitions (IM) thermal threat environments shall not degrade the fuzing system.  Additional requirements for the implementation of active hazard mitigation devices is given in Joint Ordnance Test Procedure JOTP-050 (Safety Design Requirements for Active Hazard Mitigation Device (AHMD) Employed to Address Fast and Slow Cook-Off Thermal Threats).

.

## 5.   DETAILED REQUIREMENTS

- 5.1 General.  The following detailed requirements shall apply for specific fuze designs.
- 5.2 Post-safe-separation safety.  When operational requirements necessitate protection of friendly forces in addition to the delivery system and its personnel, one of the following options shall be incorporated in the fuze design:
- a. Extension of the arming delay.
- b. Control of unintentional functioning after the proper arming delay.

The fuze requirements document shall specify for the selected option a minimum quantitative failure rate for the time frame after safe separation to attainment of the required protection or equivalent arming delay.

## 5.3 Explosive materials and trains.

- 5.3.1 Explosive compositions.  Explosive compositions in fuzes shall be qualified for use in accordance with STANAG 4170 and the US Annex in AOP-7 in their design role (primary, lead, booster, expulsion charges, etc.).  In addition, explosive compositions shall be chosen so that the fuze is safe and remains so under the specified conditions of storage and use.

## 5.3.2 Explosive sensitivity of lead and booster explosives.

- a. Only those explosives listed in Table I are approved by all services for use in a position leading to the initiation of a main charge without interruption. Materials approved as main charges may also be used as leads or boosters.
- b. Approval by all services must be received by the Chairman, DOD Fuze Engineering Standardization Working Group (see 6.4) before a new explosive can be added to Table I or a listed explosive can be deleted.  Approved explosives shall also be qualified in the fuze and certified by the associated safety authority (see 4.9) as acceptable for that fuze.
- c. The explosive material used in fuze systems shall not be altered by any means (precipitation, recrystallization, grinding, density changes, etc.) likely to increase its sensitivity beyond that at which the material was qualified and at which it is customarily used, unless it is requalified.

## MIL-STD-1316F

Table I - Approved Explosives

| Explosive                 | Specification   |
|---------------------------|-----------------|
| Comp A3                   | MIL-DTL-440     |
| Comp A4                   | MIL-DTL-440     |
| Comp A5                   | MIL-DTL-14970   |
| Comp CH6                  | MIL-C-21723     |
| DIPAM                     | WS-4660         |
| HNS Type 1 or Type 2 Gr A | WS-5003         |
| HNS-IV                    | MIL-E-82903     |
| LX-14                     | MIL-H-48358     |
| PBX 9407                  | MIL-R-63419     |
| PBXN-5                    | MIL-E-81111     |
| PBXN-6                    | WS-12604        |
| PBXN-7                    | MIL-DTL-82874   |
| PBXN-9                    | MIL-DTL-82875   |
| PBXN-11                   | MIL-DTL-32064   |
| PBXN-301                  | MIL-E-82740     |
| + RSI-007                 | WS 35173        |
| + EDF-11                  | MIL-DTL-32387   |
| * Tetryl                  | MIL-T-339       |
| * Tetryl Pellets          | MIL-P-46464     |
| PBXN-12                   | MIL-DTL-3228    |

## NOTES:

*   No longer manufactured; not for use in new developments.
+   3 grams maximum (in a single component) permitted for RSI-007 and EDF11.

## MIL-STD-1316F

## 5.3.3 Explosive train interruption.

- a. When an element of the explosive train contains explosive material other than allowed by 5.3.2, at least one interrupter (e.g., shutter, slider, rotor, etc.) shall functionally separate it from in-line, approved energetic materials until the arming sequence is completed as a consequence of intentional launch.  The interrupter(s) shall be directly locked mechanically in the safe position by at least two independent safety features.  These safety features shall not be removed prior to initiation of the launch cycle.
- b. A single interrupter locked by the two independent safety features is acceptable if the primary explosive is positioned such that omission of the interrupter will prohibit explosive train transfer.
- c. If  the  primary  explosive  is  positioned  such  that  safety  is  dependent  upon  the presence of an interrupter, the design shall include positive means to prevent the fuze from being assembled without the properly positioned interrupter.
- d. The effectiveness of interruption for the fuze explosive train in its configuration prior to initiation of the arming sequence shall be determined numerically in accordance with the Primary Explosive Component Safety Test of MIL-STD331.  If the explosive train interruption is removed progressively after intentional initiation of the launch sequence, the relationship between interrupter position and its effectiveness shall be established by a progressive arming test conducted in accordance with the Primary Explosive Component Safety Test, using a test strategy given by the Projectile Fuze Arming Distance Test of MIL-STD-331. The chosen test strategy and results shall be provided to the appropriate service safety authority (see 4.9) for approval.
5. 5.3.4 Non-interrupted explosive train control.  Explosive train interruption is not required when the explosive train contains only explosive materials allowed by 5.3.2.  The following methods shall be employed:
- a. At least two separate and independent safety features with all their associated components for environmental sensing, environment verification and energy interruption shall prevent arming until their arming environments have been validated.
- b. A third safety feature with its associated energy interrupter shall prevent arming until proper sequencing, and/or timing of the arming environments is validated.
- c. At least one energy interrupter shall operate dynamically to prevent arming if any or all of the energy interrupters malfunction statically.
- d. Validation of a post launch environment shall contribute to the enabling of a dynamic energy interrupter.

## MIL-STD-1316F

- e. A dynamic energy interrupter shall be driven by a unique signal.  The signal shall not be unintentionally generated by the effects of system or lifecycle environmental stimuli.
2. 5.3.4.1 Electrical initiator.  The initiator for an electrically fired non-interrupted explosive train shall be qualified in accordance with the test procedures of MIL-DTL-23659 Appendix A.
3. 5.3.4.1.1 Electrical initiator sensitivity.  The initiator for an electrically fired noninterrupted explosive train shall:
- a. Not be capable of being initiated when exposed to the greater of:
- 1) Commonly available electrical potentials;
- 2) Any electrical potential that may be present in the munition prior to an irreversible commit to launch; and
- 3) The  maximum  allowable  electrical  sensitivity  inputs  as  specified  in  paragraph 5.3.4.1.2.
- b. Not be capable of being initiated by any electrical potential as specified in paragraph 5.3.4.1.2 when applied to any accessible part of the fuzing system after installation into the munition or any munition subsystem.
9. 5.3.4.1.2 Maximum allowable electrical sensitivity (MAES) requirement.  For initiators to be used in an electrically fired non-interrupted explosive train, an allowable electrical sensitivity test program for qualification of the initiator shall be established and approved by the appropriate service safety review authority. The test shall include, as a minimum:
- a. Electrical  potentials  up  to  500  volts  in  accordance  with  MIL-DTL-23659 Appendix A; and
- b. Electrical potentials that may be present in the fuzing system, whether resulting from normal functioning or failures.

Results from the Electric Cook-Off test, the MAES, Maximum No Fire Voltage (MNFV) and the computation of the Maximum Allowable Safe Stimulus (MASS), that satisfy MIL-DTL-23659 Appendix A demonstrate compliance with the above requirements.  When voltages greater than 500 volts are present in the munition, evidence shall be presented to the appropriate safety review authority (see 4.9) for approval that demonstrates that the in-line initiator is insensitive or isolated to voltages up to and including the highest voltage present in the munition, excluding the firing voltage.

- 5.4 Sterilization.  Fuzing systems shall incorporate a sterilization feature based on its applicability to system requirements.

## MIL-STD-1316F

- 5.4.1 Sterilization of torpedoes and sea mines.  Fuze systems for torpedoes and sea mines shall provide for sterilization after safe jettison, after specified events and time, or when the munition is no longer capable of functioning reliably.
- 5.5 Self-destruction.  If required in the system requirement document, self-destruct feature(s) may be included.  Such feature(s) shall not increase the probability of hazards to the operator, over those that exist from the same munition fitted with a fuzing system without such a feature.  Self-destruct feature(s) shall not be capable of being enabled prior to launch and achieving safe separation distance or fuze arming delay.
- 5.6 Electro-explosive device (EED) no-fire threshold safety margins.  In any fuzing system in which safety is dependent on preventing the unintentional functioning of an EED, a minimum safety margin between the no-fire threshold (NFT) stimulus and the stimulus that could be induced by electrical or electromagnetic interference shall be demonstrated to and accepted by the appropriate service safety review authority (see 4.9) for approval.
- 5.7 Munitions including sub-munitions. For carrier munitions which include submunitions, the following shall apply:
- a. Probabilities and conditions given at paragraph 4.3 shall apply to the fuzing system of the submunition.
- b. The system hazard analysis shall demonstrate the requirements of paragraph 4.3 are met.
- 5.8 Fail-safe design.  Fuzing systems shall incorporate fail-safe design features based on their applicability to system requirements.
- 5.9 Fuze setting.  If fuze setting is safety critical (e.g., arming time, function time, or proximity broadcast turn-on time), uncontrolled alteration of the set value shall be prevented.

## 6.  NOTES

(This section contains information of a general or explanatory nature that may be helpful, but is not mandatory.)

- 6.1 Intended use.  This standard establishes specific design safety criteria for fuzes and safety and arming devices.
- 6.2 Acquisition Requirements.  Acquisition documents should specify the following:
- a. MIL-STD-1316 supersedes and takes precedence over the requirements of STANAG 4187.  It is noted that AOP-16 contains additional information addressing many of the requirements stated herein.
- 6.3 Additional criteria.  Individual services may issue regulations or instructions which impose additional design safety criteria or add clarifying guidelines such as:

| No Designator   | -   | U.S. Army Fuze Safety Review Board (AFSRB) Guidelines for Evaluation of Electronic Safety &Arming Systems                                            |
|-----------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------|
| No Designator   | -   | Weapon System Explosives Safety Review Board (WSESRB) Technical Manual for Electronic Safety and Arming Device with Non-Interrupted Explosive Trains |
| DoD DTM 17-001  |     | Cybersecurity in Defense Acquisition System                                                                                                          |
| DoDI 4140.67    | -   | DoD Counterfeit Prevention Policy                                                                                                                    |
| MIL-T-339       | -   | Tetryl (trinitrophenylmethylnitramine) (canceled)                                                                                                    |
| MIL-P-46464     | -   | Pellet, Tetryl (canceled)                                                                                                                            |
| MIL-R-63419     | -   | RDX/Vinyl Chloride, Copolymer Explosive Composition (PBX 9407) (For Use in Ammunition) (canceled)                                                    |
| MIL-STD-1901    | -   | Munition Rocket and Missile Motor Ignition System Design, Safety Criteria For                                                                        |
| MIL-STD-1911    | -   | Hand-Emplaced Ordnance Design, Safety Criteria For                                                                                                   |
| MIL-HDBK-504    | -   | Guidance on Safety Criteria for Initiation Systems                                                                                                   |
| STANAG 4187     | -   | Fuzing Systems: Safety Design Requirements                                                                                                           |

## MIL-STD-1316F

## MIL-STD-1316F

| STANAG 4560   | -   | Electro-Explosive Devices, Assessment and Test Methods for Characterization                             |
|---------------|-----|---------------------------------------------------------------------------------------------------------|
| AOP 16        | -   | Fuzing Systems: Guidelines for STANAG 4187                                                              |
| AOP 43        | -   | Electro-Explosive Devices Assessment and Test Methods for Characterization - Guidelines for STANAG 4560 |

- 6.4 Custodian of service-approvals for lead and booster explosives.

Chairman

DOD Fuze Engineering Standardization Working Group

U.S. Army Armament Research, Development and Engineering Center

ATTN: RDAR-EIZ

Picatinny Arsenal, NJ 07806-5000

- 6.5 Hazard analyses.  Techniques for conducting hazard analyses are described in:

MIL-STD-882 -

Standard Practice: System Safety

NUC REG 0492 -

Fault Tree Handbook

AFSC DH 1-6 -

Air Force Systems Command (AFSC) Design Handbook (DH) 1-6, System Safety

NAVSEA OD44942 -

Weapon System Safety Guidelines Handbook

6.6 Electronic device material management.  Anti-counterfeit measures for DoD weapon and information systems acquisition and sustainment to prevent the introduction of counterfeit materiel should adhere to DoD Instruction 4140.67.  In addition, cybersecurity measures that include identifying cyber risks and mitigation strategies should adhere to DoD Directive-type Memorandum (DTM) 17-001.

## 6.7 Subject term (key word) listing.

Delay, arming

Explosive ordnance disposal

Explosive train

Explosive train interruption

Fail-safe

Function, premature

Fuzing system

Non-interrupted explosive train

Safe separation

Safety and arming device

## MIL-STD-1316F

- 6.8 International standardization agreements.  Certain provisions of this standard are the subject of International Standardization Agreement STANAG 4187, Fuzing Systems, Safety Design Requirements.  When change notice, revision, or cancellation of this document is proposed which affect or violate the international agreement concerned, the preparing activity will take appropriate reconciliation action through international standardization channels, including departmental standardization offices, if required.
- 6.9 Changes from previous issue.  Marginal notations are not used in this revision to identify changes with respect to the previous issue due to the extensiveness of the changes.

Custodians:                                                                 Preparing activity: Army-AR                                                                     Army-AR Navy-OS                                                                    (Project  13GP-2017-001)

Air Force-11

Review activities: Army-AV, TE Navy-AS, MC Air Force-70, 170