# Moteus Parts Reconstruction & Validation

## Methodology
* Original parts were imported into Fusion. 
* Data for edges, arcs, and lines were extracted to create profiles.
* These profiles were added or subtracted to generate the final 3D part designs.
* **Note:** While the original GitHub repository lists 44 parts, the C1 components are identical to X1. Therefore, there are exactly 31 unique, valid parts.

## Validation
A validation script (`validate_moteus.py`) compares the rebuilt output models to the original parts using cadquery and trimesh. It calculates Volumetric Difference (mm³ and %) and Symmetric Difference (mm³ and %).

### Validation Output
```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  Moteus Parts — Validation Report (Volume & Symmetric Difference)            ║
╚══════════════════════════════════════════════════════════════════════════════╝
  Originals : /Users/softage/Desktop/Moteus/Original Step:stl files
  Outputs   : /Users/softage/Desktop/Moteus/Script
  STEP loader : cadquery
  trimesh   : ✓

  [OK                                      ] 21-0487A_MXM
  [OK                                      ] 21-0664E_1233-1C_MXM
  [OK                                      ] D0014A
  [OK                                      ] DDA0008E
  [OK                                      ] DRB0008F
  [OK                                      ] DRL0008A
  [OK                                      ] DSE0006A
  [OK                                      ] FDMT80080DC
  [OK                                      ] IND_4018-WE-LQS_WRE
  [OK                                      ] IND_6028-WE-LQS_WRE
  Processing: IND_8040-WE-LQS_WRE .../Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/trimesh/triangles.py:302: RuntimeWarning: invalid value encountered in divide
  center_mass = integrated[1:4] / volume
  [OK                                      ] IND_8040-WE-LQS_WRE
  [OK                                      ] IND_DFE252012_MUR
  [OK                                      ] QFN-16_MA600_MNP
  [OK                                      ] RTA0040B
  [OK                                      ] S3B-PH-SM4-TB_LF__SN_
  [OK                                      ] TSSOP14_OSM
  [OK                                      ] SM08B-GHS-TB
  [OK                                      ] XT60PW-M
  [OK                                      ] TSON Advance
  [OK                                      ] SM07B-GHS-TB-LF--SN---3DModel-STEP-56544
  [OK                                      ] XT30PW-M
  [OK                                      ] SOP_Advance
  [OK                                      ] SM06B-GHS-TB
  [OK                                      ] UFQFPN-48_7X7X0P55MM
  [OK                                      ] SOD-523_STM
  [OK                                      ] S6B-ZR-SM4A-TF_LF__SN_
  [OK                                      ] 20250427-moteus-x1-r1
  [OK                                      ] 20230226-moteus-n1-mechanical
  [OK                                      ] 20230523-moteus-n1-r1_3-mechanical
  [OK                                      ] 20200729-moteus-controller-r43-mechanical
  [OK                                      ] 20210124-moteus-controller-r45-mechanical

┌──────────────────────────────────────────────────────────────────────────────┐
│  Part Name                                 Vol Diff (mm³)     Vol (%)    Sym Diff (mm³)     Sym (%)  │
├──────────────────────────────────────────────────────────────────────────────┤
│  21-0487A_MXM                                       0.000        0.00%                 —            —  │
│  21-0664E_1233-1C_MXM                               0.000        0.00%                 —            —  │
│  D0014A                                             0.076        0.15%             0.642        1.26%  │
│  DDA0008E                                           0.190        0.64%                 —            —  │
│  DRB0008F                                           0.000        0.00%                 —            —  │
│  DRL0008A                                           0.009        0.66%                 —            —  │
│  DSE0006A                                           0.002        0.09%                 —            —  │
│  FDMT80080DC                                        0.003        0.01%             0.006        0.01%  │
│  IND_4018-WE-LQS_WRE                                0.000        0.00%             0.000        0.00%  │
│  IND_6028-WE-LQS_WRE                                0.000        0.00%             0.000        0.00%  │
│  IND_8040-WE-LQS_WRE                                0.000        0.00%             0.000        0.00%  │
│  IND_DFE252012_MUR                                  0.000        0.00%             0.000        0.00%  │
│  QFN-16_MA600_MNP                                   0.000        0.00%             0.000        0.00%  │
│  RTA0040B                                           0.000        0.00%                 —            —  │
│  S3B-PH-SM4-TB_LF__SN_                              0.002        0.00%                 —            —  │
│  TSSOP14_OSM                                        0.001        0.00%             1.004        3.78%  │
│  SM08B-GHS-TB                                       0.005        0.00%                 —            —  │
│  XT60PW-M                                          22.206        1.38%            30.218        1.88%  │
│  TSON Advance                                       0.002        0.03%                 —            —  │
│  SM07B-GHS-TB-LF--SN---3DModel-STEP-565             0.110        0.09%                 —            —  │
│  XT30PW-M                                          39.440       12.94%                 —            —  │
│  SOP_Advance                                        0.001        0.00%                 —            —  │
│  SM06B-GHS-TB                                       0.004        0.00%                 —            —  │
│  UFQFPN-48_7X7X0P55MM                               0.000        0.00%             0.000        0.00%  │
│  SOD-523_STM                                        0.001        0.08%             0.001        0.08%  │
│  S6B-ZR-SM4A-TF_LF__SN_                             1.237        0.90%             1.270        0.93%  │
│  20250427-moteus-x1-r1                             39.202        0.45%            39.218        0.45%  │
│  20230226-moteus-n1-mechanical                      0.004        0.00%             0.014        0.00%  │
│  20230523-moteus-n1-r1_3-mechanical                 2.058        0.03%             2.069        0.03%  │
│  20200729-moteus-controller-r43-mechani             0.003        0.00%             0.025        0.00%  │
│  20210124-moteus-controller-r45-mechani             0.003        0.00%             0.025        0.00%  │
└──────────────────────────────────────────────────────────────────────────────┘

  Notes:
  • Vol Diff   = |volume(original) − volume(output)|  in mm³
  • Vol (%)    = Vol Diff as % of original volume
  • Sym Diff   = (A−B) ∪ (B−A) boolean volume in mm³  [requires watertight meshes]
  • Sym (%)    = Sym Diff as % of original volume
  • '—' in Sym columns means the mesh is an open shell or trimesh is unavailable.
```
