<!-- page 1 of 31 -->

MIL-HDBK-217F

## 3.0 INTRODUCTION

3.3 Limitatlons of Reilability Predictions - This handbook provides a common basis for reliability predictions, based on analysis of the best available data at the time of issue. It is intended to make reliability prediction as good a tool as possible. However, like any tool, reliability prediction must be used intelligently, with due consideration of its limitations.

The first limitation is that the failure rate models are point estimates which are based on available data. Hence, they are valid for the conditions under which the data was obtained, and for the devices covered. Some extrapolation during model development is possible, but the inherently empirical nature of the modeis can be severeiy restrictive. For exampie, none oí the modeis in this handbook predict nuciear survivability or the effects of ionizing radiation.

Even when used in similar environments, the differences between system applications can be significant. Predicted and achleved rellabity have aiways been coser for ground electronic systems than for avionic systems, because the envirormental stresses vary less from system to system on the ground and hence the fleld conditions are in general closer to the environment under which the data was collected for the prediction model. However, failure rates are also impacted by operational scenarios, operator characteristics, maimtenance practices, measurement techniques and differences in detinition of talture. Hence, a rellability prediction should never be assumed to represent the expected field rellabllity as measured by the user (i.e., Mean-Time-Between-Maintenance, Mean-Time-Between-Removals, etc.). This does not negate its value as a reliability engineering tool; note that none of the applications discussed above requires the predicted reliability to match the fieid measurement.

Electronic technology is noted for its dynamic nature. New types of devices and new processes are continually introduced, compounding the difficulties of predicting reliability. Evolutionary changes may be handled by extrapolation from the existing models; revolutionary changes may defy analysis

Another limitation of reliabiltty predictions Is the mechanlcs of the process. The part stress analysis method requires a signlficant amount of design detall. This naturalty imposes a time and cost penalty. More significantly, mary of the details are not avaitable in the earty design stages. For this reason this handbook contains both the part stress analysls method (Sections5 through23) and a simpler parts count method (Appendix A) which can be used in earty design and bid forrnulation stages.

Finally, a basic limitation of reliability prediction is its dependence on correct application by the user. Those who correctly apply the models and use the information in a conscientious reliability program will find the prediction a useful tool. Those who view the prediction only as a number which must exceed a specified value can usually find a way to achieve their goal without any impact on the system.

## 3.4 Part Stress Analysis Prediction

3.4.1 Appiicabiity - This method is appiicabie when most of the design is completed and a detailed parts list including part stresses Is avallable. It can also be used during later design phases tor reliability trade-offs vs. part selection and stresses. Sections 5 through 23 contain failure rate models for a broad variety of parts used in etectronic equipment. The parts are grouped by major categorles and, where appropriate, are subgrouped within categories. For mechanical and electromechanical parts not covered by this Handbook, refer to Bibllography items 20 and 36 (Appendix C).

The failure rates presented apply to equipment under normnal operating conditions, i.e., with power on and performing Its intended functions in lts intended environment. Extrapolation of any of the base failure rate models beyond the tabulated values such as high or sub-zero temperature, electrical stress values above 1.0, or extrapolation of any associated model modifiers is completely invalid. Base fallure rates can be interpolated between electrical stress values from 0 to 1 using the undertying equations.

The general procedure for determining a board level (or system level) failure rate is to sum individually calculated failure rates for each component. This summation is then added to a failure rate for the circuit board (which inctudes the effects of soldering parts to it) using Section 16, Interconnection Assemblies.

3-2

<!-- page 2 of 31 -->

3.0 INTRODUCTION

MIL-HDBK-217F

For parts or wires soldered together (e.g., a jumper wire between two parts), the connections model appearing in Section 17 is used. Finally, the effects of connecting circuit boards together is accounted for by adding in a failure rate for each connector (Section 15, Connectors). The wire between connectors is assumed to have a zero failure rate. For various service use profiles, duty cycles and redundancies the procedures described in MIL-STD-756, Reliability Modeling and Prediction, should be used to determine an effective system level failure rate.

3.4.2 Part Quality - The qualty of a part has a direct effect on the part failure rate and appears In the part models as a factor, πQ. Mañy parts are covered by speclfications that have several quality levels, hence, the part models have values of πo that are keyed to these quality levels. Such parts with their quality designators are shown in Table 3-1. The detailed requirements for these levels are clearty defined in the applicable specification, except for microcircuits. Microcircuits have quality levels which are dependent on the number of Mil-STD-883 screens (or equivalent) to which they are subjected.

Table 3-1: Parts With Muttl-Level Quallty Speclficatlons

```
                  Part                                          Quality Designators
                                                  S, B, B-1, Other: Quality Judged by
Microcircuits                                      Screening Level
Discrete Semiconductors                           JANTXV, JANTX, JAN
Capacitors, Established                           D, C, S, R, B, P, M, L
 Reliability (ER)
Resistors, Established                            S, R, P, M
 Reliablity (ER)
Coils, Molded, R.F.,                              S, R, P, M
 Reliabiity (ER)
Reiays, Estabiished                               R, P, M, L
 Reliability (ER)
```

Some parts are covered by older specifications, usually referred to as Nonestablished Reliability (Non-ER). that do not have multi-levels of guality. These part modeis generaily have two quaiiiy leveis designated as "MIL-SPEC.", and "Lower". if the part is procured in complete accordance with the applicable specification, the πo value for MIL-ŚPEC should be used. If any requirements are waived, or if a commercia! part is procured, the πo value for Lower should be used.

The foregoing discussion involves the "as procured" part quality. Poor equipment design, production, and testing facilities can degrade part quality. The use of the higher quality parts requires a total equipment design and guality control process commensurate with the high part quality. t would make little sense to procure high guality parts only to have the equipment production procedures damage the parts or introduce latent defects. Total equipment program descriptions as they might vary with different part quality mixes is beyond the scope of this Handbook. Reliability management and quality control procedures are described in other DoD standards and publications. Nevērtheless, when a proposed equipment development is pushing the state-of-the-art and has a high reliability requirement necessitating high quality parts, the total equipment program should be given careful scrutiny and not just

3-3

<!-- page 3 of 31 -->

MIL-HDBK-217F

## 3.0 INTRODUCTION

the parts quality. Otherwise, the low failure rates as predicted by the models for high quality parts will not be realized.

3.4.3 Use Environment - Al part reliability models include the etfects of environmental stresses through the environmentai iactor, πe, except ior tne eifecis of ionizing radiation. Tne descripions oi these environments are shown in Table 3-2. The x factor is quantified within each part failure rate model. These environments encompass the major areas of equipment use. Some equipment will experience more than one environment during its normal use, e.g., equipment in spacecraft. In such a case, the reliability analysis should be segmented, namely, missile launch (M) conditions during boost into and retum from orbit, and space flight (SF) whlle in orblt.

Table 3-2: Environmental Symbol and Description

```
                                            Equtvatent
                                         MIL-HDBK-217E.
                                             Notice 1
   Environment           E Symbol
                                           πE Symboi                        Description
                                             GB
Ground, Benign              GB
                                                            Nonmobile, temperature and humidity
                                                            controlled environments readily accessible to
                                             GMS
                                                            maintenance; inciudes iaboratory instruments
                                                            and test equipment, medical electronic
                                                            equipment, business and scientific computer
                                                            complexes, and missiles and support
                                                            equipment in ground silos.
Ground, Fixed               GF               GF             Moderately controlled environments such as
                                                            installation in permanent racks with adequate
                                                            cooling air and possible installation in unheated
                                                            buildings; includes permanent installation of air
                                                            traffic control radar and communications
                                                            facilities.
Ground, Mobile              GM               GM             Equipment installed on wheeled or tracked
                                             Mp            vehicles and equipment manually transported;
                                                            includes tactical missile ground support
                                                           equipment, mobile communication equipment,
                                                           tactical fire direction systems, handneid
                                                           communications equipment, laser designations
                                                            and range finders.
Naval, Sheltered           Ns               Ns             Includes sheltered or below deck conditions on
                                                           surface ships and equipment installed in
                                            NSB            submarines.
Naval, Unshetered           NU               NU            Unprotected surtace shipborne equipment
                                            NW             exposed to weather conditions and equipment
                                                           immorsed in salt water. Includes sonar
                                            NH             equipment and equipment installed on hydrotoil
                                                           vessels.
```

3-4

<!-- page 4 of 31 -->

MIL-HDBK-217F

3.0 INTRODUCTION

Table3-2: Envtronmental Symbol and Descriptlon (cont'd)

```
                                           Equivajent
                                        MIL-HDBK-217E.
                                            Notice 1
   Environment                             "E Symbol                        Description
                        πE Symbol
Airborne, Inhabited,        AiC              AIC           Typical conditions in cargo compartments
Cargo                                       ATT            which can be occupied by an aircrew.
                                                           Environment extremes of pressure.
                                            AIB            temperature, shock and vibration sre minimal.
                                                           Examples inctude long mission aircraft such as
                                                           the C130, C5, B52, and C141. This category
                                                           aleo applies to inhabited areae in kower
                                                           performance smaller aircraft such as the T38.
Airborne, Inhabited,        AIF             AIF            Same as AC but installed on high performance
Fighter                                     AIA            aircraft such as fighters and interceptors.
                                                           Examples include the F15, F16, F111, F/A 18
                                                           and Àiôaircra.
Airborne, Uninhabited,     AUC              AUC            Environmentally uncontrolied areas which
Cargo                                       AUT            cannot be inhabited by an aircrew during flight.
                                                           Environmental extremes of pressure,
                                            AUB            temperature and shock may be severe.
                                                           Examples indude uninhabited areas of long
                                                           mission aircraft such as the C130, C5, B52 and
                                                           C141. This category also applies to
                                                           uninhabited area oi iower periormance smaïier
                                                           aircraft such as the T38.
Airborne,                  AUF              AUF            Same as AuC but installed on high pertormance
Uninhabited,                                AUA            aircraft such as fighters and interceptors.
Fighter                                                    Examples include the F15, F16, F111 and A10
                                                           aircrañ.
Airborne, Rotary           ARW              ARW            Equipment installed on helicopters. Applies to
Winged                                                     both internally and externally mounted
                                                           equipment such as laser designators, fire
                                                           control systems, and communications
                                                           equipment.
Space, Fiight               SF              SF             Earh orbüai. Approaches benign ground
                                                           conditions. Vehice neither under powered
                                                           flight nor in atmospheric reentry; includes
                                                           sateiiites and shuitties.
```

3-5

<!-- page 5 of 31 -->

MIL-HDBK-217F

3.0 INTRODUCTION

Tabie 3-2: Environmental Symbol and Descriptlon (cont'd)

```
                                           Equivalent
                                        MIL-HDBK-217E,
  Environment                               Notice 1
                                          πE Symbol                       Description
                        πE Symbol
Missile, Flight             MF              M/F           Conditions reiated to powered füght of air
                                            MFA           breathing missiles, cruise missiles, and
                                                          missiles in unpowered free flight.
Missile, Launch             M               M             Severe conditions related to missile launch (air,
                                            USL           ground and sea), space vehicle boost into
                                                          orbit, and vehicle re-entry and landing by
                                                          parachute. Also applies to solid rocket motor
                                                          propulslon powered flight, and torpedo and
                                                          missile launch from submarines.
Cannon, Launch              CL              CL            Extremely sévēre conditions related to cannon
                                                          launching of 155 mm. and 5 inch guided
                                                          projectiles. Conditions apply to the projectile
                                                          trom launch to target impact.
```

3.4.4 Part Fallure Rate Models- Part failure rate models for microelectronic parts are significantly different from those for other parts and are presented entirely in Section 5.0. A typical example of the type of model used for most other part types is the following one for discrete semiconductors:

![Formula block](doc:660ab37/tier:flash/page:5/block:6)

where:

2p is the part failure rate,

\~p is the base failure rate usually expressed by a model relating the influence of electrical and temperature stresses on the part,

πE and the other π factors modify the base failure rate for the category of environmental application and other parameters that affect the part reliability.

The π and πo factors are used in most all models and other π factors apply only to specific models. The applicabillty of π factors is identified in each section.

The base failure rate (λ) models are presented in each part section along with identification of the applicable model factors. Tables of calculated λvalues are also provided for use in manual calculations. The model eguations can, of course, be incorporated into computer programs for machine processing. The tabulated values of λ are cut off at the part ratings with regard to temperature and stress, hence, use of parts beyond these cut off points will overstress the part. The use of the λn models in a computer

3-6

<!-- page 6 of 31 -->

3.0 INTRODUCTION

MIL-HDBK-217F

program should take the part rating limits into account. The λ equations are mathematically continuous beyond the part ratings but such failure rate values are invalid in the overstressed regions.

Al the part models include failure data from both catastrophic and permanent drift failures (e.g., a resistor permanently falling out of rated tolerance bounds) and are based upon a constant failure rate, except for motors which show an increasing failure rate over time. Failures associated with connection of parts into circuit assemblies are not included within the part failure rate models. Information on connection reliability is provided in Sections 16 and 17.

3.4.5 Thermal Aspects - The use of this prediction method requires the determination of the temperatures to which the parts are subjecied. Since paris reliabiity is sensitive to temperature, the thermal analysis of any design should fairly accurately provide the ambient temperatures needed In using the part models. Of course, lower temperatures produce better reliability but also can produce increased penatties in terms of added loads on the environmental control system, unless achleved through improved thermal design of the equipment. The thermai analysis shouid be part of the design process and included in all the trade-off studies covering equipment pertormance, reliability, weight, volume, environmental control systems, etc. References 17 and 34 listed in Appendix C may be used as guides in determining component temperatures.

3-7

<!-- page 7 of 31 -->

MIL-HDBK-217F

4.0 RELIABILITY ANALYSIS EVALUATION

Tabie 4-1 provides a generai checkiist io be used as a quida for evaiuating a reliability prediction report. For completeness, the checklist Includes categories tor reliablility modeling and allocation, which are sometimes delivered as part of a prediction report. It should be noted that the scope of any reliability analysis depends on the specific reguirements called out in a statement-of-work (SOw) or system specification. The inclusion of this checklist is not intended to change the scope of these reguirements.

Table 4-1: Rellabllity Analysis Checklist

```
                Major Concerns                                               Comments
MODELS
     Are all functional elements incuded in the        System design drawings/diagrams must be reviewed to
     reliabitity block diagram /model?                 be sure that the reliability model/diagram agrees with the
                                                       hardware.
     Are all modes of operation considered in the      Duty cycles, alternate paths, degraded conditions and
     math model?                                       redundant units must be detined and modeled.
     Do the math model results show that the design    Unit failure rates and redundancy equations are used
     achieves the reliability requirement?             from the detaiied part predictions in the system math
                                                       model (See MIL-STD-756, Reliability Prediction and
                                                       Modeling).
ALLOCATION
     Are system reliability requirements allocated     Useful levels are defined as: equipment for
     (subdivided)to useful levels?                     subcontractors, assemblies for sub-subcontractors,
                                                       circuï boards for designers.
     Does the allocation process consider              Conservative values are needed to prevent reallocation
     compiexity, design fiexibiity, and safety         aiēvēry dēsign changē.
    margins?
PREDICTIÔN
     Does the sum of the parts equal the value of      Many predictions neglect to include all the parts producing
     the module or unit?                               optimistic results (check for solder connections,
                                                       connectors, circuit boards).
    Are environmental conditions and part quality      Optimistic quality levels and favorable environmental
     representative of the requirements?               conditions are often assumed causing optimistic results.
     Are the circuit and part temperatures defined     Temperature is the biggest driver of part failure rates;
    and do they represent the design?                  low temperature assumptions will cause optimistic
                                                       results.
    Are equipment, assembly, subassembly and          Identification is needed so that corrective actions for
    part reliability drivers identified?              reliability improvement can be considered.
    Are aternate (Non MIL-HDBK-217) failure rates     Use of altemate failure rates, if deemed necessary,
    highiighted aiong with the rationale for their    require submission of backup data to provide credence in
    use?                                              the vatues.
                                                      Each component type should be sampled and failure
    Is the level of detail for the part failure rate  rates completely reconstructed for accuracy.
    models sufficient to reconstruct the result?
                                                      Prediction methods for advanced technology parts should
    Are critical components such as VHSIC,            be carefully evaluated for impact on the module and
    Monolithic Microwave Integrated Circuits          system.
    (MMIC), Application Specific Integrated
    Circuits (ASIC) or Hybrids highlighted?
```

4-1

<!-- page 8 of 31 -->

MIL-HDBK-217F

5.0 MICROCIRCUITS, INTRODUCTION

This section presents failure rate prediction modeis for the following ten major classes of microelectronic devices:

Seciion

5.1 Monolithic Bipolar Digital and Linear Gate/Logic Array Devices

5.1 Monolithic MOS Digital and Linear Gate/Logic Array Devices

5.1 Monolithic Bipoiar and MOS Digital Microprocessor Devices

5.2 Monolithic Bipolar and MOS Memory Devices

5.3 Very High Speed integrated Circuit (VHSiC/VHSiC-Like and VLSi) CMOS Devices (>60K Gates)

5.4 Monolithic GaAs Digital Devices

5.4 Monolithic GaAs MMIC

5.5 Hybrid Microcircuits

5.6 Surface Acoustic Wave Devices

5.7 Magnetic Bubble Memories

in the title description of each monolithic device type, Bipolar represents all TTL, ASTTL, DTL, ECL, CML, ALSTTL, HTTL, FTTL, F, LTTL, STTL, BiCMOS, LSTTL, iiL, ³L and ISL devices. MOS represents all metal-oxide microcircuits, which Includes NMOS, PMOS, CMOS and MNOS fabricated on various substrates such as sapphire, polycrystalline or single crystal silicon. The hybrid model is structured to accommodate all of the monolithic chip device types and various complexity levels.

Monolithic memory complexity factors are expressed in the number of bits in accordance with JEDEC STD 21A. This standard, which is used by all govemment and industry agencies that deal with microcircuit memories, states that memories of 1024 bits and greater shall be expressed as K bits, where 1K = 1024 bis. For exampie, a 16K memory has 16,384 bis, a 64K mémory has 65,536 bits and à 1M memory has 1,048,576 bits. Exact numbers of bits are not used for memories of 1024 bits and greater.

For devices having both linear and digital functions not covered by MIL-M-38510 or MIL-l-38535, use the iinear modei. Line drivers and iine receivers are considered iinear devices. For linear devices not covered by MIL-M-38510 or MIL-l-38535, use the transistor count from the schematic diagram of the device to determine circuit complexity.

For digtal devices not covered by MIL-M-38510 or MIL-I-38535, use the gate count as determined from the logic diagram. A J-K or R-S flip flop is equivalent to 6 gates when used as part of an LSi circuit. For the purpose of this Handbook, a gate is considered to be any one of the following functions; AND, OR, exclusive OR, NAND, NOR and inverter. When a logic diagram is unavailable, use device transistor count to determine gate count using the following expressions:

Technoloay

Gate Approximation

Bipolar

No. Gates = No. Transistors/3.0

CMOS

No. Gates = No. Transistors/4.0

All other MOS except CMOS

No. Gates = No. Transistors/3.0

5-1

<!-- page 9 of 31 -->

MIL-HDBK-217F

5.0 MICROCIRCUITS, INTRODUCTION

A detailed form of the Section 5.3 VHSiC/VHSiC-Like model is included as Appendix B to allow more detailed trade-offs to be pertormed. Reference 30 should be consulted for more information about this model.

Reference 32 should be consulted for more Information about the models appearing in Sections 5.1, 5.2, 5.4, 5.5, and 5.6. Reference 13 should be consulted for additional information on Section 5.7.

5-2

<!-- page 10 of 31 -->

MIL-HDBK-217F

## 5.1 MICROCIRCUITS, GATE/LOGIC ARRAYS AND MICROPROCESSORS

## DESCRIPTION

1. Bipolar Devices, Digital and Linear Gate/Logic Arrays

2. MOS Devices, Digttal and Linear Gate/Logic Arrays

3. Field Programmable Logic Array (PLA) and

Programmable Array Logic (PAL)

4. Microprocessors

![Formula block](doc:660ab37/tier:flash/page:10/block:9)

Bipolar Digital and Linear Gate/Logic Array Die Complexity Failure Rate - C,

```
          Digital                  Linear                  PLA/PAL
     No. Gates     C1       No. Transistors C1         No. Gates     C1
    1  to   100    .0025     1 to    100    .010        Up to 200    .010
   101 to 1,000    .0050   101
                              to    300     .020      201 to 1,000   .021
 1,001 to 3,000    .010    301 to  1,000    .040    1,001 to 5,000   .042
 3,001 to 10,000   .020   1,001
 10,001 to 30,000  .040       to  10,000    .060
30,001 to 60,000   .080
```

MOS Digital and Linear Gate/Logic Array Die Complexlty Failture Rate - C,

```
          Digital                   Linear                  PLA/PAL
     No. Gates      C{1      No. Transistors C1         No. Gates      C1
    1  to   100    .010       1 to   100     .010        Up to 500    .00085
   101 to 1,000    .020     101 to   300     .020      501 to 1,000   .0017
 1,001 to 3,000    .040     301 to  1,000    .040     2,001 to 5,000  .0034
 3,001 to 10,000   .080    1,001 to 10,000   .060    5,001 to 20,000  .0068
 10,001 to 30,000  .16
       to 60,000   .29
30,001
```

\*NOTE: For CMOS gate counts above 60,000 use the VHSIC/VHSIC-Like model in Section 5.3

Die Complexity Failure Rate - C1

```
 No. Bits   Bipolar     MOS
             C{1        C1
Up to 8      .060       .14
Up to 16     .12        .28
Up to 32     .24        .56
```

All Other Model Parameters

```
Parameter             Refer to
  πT               Section 5.8
  C2               Section 5.9
 πE，πQ             Section 5.10
```

5-3

<!-- page 11 of 31 -->

MIL-HDBK-217F

5.2 MICROCIRCUITS, MEMORIES

## DESCRIPTION

1. Read Onty Memories (ROM)

2. Programmable Read Only Memories (PROM)

3. Ultraviolet Eraseable PRÓMs (UVEPROM)

4. "Flash," MNOS and Floating Gate Electrically Eraseable PROMs (EEPROM). Inctudes both floating gate tunnel oxide (FLOTOX) and textured polysilicon type EEPROMs

5. Static Random Access Memorles (SRAM)

6. Dynamic Random Access Memories (DRÁM)

λp = (C₁ πT +C2 πE +λcyc) πOπL Failures/106 Hours

Die Complexity Failure Rate - C1

```
                                      MOS                         Bipolar
                               PROM,                SRAM
                               UVEPROM,            (MOS &     ROM,
  Memory Size, B (Bits) ROM    EEPROM,    DRAM     BiMOS)     PROM     SRAM
                               EAPROM
Up to 16K              .00065   .00085    .0013     .0078    .0094     .0052
 16K < B ≤ 64K         .0013    .0017     .0025     .016     .019      .011
 64K < B ≤ 256K        .0026    .0034     .0050     .031     .038      .021
 256K < B ≤ 1M         .0052    .0068     .010      .062     .075      .042
```

Aq Factor for λçyc Calculation

```
  Total No. of
  Programming            Textured-
  Cycles Over  Flotox1    Poly2
EEPROM Life, C
Up to 100       .00070     .0097
100 < C ≤ 200   .0014      .014
200<C≤ 500      .0034      .023
500 < C ≤ 1K    .0068      .033
1K<C≤3K         .020       .061
3K<C≤7K         .049       .14
7K<C≤15K        .10        .30
15K < C ≤ 20K   .14       .30
20K < C ≤ 30K   .20       .30
30K < C≤ 100K   .68       .30
100K<C≤200K    1.3        .30
200K < C ≤ 400K 2.7       .30
400K < C ≤ 500K 3.4        .30
   1. A1 = 6.817 x 10-6 (C)
  2. No underlying equation for Textured-
     Poly.
```

A2 Factor for λcvc Calculation

```
Total No. of Programming
 Cycles Over EEPROM    Textured-Poly A2
       Life, C
 Up to 300K                   0
 300K < C ≤ 400K             1.1
 400K < C ≤ 500K             2.3
```

All Other Model Parameters

```
    Parameter           Refer to
πT                   Section 5.8
C2                   Section 5.9
πE,πQ.πL             Section 5.10
λcyc (EEPROMS        Page 5-5
    oniy)
AcyC  0  For all other devices
```

5-4

<!-- page 12 of 31 -->

MIL-HDBK-217F

5.2 MICROCIRCUITS, MEMORIES

EEPROM ReadWrite Cycing induced Faiture Rate - λcvc

```
                                                          λcyc=0
   All Memory Devices Except Flotox and
   Textured-Poly EEPROMS
                                                              A2B2
   Flotox and Textured Poly EEPROMS            λcyc =1 A1B1+        πECC
                                                               TQ
   Modei Eacior                  Eiotox                     Textured-Poiy
      A1                        Page 5-4                     Page 5-4
      B1                        Page 5-6                     Page 5-6
      A2                        A2=0                         Page 5-5
      B2                        B2=0                         Page 5-6
      πQ                        Section 5.10                 Section 5.10
Error Correction Code (ECC) Options:
   1. No On-Chip ECC            πECC = 1.0                   πECC = 1.0
   2. On-Chip Hamming Code      πECC =.72                    πECC = .72
   3. Two-Needs-One             πECC = .68                   πECC =.68
      Redundant Cell Approach
   NOTES:    1.
                See Reference 24 tor modeling off-chip error detection and correction
                schemes at tne memory sysiem ievei.
             2. If EEPROM type is unknown, assume Flotox.
             3. Eror Correction Code Options: Some EEPROM manufacturers have incorporated
                on-chip error correction circuitry into their EEPROM devices. This is represented by
                the on-chip hamming code entry. Other manufacturers have taken a redundant cell
                approach which incorporates an extra storage transistor in every memory cell. This
                is represented by the two-needs-one redundant ceii entry.
                The A and A factors shown in Section 5.2 were developed based on an assumed
             4.
                system life of 10,000 operating hours. For EEPROMs used in systems with
                significantly longer or shorter expected lifetimes the A, and A,factors should be
                multiplied by:
                                       10,000
                           System LifetimeOperating Hours
```

5-5

<!-- page 13 of 31 -->

MIL-HDBK-217F

5.2 MICROCIRCUITS, MEMORIES

```
   M     0 13 7        2            0775270 8 5 8 2 0 58
       2    18  5 4 3 3 2
         2 1    1 1  1 1 1 1 1
                                                        -18
   256K
                   96 87
                                       850
                       8    72   6  575
                                            40 44
       5 4 3 3                                   42
         1  1 2  1.0
         10         05255454754亿433354333329
   64K    95 89 84
              80 5722
                   969
                                                        (.63x 1.5
                             35
                                          23
   16K
                              33
                 50 4
              0.56
                                      02
                                       0.27 20
             0.59
                    45 7 40 3 3
                                32 30 2
                                            24 2 2 22 21 0.21
       0.76
        0.71 0.7 3
            0.  0. 0 0 0. 0. 0 0. 0 0 0. 0 0 0 0. 0. 0 0 0. 0 0 0 0 .122
                                              16
                                                 15
         0 47 45 42 40 38          2               15
                                             16
                                                15
                                23 22 20  18
                                           77
                 36    29
                        28 27
                              22
                           28 25
                                                        dx0
                                                25
                                              79
   M                                   65    76
        20                                         8  25
           2
              27
                 30 2 4 36
                       38 40
                           45
                             47 5.0
                                25 7 60
                   3 3          5. 55 262 71 7  8
          22
             25
                20
                          43
                                                        640
   256K
       3 14                                            8
                                       46
                 22                      48 0 2 4 6 8 3
               20
                 1 3 4 6 7 6 0 2 4 5 7 6 42
                                      4
          15
           16
             18
              19
                                3 3       5
                                             555
                                                 6. 6.
                          3333
                                           5
                    2 2 2 2
                                                         I
   64K
                        2022     8   23  4 87 6  3
          1  3            2 3 2                    45
        10    13 14
                 15
                   16
                    17
                     18
                       19
                              5 6 22
                                   9 3333
                                    0     33
                                               0 2
                             4 22
                                             3
                                              4.
             1                                  4 4     2
        17
           82              16    19
       66
   16K
                 1 1 2 13 14 15 7 10
                                19 0 1 23 4
                                          5
                   1 1             2       87   9 0
                                    222
                                                 3
                                              22
                                                   3
                                          22
                                        2
                                             2
           58 67
   K         2   76 86 96
       47 50
          54
                   81 66 0 二
                                      1.6 0.
                                           四.
                             12
                                13  15
                                          1 1 19 0
                              13
                           11
                                              222  2
                                                         18    18
   M   3
          27 3 8 0 6 3       14
        8
        455667
                                                        1++23
                 8
                  8 9 10
                       二 12 12 13 151617
                                  18 19 20 21 2 23 2 25 27 292931
   256K
                       5  2
                              75 80 95  1
           92 47 1 4
                    47
       2 47
                     51
                            7 1
                           6.
                 4        8.          10 二 212 13 14 14 15
Fo1 ()
       222
           23
              33
                                                   15
                                                               (.63 1.5
                                                        (.631.5
                                       E.
                                   5 5.0 56
   64K
                                 2
                                       5  58 4. 71
                              38
          13 11
             16
              17
                19
                 20
                   22
                    24
                     25
                       27
                        29
                          31
                           33
                             35
                                10
        12
                                             8.  7     155     一
           0.72
             0.79
              0.8.6
          06.6
       0.5
        0..0
                0.3 1.0
   16K
                           17 1.9
                  11
                     13 14 15
                          16
                                20    5   9     5  39
                    12
                                       6 2.
                                         8 233333
                                             2 4
                                    22
                                 2
                                   2
                                       2
                                                        dxe    dxe
               4
             40 43
          3
           38
                             9  10 1 2        17
        30
                    59
                          78
                           3
                      63 8 73
                 51 55
       27
                                       3 二
                                           15
                                       1     1        5        25
                                          2
                                      3
                                                               60009
                                                         160
   e y Sihs)
                                                        8      B
                                                         I
       2505055050575050901015 05303101550157075
     ()
                                                               3
```

Balai  o i  i lon

5-6

<!-- page 14 of 31 -->

MIL-HDBK-217F

5.3 MICROCIRCUITS, VHSIC/VHSIC-LIKE AND VLSI CMOS

DESCRIPTION CMOS greater than 60,000 gates

![Formula block](doc:660ab37/tier:flash/page:14/block:4)

Die Base Faiture Rate - λBD

```
Part Type                  ABD
Logic and Custom           0.16
Gate Array                 0.24
```

Manutacturing Process Correction Faotor - πMFG

All Other Model Parameters

```
Parameter               Refer to
  T                  Section 5.8
 πE, πQ              Section 5.10
```

```
Maruiacturing Process      TMFG
QML or QPL                 .55
Non QML or Non QPL         2.0
```

Package Type Correction Factor - πpT

```
                      πPT
Package Type  Hermetic Nonhermetic
DIP             1.0       1.3
Pin Grid Array  2.2       2.9
Chip Carrier    4.7       6.1
 (Surface Mount
 Technology)
```

Die Complexity Correction Factor - πCD

```
Feature Size                     Die Area (cm²)
 (Microns)   A≤.4       .4<A≤.7   .7<A≤1.0    1.0 < A≤ 2.0 2.0 < A ≤ 3.0
   .80         8.0       14          19         38          58
  1.00        5.2         8.9        13         25          37
  1.25        3.5         5.8         8.2       16          24
"CD   A   2
     21     2 (.64) +.36 A = Total Scribed Chip Die Area in cm² Xg - Feature Size (microns)
         xs
Die Area Conversion: cm²
                - MIL2+155,000
```

```
   Package Base Failure Rate - ^BP
  Number of Pins           λBP
        24                 .0026
        28                 .0027
       40                  .0029
       44                  .0030
       48                  .0030
       52                  .0031
       64                  .0033
       84                  .0036
      120                  .0043
      124                  .0043
      144                  .0047
      220                  .0060
       .0022 + ((1.72 x 10-5) (NP))
λBP
NP      Number of Package Pins
```

```
  Electricai Ôverstress Failure Rate - λEOS
 VTH (ESD Susceptibility (Volts))* λEOS
            0 - 1000              .065
        > 1000 - 2000             .053
        > 2000 - 4000             .044
       > 4000 - 16000             .029
            > 16000               .0027
λEOS = (-in (1 - .00057 exp(- .0002 VTH)) /.00876
VTH = ESD Susceptibility (volts)
  Voltage ranges which will cause the part to
  fail. If unknown, use 0 - 1000 volts.
```

<!-- page 15 of 31 -->

MIL-HDBK-217F

5.4 MICROCIRCUITS, GaAS MMIC AND DIGITAL DEVICES

## DESCRIPTION

Gallium Arsenide Microwave Monolithic Integrated Circuit (GaAs MMIC) and GaAs Digital Integrated Circults using MESFET Transistors and Gold Based Metallization

λp =[C1xTπA + C2πE]πLπQFallures/106 Hours

MMIC: Die Complexity Failure Rates - C1

```
     Complexity             C1
  (No. of Elements)
       1 to 100             4.5
   101 to 1000              7.2
1. C1 accounts for the following active
   elements: transistors, diodes.
```

Device Application Factor - πA

```
          Application          XA
MMIC Devices
 Low Noise & Low Power (≤ 100 mW) 1.0
 Drtver & High Power (> 100 mW) 3.0
 Unknown                       3.0
Digital Devices
 All DigitalApplications       1.0
```

Digital: Die Complexity Faiture Rates - C1

```
      Complexity               C1
    (No. of Elements)
         1 to 1000             25
   1,001 to 10,000             51
  C. aċcounts for the following activē
1.
   elements: transistors, diodes.
```

All Other Model Parameters

```
 Parameter             Refer to
 πT                 Section 5.8
C2                  Section 5.9
 "E·LTQ             Section 5.10
```

5-8

<!-- page 16 of 31 -->

MIL-HDBK-217F

5.5 MICROCIRCUITS, HYBRIDS

## DESCRIPTION Hybrid Microcircuits

![Formula block](doc:660ab37/tier:flash/page:16/block:4)

Nc π Number of Each Particular Component

= Failure Rate of Each Particular Component

The general procedure for developing an overall hybrid failure rate is to calculate an individual failure rate for each component type used in the hybrid and then sum them. This summation is then modtfied to accoun tor the overail hybrid tunction (xf), screening levei (πo), and maturity (π). The hybrid package tailure rate is a function of the active component failure modifiod by the environmental factor (i.e., (1 + .2 πE)). Only the component types listed in the following table are considered to contribute signtficantty to the overall failure rate of most hybrids. All other component types (e.g., resistors, inductors, etc.) are considered to contribute insignfficantly to the overall hybrid fallure rate, and are assumed to have a fallure rate of zero. This simplification is valid for most hybrids; however, if the hybrid consists of mostly passive components then a failure rate shouid be caicuiated for these devices. i factoring in other component types, assume πQ = 1, πE =1 and TA = Hybrid Case Temperature for these calculations.

Determination of λ

```
   Determine λfor These      Handbook Section    Make These Assumptions When Determining
     Component Types                                               2c
  Microcircuits                     5           C2 = 0, πQ = 1, πL = 1, Tj as Determined from
                                                Section 5.12, λBp = 0 (for VHSIC).
  DiscreteSemiconductors             6         πQ = 1, Tas Determined from Šection 6.14,
                                               πE=1.
  Capacitors                       10          πQ = 1, TA = Hybrid Case Temperature,
                                               πE=1.
NOTE:     If maximum rated stress for a die is unknown, assume the same as for a discretely package
          die of the same type. If the same die has several ratings based on the discrete packaged
          type, assume the lowest rating. Power rating used should be based on case temperature
          for discrete semiconcuctors.
```

Circuit Function Factor - πF

```
     Circuit Type         πF
Digital                   1.0
Video, 10 MiHz < f < 1 GHz 1.2
Microwave, f > 1 GHz     2.6
Linear, f < 10 MHz       5.8
Power                   21
```

Alt Other Hybrd Mode! Parameters

```
πL，πQ·πE       Refer to Section 5.10
```

5-9

<!-- page 17 of 31 -->

MIL-HDBK-217F

## 5.6 MICROCIRCUITS, SAW DEVICES

## DESCRIPTION Surface Acoustic Wave Devices

## λp = 2.1 πQ πE Failures/106 Hours

Quality Factor - πO

```
Screening Level                     πQ
10 Temperature Cycles (-55C to       .10
+125°C) with end point electrical
tests at temperature extremes.
None beyond best commerical        1.0
practices.
```

Environmental Factor - xE

```
Environment        πE
    GB             .5
    GF            2.0
   GM             4.0
    NS            4.0
    NU            6.0
    AIC           4.0
    AIF           5.0
    AUC           5.0
    AUF           8.0
    ARW           8.0
    SF             .50
    MF            5.0
    ML           12
    CL          220
```

5-10

<!-- page 18 of 31 -->

MIL-HDBK-217F

5.7 MICROCIRCUITS, MAGNETIC BUBBLE MEMORIES

The magnetic bubbie memory device in its present form is a non-hermetic assembly consisting of the following two major structural segments:

1. A basic bubble chip or die consisting of memory or a storage area (e.g., an array of minor loops), and required control and detection elements (e.g., generators, various gates and detectors).

A magnetic structure to provide controlled magnetic fields consisting of permanent magnets, coils, and a housing.

These two structura! segments of the device are interconnected by a mechanica! substrate and lead frame. The interconnect substrate in the present technology is normally a printed circuit board. It should be noted that this model does not include extemal support microelectronic devices required for magnetic bubbie memory operation. The modei is based on Reierence 33. The generai form oi the faiiure rate model is:

![Formula block](doc:660ab37/tier:flash/page:18/block:7)

where:

λ,= Failure Rate of the Control and Detection Structure

![Formula block](doc:660ab37/tier:flash/page:18/block:10)

λ2 = Failure Rate of the Memory Storage Area

![Formula block](doc:660ab37/tier:flash/page:18/block:12)

![Formula block](doc:660ab37/tier:flash/page:18/block:13)

Device Complexity Failure Rates for Control and Detection Structure - C11 and C21

![Formula block](doc:660ab37/tier:flash/page:18/block:15)

```txt
NC Number of Bubble Chips per
Packaged Device
Temperature Factor - πT
-Ea 1 298
πT = (.1) exp 8.63 × 10-5 Tj+ 273
Use:
Ea .8 to Calculate πT1
Ea .55 to Calculate πT2
TJ = Junction Temperature (°C),
25≤Tj≤175
TJ = TCASE + 10℃
```

![Formula block](doc:660ab37/tier:flash/page:18/block:17)

![Formula block](doc:660ab37/tier:flash/page:18/block:18)

5-11

<!-- page 19 of 31 -->

MIL-HDBK-217F

## 5.7 MICROCIRCUIT, MAGNETIC BUBBLE MEMORIES

## Write Duty Cycle Factor - π

![Formula block](doc:660ab37/tier:flash/page:19/block:4)

![Formula block](doc:660ab37/tier:flash/page:19/block:5)

![Formula block](doc:660ab37/tier:flash/page:19/block:6)

Avg. Device Data Rate D ≤1 Míg. Max. Rated Data Rate

R/W  No. of Reads per Write

NOTE:

For seed-bubble generators, divide πw by 4, or use 1, whichever is greater.

Duty Cycle Factor - πD

![Formula block](doc:660ab37/tier:flash/page:19/block:12)

![Formula block](doc:660ab37/tier:flash/page:19/block:13)

Device Complexity Failure Rates for Memory Storage Structure - C12 and C22

![Formula block](doc:660ab37/tier:flash/page:19/block:15)

![Formula block](doc:660ab37/tier:flash/page:19/block:16)

![Formula block](doc:660ab37/tier:flash/page:19/block:17)

Aii Other Modei Parameters

```
Parameter           Section
C2                  5.9
πE，πQ·πL            5.10
```

5-12

<!-- page 20 of 31 -->

MIL-HDBK-217F

5.8 MICROCIRCUITS, xT TABLE FOR ALL

```
      Duyr
   Ga Dnl
               10300
                     14--°7
                       31-07
                                13-06
                                                   6.--03
                 2.50--06
                        630-7
                            3.1-6
                              930-
                                  253-06
                                    4-0-5
                                            6-04
                                              103-03
                                               1-03
                                                 C1-0
                                                       15-02
                                                           3--02
                                                                      5.70-01
                   5--0
                          15-6
                                        17-01
                                          3.30-0
                                                         243-02
                                                             63--02
                                                                    3.70-01
                                                               10-1
                                                                 16-1
                                                                   240-01
                                                                        05-01
     v
      o
                            153-06
                                 140-06
                              320-0
                                                          37-02
                        2-7
                                                       133-02
                 4-09
                   21-0
                      133-7
                          67-07
                                    2030-06
                                         210-24
                                             753-°04
                                                         20-2
               3230-09
                                0-300'9
                                      .730L-6
                                        113-0
                                            40-04
                                               143-01
                                                 2.4-0
                                                   4.33-0
                                                     53-°0C
                                                             61-02
                     80-
                                                               1.03-01
                                                                 163--01
                                                                  2.6-01
                                                                    41-01
                                                                      64-01
                                                                        0-1
                                                                              Geak es
     Aovy
                     620
                                                                                                              s s
      SONT'EON
     d
               10 15
                   2      5
                            12
                                  2
          9                         0     8.5 二 18
                              1.6 21
                                                28884680
                                                                128 180 20
                                                                        20
                  23     71 10 二 20
               10 15
                                     70
                                2
                                  30 5.2
                                        3    222834872
                                                                              (.6110.5
                                           16             10  180 20 270 30 80 480
                                          12
    VHSC CHOS
  DM.
                      24
         3     10 13 16 1
                        20
                          3
                            42
                              50      8 11 17
                                                    11
                                           15 1.0
                                                   27
                                                       55 3.9 6.0 9.9 8 7.0 9'8
                                               21 21
  I  '
         6            3   55 12
               10 15
                  21
                              16
                                  20 50
                                       66
                                         3 二 二1 12323437202033
                                21
                                               120                  10 20
                                                                             Sien Dis
                                                                                   E(ec es) (Ao) A y Aove)
  BRCOS.
    LST        10 1 19  15 7
                              10 1.3 13 21 2.5
          5                            3   50   a   13 16
                                                        219227837485
                                                                        38
                                                                             121
                                                                                             TC
              10
                13 18 22
                      3     6 80 10
         12                      215           4.8
                                     1.9 2.3 2.8 31 41 5.8 6.9
                                                    2     13
                                                            1518
                                                         11    20227313
STL                    3
              10 12 227      87        1.6 10                               3                      P
                         25
                                          22
                                              2
                                                37
                                                  2     7 L'L 0.0
         4                                                    10 11 13 15 10
  CL
                                                                                             1              2im
                                                                             x =L
                                                                                             NOTES:
                                                                                    I
          1.C)
              23                                                                     人
               3330583830783880
                                            100 110   10 13 15
                                                               13 10 16 20
                                                              10
                                                                       175
```

5-13

<!-- page 21 of 31 -->

MIL-HDBK-217F

5.9 MICROCIRCUITS, C2 TABLE FOR ALL

Package Failure Rate for all Microcircuits - C2

```
                               Package Type
           Hermetic: DIPs
            w/Solder or                                         Nonhermetic:
Number of  Weld Seal, Pin DIPs with Glass Flatpacks with Cans4   DIPs, PGA,
Functional   Grid Array    Seat²     Axial Leads on             SMT (Leaded
Pins, Np    (PGA) 1, SMT             50 Mil Centers³                and
                                                                Nonleaded)5
            (Leaded and
            Nonleaded)
   3468
               .00092       .00047       .00022      .00027       .0012
              .0013         .00073       .00037      .00049       .0016
              .0019         .0013        .00078      .0011        .0025
               .0026        .0021        .0013       .0020        .0034
   10         .0034         .0029        .0020       .0031        .0043
  12          .0041         .0038        .0028       .0044        .0053
  14           .0048        .0048        .0037       .0060        .0062
  16           .0056       .0059         .0047       .0079        .0072
  18          .0064         .0071        .0058                    .0082
  22          .0079        .0096         .0083                    .010
  24          .0087         .011         .0098                    .011
  28          .010         .014                                   .013
  36          .013         .020                                   .017
  40          .015         .024                                   .019
  64          .025         .048                                   .032
  80          .032                                                .041
  128         .053                                                .068
  180         .076                                                .098
  224         .097                                                .12
                                             C2=9.0 × 10-5(Np)1.51
    C2=2.8 × 104 (Np)
1.                   1.08               2.
    C2=3.0 × 10-5 (N)1.82
                                             C2=3.0 × 10-5 (Np)2.01
3.                                      4.
                     1.08
    C2=3.6 × 10-4(Np)
5.
NOTES:
1.   SMT: Surface Mount Technology
2.   DIP: Dual In-Line Package
3.   If DIP Seal type is unknown, assume glass
4.   The package faiiure rate (C2) accounts for faiiures associated oniy with ihe package iseif.
     Failures associated with mounting the package to a circuit board are accounted for in
     Section 16, InterconnectionAssemblies.
```

5-14

<!-- page 22 of 31 -->

MIL-HDBK-217F

## 5.10 MICROCIRCUITS, xE, λL AND xQ TABLES FOR ALL

Environment Factor - πE

```
Environment          RE
   GB                .50
   GF               2.0
   GM               4.0
   NS               4.0
   NU               6.0
   AIC              4.0
   AF               5.0
   AUC              5.0
   AUF              8.0
   ARW              8.0
   SF                .50
   MF               5.0
   ML              12
   CL             220
```

Learming Factor - πL

```
  Years in Production, Y πL
  ≤.1                   2.0
  .5                    1.8
  1.0                   1.5
  1.5                   1.2
  ≥ 2.0                 1.0
πL = .01 exp(5.35 - .35Y)
Y = Years generic device type has been
   in production
```

Quality Factors - πQ

```
            Description                   xQ
 Class S Categories:
   1:
       Procured in full accordance
       with MIL-M-38510, ClassS
        requirements.
   2.                                      .25
       Procured in full accordance
       with MIL--38535 and
       Appendix B thereto (Class U).
   3.  Hybrids: (Procured to Class
       S requirements (Quality Level
       K) of MIL-H-38534.
 Class B Categories:
       Procured in full accordance
   1.
       with MiL-M-38510, Ciass B
       requirements.
   2.  Procured in fult accordance       1.0
       with MIL-I-38535, (Class Q).
   3.  Hybrids: Procured to Class B
       requirements (Quality Level
       H) of MIL-H-38534.
Class B-1 Category:
  Fully compliant with all
   requirements of paragraph 1.2.1       2.0
  of MIL-STD-883 and procured to a
  MIL drawing. DESC drawing or
  ather govemment approved
  documentation. (Does not include
  hybrids). For hybrids use custom
  screening section below.
```

5-15

<!-- page 23 of 31 -->

MIL-HDBK-217F

## 5.10 MICROCIRCUITS, πE, πL AND πQ TABLES FOR ALL

Quality Factors (cont'd):  Calculation for Custom Screening Programs

```
    Group               MIL-STD-883 Screen/Test (Note 3)       Point Valuation
             TM 1010 (Temperature Cycle, Cond B Minimum) and TM 2001
             (Constant Acceleration, Cond B Minimum) and TM 5004 (or 5008
     1      for Hybrids) (Final Electricals @ Temp Extremes) and TM 1014 50
            (Seal Test, Cond A, B, or C) and TM 2009 (Extemal Visual)
            TM 1010 (Temperature Cycle, Cond B Minimum) or TM 2001
             (Constant Acceleration, Cond B Minimum)
     2*     TM 5004 (or 5008 for Hybrids) (Final Electricals @ Temp Extremes) 37
            and TM 1014 (Seai Tesi, Cond A, B, or C) and TM 2009 (Extemai
            Visuen
            Pre-Bum in Electricals
     3      TM 1015 (Burn-in B-LeveVS-Level) and TM 5004 (or 5008 for 30 (B Level)
            Hybrids) (Post Bum-in Electricals @ Temp Extremes) 36   (S Level)
     4       TM 2020 Pind (Particie Impadt Noise Detection)    11
     5      TM 5004 (or 5008 for Hybrids) (Final Electricals @ Temperature 11 (Note 1)
            Extremes)
     6      TM 2010/17 (Intemal Visual)                         7
     7*      TM 1014 (Seal Test, Cond A, B, or C)               7  (Note 2)
     8      TM 2012 (Radiography)                               7
     9       TM2009 (Extemal Visual)                            7  (Note 2)
     10     TM 5007/5013 (GaAs) (Wafer Acceptance)              1
     11     TM 2023 (Non-Destructive Bond Pull)                 1
                   87
      πQ=2+
             Σ Point Valuations
 *NOT APPROPRIATE FOR PLASTIC PARTS.
 NOTES:
      Point valuation only assigned if used independent of Groups 1, 2 or 3.
    1.
      Polnt valuation onty assigned if used independent of Groups 1 or 2.
    2.
   3. Sequencing of tests within groups 1, 2 and 3 must be foliowed.
    4. TM refers to the MIL-STD-883 Test Method.
   5.
      Nonhermetic parts should be used only in controlled environments (i.e., GB and other
      temperature/humidity controlled environments).
EXAMPLES:
1.    Mfg. performs Group 1 test and Class B bum-in: πQ = 2 + 87 =3.1
                                              50+30
2.    Mfg. perfoms intemal visual test, seal test and final electrical test: 87
                                                            7+7+11 -5.5
                                                     πQ=2+
      Other Commercial or Unknown Screening Levels  πQ=10
```

5-16

<!-- page 24 of 31 -->

MIL-HDBK-217F

## 5.11 MICROCIRCUITS, TJ DETERMINATION, (ALL EXCEPT HYBRIDS)

Ideally, device case temperatures should be determined from a detailed thermal analysis of the equipment. Device junction temmperature is then calculated with the following relationship:

![Formula block](doc:660ab37/tier:flash/page:24/block:4)

TJ Worst Case Junction Temperature (°C).

TC = Case Telperature (°C). i not avallable, use the tolowing detault table.

Default Case Temperature (Tc) for all Environments

```
Environment GB GF GM NS NU A4C AF AUC AUF ARW SF MF ML
                                       CL
{C(C) 35 45 50 45 50 60 60
                      75  75 60 35 50 60 45
```

θJC = Junction-to-case thermal resistance (°C/watt) for a device soldered into a printed circuit board. if θjC is not available, use a value contained in a specification for the closest equivalent device or use the following table.

```
             Die Area > 14,400 mil² θJC Die Area ≤ 14,400 mil²
 Package Type       (CM)
 (Ceramic Only)                      θJC (CM)
Dual-In-Line         11                28
Flat Package         10                22
Chip Carrier         10                20
Pin Grid Array       10                20
Can                                    70
```

P The maximum power dissipation realized in a system application. If the applied power is not available, use the maximum power dissipation from the specification for the closest equivalent device.

5-17

<!-- page 25 of 31 -->

MIL-HDBK-217F

## 5.12 MICROCIRCUITS, T DETERMINATION, (FOR HYBRIDS)

This section describes a method for estimating junction temperature (T) for integrated circuit dice mounted in a hybrid package. A hybrid is normally made up of one or more substrate assemblies mounted within a sealed package. Each substrate assembly consists of active and passive chips with thick or thin film metallization mounted on the substrate, which in turn may have multiple layers of metallization and dielectric on the surface. Figure 5-1 is a cross-sectional view of a hybrid with a single multi-layered substrate. The layers within the hybrid are made up of various materials with different thermal characteristics. The table following Figure 5-1 provides a list of commonly used hybrid materlals with typical thicknesses and corresponding thermnal conductivities (K). If the hybrid intemal structure cannot be determined, use the following default values for the temperature rise trom case to junction: microcircuits, 10°C; transistors, 25°C; diodes, 20°C. Assume capacitors are at TC

![Image block](doc:660ab37/tier:flash/page:25/block:4)

Figure 5-1: Cross-sectionai View of a Hybrid with a Singie Muiti-Layered Substrate

5-18

<!-- page 26 of 31 -->

MIL-HDBK-217F

5.12 MICROCIRCUITS, T\_ DETERMINATION, (FOR HYBRIDS)

```
                                                            Thermal
                                                          Conductivity,
                                       Typica!   Feature
                                                                     ()(4)
      Material                                                K
                      Typical Usage   Thickness, From Figure (W/n2)
                                       Li (in.)    5-1      Cin
                                                                     (in2 °C/W)
 Silicon          Chip Device          0.010       A        2.20      .0045
 GaAs             Chip Device          0.0070      A         .76      .0092
 Au Eutectic      Chip Attach          0.0001      B        6.9       .000014
 Solder           Chip/Substrate Attach 0.0030    B/E       1.3       .0023
 Epoxy (Dielectric) Chip/Substrate Attach 0.0035  B/E        .0060    .58
 Epoxy (Conductive) Chip Attach        0.0035      B         .15      .023
 Thick Film Dielectric Glass Insulating Layer 0.0030 C       .66      .0045
Alumina           Substrate, MHP       0.025       D         .64      .039
 Beryllium Oxide  Substrate, PHP       0.025       D       6.6        .0038
Kovar             Case, MHP            0.020       F        .42       .048
Aluminum          Case, MHP            0.020       F       4.6        .0043
Copper            Case, PHP           0.020        F       9.9        .0020
```

NOTE: MHP: Multichip Hybrid Package, PHP: Power Hybrid Package (Pwr: ≥ 2W, Typically)

![Formula block](doc:660ab37/tier:flash/page:26/block:5)

n M Number of Materia! Layers

K= Thermal Conductivity of  Material W/in2) C/in (User Provided or From Table)

Lj= Thickness of th Material (in) (User Provided or From Table)

À = Die Àrea (in²). if Die Àrea cannot be readily determined, estimate as follows: A = [.00278 (No. of Die Active Wire Terminals) + .0417)2

Estimate T as Follows:

![Formula block](doc:660ab37/tier:flash/page:26/block:11)

TC  Hybrid Case Temperature (°C). If unknown, use the Tc Default Table shown in Section 5.11.

θJC= Junction-to-Case Thermal Resistance (°C/W) (As determined above)

PD Die Power Dissipation (W)

5-19

<!-- page 27 of 31 -->

MIL-HDBK-217F

## 5.13 MICROCIRCUTS, EXAMPLES

Example 1: CMOS Digital Gate Array

Given: A CMOS digital timing chip (4046) in an airbome inhabited cargo application, case temperature 48°C, 75mW power dissipation. The device is procured with normal manufacturers screening consisting of temperature cycling, constant acceleration, electrical testing, seal test and extemal visual Inspection, in the sequence given. The component manufacturer aiso pertorms a B-levei bum-in followed by electrical testing. All screens and tests are performed to the applicable MIL-STD-883 screening method. The package is a 24 pin ceramic DIP with a glass seal. The device has been manufactured for several years and has 1000 transistors.

![Formula block](doc:660ab37/tier:flash/page:27/block:5)

![Formula block](doc:660ab37/tier:flash/page:27/block:6)

![Formula block](doc:660ab37/tier:flash/page:27/block:7)

![Formula block](doc:660ab37/tier:flash/page:27/block:8)

Section 5.9

![Formula block](doc:660ab37/tier:flash/page:27/block:10)

Section 5.10

![Formula block](doc:660ab37/tier:flash/page:27/block:12)

![Formula block](doc:660ab37/tier:flash/page:27/block:13)

![Formula block](doc:660ab37/tier:flash/page:27/block:14)

![Formula block](doc:660ab37/tier:flash/page:27/block:15)

Section 5.10

![Formula block](doc:660ab37/tier:flash/page:27/block:17)

## Example 2: EEPROM

Given: À 128K Fiotox EEPROM that is expected to have a Tj of 80°C and experience 10,000 read/write cycles over the life of the system. The part is procured to all requirements of Paragraph 1.2.1, MIL-STD-883, Class B screening level requirements and has been in production for three years. It is packaged in a 28 pin DǐP with a glass seal and will be used in an airborne uninhabited cargo application.

![Formula block](doc:660ab37/tier:flash/page:27/block:20)

![Formula block](doc:660ab37/tier:flash/page:27/block:21)

![Formula block](doc:660ab37/tier:flash/page:27/block:22)

![Formula block](doc:660ab37/tier:flash/page:27/block:23)

Section 5.8

![Formula block](doc:660ab37/tier:flash/page:27/block:25)

5-20

<!-- page 28 of 31 -->

MIL-HDBK-217F

## 5.13 MICROCIRCUITS, EXAMPLES

```txt
πE = 5.0 Section 5.10
πQ 2.0 Section 5.10
πL 1 1.0 Section 5.10
λcyc .38 Section 5.2:
2cyc- A1 B1+ A2B2 πQ πECC
A2 = B2 = 0 for Flotox
Assumme No ECC, πECC = 1
A1 = .1, 7K ≤ C ≤ 15K Emry
B1 = 3.8 (Use Equation 1 at bottom oi B1 and B2 Tabie)
λcyc = Aq Bq = (.1)(3.8) = .38
```

![Formula block](doc:660ab37/tier:flash/page:28/block:4)

## Example 3: GaAs MMIC

Given: A MA4GM212 Single Pole Double Throw Switch, DC - 12 GHz, 4 transistors, 4 inductors, 8 resistors, maximum input Pp = 30 dbm, 16 pin hermetic flatpack, maximum TCH = 145°C in a ground benign environment. The part has been manutactured for 1 year and is screened to Paragraph 1.2.1 of MIL-STD-883, Class B equivalent screen.

![Formula block](doc:660ab37/tier:flash/page:28/block:7)

```txt
C1 4.5 Section 5.4, MMIC Table, 4 Active Elements (See Footnote to
Table)
πT 日 .061 Section 5.8, T = TCH = 145°C
πA 3.0 Section 5.4, Unknown Application
C2 .0047 Section 5.9
πE .50 Section 5.10
πL 1.5 Section 5.10
πQ 2.0 Section 5.10
```

![Formula block](doc:660ab37/tier:flash/page:28/block:9)

NOTE: The passive elements are assumed to contribute negligibly to the overaii device failure rate.

## Example 4: Hybrid

Given: A linear multichip hybrid driver in a hermeticaly sealed Kovar package. The substrate is alumina and there are two thick film dielectric layers. The die and substrate attach materials are conductive epoxy and solder, respectively. The application environment is naval unsheltered, 65°C case temperature and the device has been in production for over two years. The device is

5-21

<!-- page 29 of 31 -->

MIL-HDBK-217F

## 5.13 MICROCIRCUITS, EXAMPLES

screened to MIL-STD-883, Method 5008, in accordance with Table VIll, Class B requirements. The hybrid contalns the following components:

Active Components:

1 一 LM106 Bipolar Comparator/Buffer Die (13 Transistors)

1 LM741A Bipolar Operational Amplifier Die (24 Transistors)

2 Si NPN Transistor

2 Si PNP Transistor

2 - Si General Purpose Diodes

Passive Components:

2 Ceramic Chip Capaciors 17 Thick Fllm Resistors

![Formula block](doc:660ab37/tier:flash/page:29/block:12)

1. Estimate Active Device Junction Temperatures

If limited information is available on the specific hybrid materials and construction characteristics the default case-to-junction temperature rises shown in the introduction to Section 5.12 can be used. When detaiied intormation becomes availabie the following Section 5.12 procedure should be used to determine the junction-to-case (θjc) thermal resistance and Tj values for each component.

![Formula block](doc:660ab37/tier:flash/page:29/block:15)

(Equation 1)

```
                                                          (同)(4)
         Layer             Figure 5-1 Feature
                                                         (in2 °C/W)
Silicon Chip                     A                         .0045
Conductive Epoxy                 B                         .023
Two Dielectric Layers            C          (2)(.0045) =   .009
Alumina Substrate                D                        .039
Solder Substrate Attachment     E                         .0023
Kovar Case                       F                         048
                                           (R)(4)=
                                                           .1258
```

A = Die Area = [.00278 (No. Die Active Wire Terminals) + .0417]2 (Equation 2)

![Formula block](doc:660ab37/tier:flash/page:29/block:19)

5-22

<!-- page 30 of 31 -->

MIL-HDBK-217F

## 5.13 MICROCIRCUITS, EXAMPLES

```
                 LM106  LM741A   SiNPN   Si PNP  Si Diode     Source
 No. of Pins     8      14       3       3        2      Vendor Spec. Sheet
Power Dissipation, .33    .35     .6      .6       .42   Circuit Analysis
PD(M)
Area of Chip (in.2) .0041 .0065   .0025   .0025    .0022 Equ. 2 Above
θJC (CM)        30.8    19.4    50.3    50.3     56.3    Equ. 1 Above
TJ(C)           75      72      95      95       89      Equ. 3 Above
```

2. Calculate Failure Rates for Each Component:

A) LM106 Die, 13 Transistors (from Vendor Spec. Sheet)

![Formula block](doc:660ab37/tier:flash/page:30/block:6)

B) LM741 Die, 23 Transistors. Use Same Procedure as Above.

![Formula block](doc:660ab37/tier:flash/page:30/block:8)

C) Silicon NPN Transistor, Rated Power = 5W (From Vendor Spec. Sheet), VCENCEO = .6, Linear Application

![Formula block](doc:660ab37/tier:flash/page:30/block:10)

D) Silicon PNP Transistor, Same as C.

![Formula block](doc:660ab37/tier:flash/page:30/block:12)

E) Silicon Generai Purpose Diode (Anaiog), Voltage Stress = 60%, Metallurgically Bonded Construction.

![Formula block](doc:660ab37/tier:flash/page:30/block:14)

5-23

<!-- page 31 of 31 -->

MIL-HDBK-217F

## 5.13 MICROCIRCUITS, EXAMPLES

F) Ceramic Chip Capacitor, Voltage Stress = 50%, TA = TCASE for the Hybrid, 1340 pF, 125°C Rated Temp.

![Formula block](doc:660ab37/tier:flash/page:31/block:4)

Section 10.11; πQ, πE Default to 1.0

G Thick Film Resistors, per instructions in Section 5.5, the contribution of these devices is considered insignificant relative to the overall hybrid faiture rate and they may be ignored.

Overall Hybrid Part Failure Rate Calculation:

![Formula block](doc:660ab37/tier:flash/page:31/block:8)

Section 5.5

![Formula block](doc:660ab37/tier:flash/page:31/block:10)

![Formula block](doc:660ab37/tier:flash/page:31/block:11)

5-24