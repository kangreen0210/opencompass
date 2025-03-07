from mmengine.config import read_base

with read_base():
    from .groups.supergpqa import supergpqa_summary_groups

summarizer = dict(
    dataset_abbrs=[
    "supergpqa",
    "supergpqa_Procedural_Law",
    "supergpqa_Microbiology",
    "supergpqa_World_History",
    "supergpqa_Civil_and_Commercial_Law",
    "supergpqa_Relativity",
    "supergpqa_Discrete_Mathematics",
    "supergpqa_Laser_Technology",
    "supergpqa_Power_Machinery_and_Engineering",
    "supergpqa_Geotechnical_Engineering",
    "supergpqa_Mineralogy,_Petrology,_and_Economic_Geology",
    "supergpqa_Fluid_Flow_and_Heat_Transfer_in_Chemical_Engineering",
    "supergpqa_Composition",
    "supergpqa_Biophysics",
    "supergpqa_Geriatric_Medicine",
    "supergpqa_Cell_Biology",
    "supergpqa_Underwater_Acoustics",
    "supergpqa_Political_Science",
    "supergpqa_Atomic_and_Molecular_Physics",
    "supergpqa_Industrial_Economics",
    "supergpqa_Marine_Chemistry",
    "supergpqa_Ophthalmology",
    "supergpqa_Geochemistry",
    "supergpqa_Anesthesiology",
    "supergpqa_Sports_Science_and_Medicine",
    "supergpqa_Forest_Cultivation_and_Genetic_Breeding",
    "supergpqa_Philology_and_Bibliography",
    "supergpqa_Cryptography",
    "supergpqa_Road_and_Railway_Engineering",
    "supergpqa_Literary_History",
    "supergpqa_Mining_and_Safety_Engineering",
    "supergpqa_Group_Theory",
    "supergpqa_Crop_Science",
    "supergpqa_Food_Biochemistry",
    "supergpqa_Textile_Materials_Science",
    "supergpqa_Fundamental_Mathematics",
    "supergpqa_Microelectronics_and_Solid-State_Electronics",
    "supergpqa_International_Law",
    "supergpqa_Agricultural_Environment_and_Soil-Water_Engineering",
    "supergpqa_Environmental_Science",
    "supergpqa_Urban_Infrastructure_Engineering",
    "supergpqa_Solid_State_Physics",
    "supergpqa_Mechatronic_Engineering",
    "supergpqa_Economic_History",
    "supergpqa_Power_Electronics_and_Electrical_Drives",
    "supergpqa_History_and_Theory_of_Journalism_and_Media_Management",
    "supergpqa_Neurology",
    "supergpqa_Computer_Networks",
    "supergpqa_Animal_Nutrition_and_Feed_Science",
    "supergpqa_Marine_Engineering",
    "supergpqa_Materials_Physics_and_Chemistry",
    "supergpqa_Business_and_Accounting_Management",
    "supergpqa_Basic_Stomatology",
    "supergpqa_Space_physics",
    "supergpqa_Transportation_Planning_and_Management",
    "supergpqa_Information_Management_and_Communication",
    "supergpqa_Quantitative_Economics",
    "supergpqa_Elements_of_Chemical_Reaction_Engineering",
    "supergpqa_Library_and_Archival_Science",
    "supergpqa_Electrodynamics",
    "supergpqa_Fluid_Machinery_and_Engineering",
    "supergpqa_Dynamic_Meteorology",
    "supergpqa_Functions_of_Real_Variables",
    "supergpqa_Pharmacology",
    "supergpqa_Communication_Principles",
    "supergpqa_Communication_and_Broadcasting",
    "supergpqa_Musical_Forms_and_Analysis",
    "supergpqa_Cartography_and_Geographic_Information_Engineering",
    "supergpqa_Maternal,_Child_and_Adolescent_Health",
    "supergpqa_Clinical_Stomatology",
    "supergpqa_Data_Structures",
    "supergpqa_Optoelectronic_Technology",
    "supergpqa_Physiology",
    "supergpqa_Thermodynamics_and_Statistical_Physics",
    "supergpqa_Pediatrics",
    "supergpqa_Geodesy_and_Surveying_Engineering",
    "supergpqa_Theoretical_Mechanics",
    "supergpqa_Hydraulics_and_Hydrology",
    "supergpqa_International_Trade",
    "supergpqa_Military_Chemistry_and_Pyrotechnics",
    "supergpqa_Finance",
    "supergpqa_Psychiatry_and_Mental_Health",
    "supergpqa_Fundamentals_of_Dynamics_and_Control",
    "supergpqa_Sports_Humanities_and_Sociology",
    "supergpqa_Harmony",
    "supergpqa_Control_Theory_and_Control_Engineering",
    "supergpqa_Surgery",
    "supergpqa_Analytical_Chemistry",
    "supergpqa_Political_Economy",
    "supergpqa_Theory_of_Curriculum_and_Instruction",
    "supergpqa_High_Voltage_and_Insulation_Technology",
    "supergpqa_Numerical_Analysis",
    "supergpqa_Physical_Geography",
    "supergpqa_Physical_Education_and_Training",
    "supergpqa_Applied_Optics",
    "supergpqa_Mathematical_Analysis",
    "supergpqa_Advanced_Programming_Languages",
    "supergpqa_Western_Economics",
    "supergpqa_Organic_Chemistry",
    "supergpqa_French_Language_and_Literature",
    "supergpqa_Urban_Planning_and_Design",
    "supergpqa_Polynomials_and_Series_Expansions",
    "supergpqa_Functions_of_Complex_Variables",
    "supergpqa_Advanced_Algebra",
    "supergpqa_Operating_Systems",
    "supergpqa_Internal_Combustion_Engineering",
    "supergpqa_Food_Processing_and_Storage_Engineering",
    "supergpqa_Educational_Technology_and_Principles",
    "supergpqa_Acoustics",
    "supergpqa_Quantum_Mechanics",
    "supergpqa_Iron_and_Steel_Metallurgy",
    "supergpqa_Land_Resource_Management_and_Administrative_Management",
    "supergpqa_Fuzzy_Mathematics",
    "supergpqa_Special_Education",
    "supergpqa_Solid_Mechanics",
    "supergpqa_Zoology",
    "supergpqa_Demography_and_Anthropology",
    "supergpqa_Tourism_Management_and_Technological_Economics_Management",
    "supergpqa_Theoretical_Optics",
    "supergpqa_Genetics",
    "supergpqa_Constitutional_and_Administrative_Law",
    "supergpqa_Structural_Engineering",
    "supergpqa_Principles_of_Metallurgy",
    "supergpqa_Medicinal_Chemistry",
    "supergpqa_Electromagnetic_Field_and_Microwave_Technology",
    "supergpqa_Clinical_Laboratory_Diagnostics",
    "supergpqa_Theoretical_Fluid_Mechanics",
    "supergpqa_Pitch_and_Scales",
    "supergpqa_Stochastic_Processes",
    "supergpqa_Ethics",
    "supergpqa_Circuits_and_Systems",
    "supergpqa_Engineering_Thermophysics",
    "supergpqa_Landscape_Plants_and_Ornamental_Horticulture",
    "supergpqa_Polymer_Physics",
    "supergpqa_Wood_Science_and_Technology",
    "supergpqa_Biochemistry_and_Molecular_Biology",
    "supergpqa_Preschool_Education",
    "supergpqa_Psychology",
    "supergpqa_Traditional_Chinese_Health_Preservation",
    "supergpqa_Modern_and_Contemporary_Chinese_Literature",
    "supergpqa_Religious_Studies",
    "supergpqa_Subatomic_and_Atomic_Physics",
    "supergpqa_Human_Geography",
    "supergpqa_Water_conservancy_and_Hydropower_Engineering",
    "supergpqa_Thermal_Energy_Engineering",
    "supergpqa_Immunology",
    "supergpqa_Communication_and_Information_Systems",
    "supergpqa_Meteorology",
    "supergpqa_Bridge_and_Tunnel_Engineering",
    "supergpqa_Military_Management",
    "supergpqa_Russian_Language_and_Literature",
    "supergpqa_Particle_and_Nuclear_Physics",
    "supergpqa_Rigid_Body_Mechanics",
    "supergpqa_Nuclear_Energy_and_Reactor_Technology",
    "supergpqa_Oncology",
    "supergpqa_Public_Finance",
    "supergpqa_Classical_Chinese_Literature",
    "supergpqa_Ecology",
    "supergpqa_Principles_of_Computer_Organization",
    "supergpqa_Pattern_Recognition",
    "supergpqa_Databases",
    "supergpqa_Ordinary_Differential_Equations",
    "supergpqa_Electrochemistry",
    "supergpqa_Traditional_Chinese_Pharmacy",
    "supergpqa_Dance_Studies",
    "supergpqa_Pharmaceutical_Analysis",
    "supergpqa_Otorhinolaryngology",
    "supergpqa_Principles_of_Seismic_Exploration",
    "supergpqa_Physical_Chemistry",
    "supergpqa_Special_Number_Theory",
    "supergpqa_Astrophysics",
    "supergpqa_Physical_Oceanography",
    "supergpqa_Instrumentation_and_Performance",
    "supergpqa_Military_Law",
    "supergpqa_Signal_and_Information_Processing",
    "supergpqa_Thermodynamics",
    "supergpqa_Architectural_Design_and_Theory",
    "supergpqa_Non-ferrous_Metallurgy",
    "supergpqa_Internal_Medicine",
    "supergpqa_Film_Studies",
    "supergpqa_Fluid_Physics",
    "supergpqa_Refrigeration_and_Cryogenic_Engineering",
    "supergpqa_Broadcasting_and_Television_Art",
    "supergpqa_Social_Medicine_and_Health_Management",
    "supergpqa_Military_Logistics_and_Equipment",
    "supergpqa_Criminal_Law",
    "supergpqa_Electrical_Theory_and_New_Technologies",
    "supergpqa_Nutrition_and_Food_Hygiene",
    "supergpqa_Literary_Theory",
    "supergpqa_Instrument_Science_and_Technology",
    "supergpqa_Legal_Theory_and_Legal_History",
    "supergpqa_Computer_Architecture",
    "supergpqa_Chemical_Transport_Engineering",
    "supergpqa_Military_Thought_and_History",
    "supergpqa_Archaeology_and_Museology",
    "supergpqa_Architectural_History",
    "supergpqa_Microbiology_and_Biochemical_Pharmacy",
    "supergpqa_Philosophy_of_Science_and_Technology",
    "supergpqa_Labor_Economics",
    "supergpqa_Dermatology_and_Venereology",
    "supergpqa_Materials_Processing_Engineering",
    "supergpqa_Human_Anatomy_and_Histology-Embryology",
    "supergpqa_Optical_Fiber_Communication",
    "supergpqa_Journalism_and_News_Practice",
    "supergpqa_Emergency_Medicine",
    "supergpqa_Veterinary_Medicine",
    "supergpqa_Heat_Transfer",
    "supergpqa_Information_Management_Science",
    "supergpqa_Physical_Chemistry_of_Metallurgical_Process",
    "supergpqa_Radiochemistry",
    "supergpqa_Guidance,_Navigation_and_Control",
    "supergpqa_Solid_Earth_Geophysics",
    "supergpqa_Systems_Science",
    "supergpqa_Weapon_Systems_Science_and_Engineering",
    "supergpqa_Manufacturing_Automation",
    "supergpqa_Engineering_Fluid_Mechanics",
    "supergpqa_Mineral_Processing_Engineering",
    "supergpqa_Animal_Rearing_and_Breeding",
    "supergpqa_Philosophical_Aesthetics",
    "supergpqa_Solar_System_Science",
    "supergpqa_Antenna_and_Radio_Communication",
    "supergpqa_Computational_Mathematics",
    "supergpqa_Health_Toxicology_and_Environmental_Health",
    "supergpqa_Design_Arts",
    "supergpqa_Computer_Software_and_Theory",
    "supergpqa_Aquaculture",
    "supergpqa_Nursing_and_Rehabilitation_Medicine",
    "supergpqa_Inorganic_Chemistry",
    "supergpqa_Traffic_Information_Engineering_and_Control",
    "supergpqa_Botany",
    "supergpqa_Number_Theory",
    "supergpqa_Hydrogeology",
    "supergpqa_Marine_Biology",
    "supergpqa_Law_and_Social_Governance",
    "supergpqa_Contract_Law",
    "supergpqa_Vehicle_Operation_Engineering",
    "supergpqa_Aeronautical_and_Astronautical_Science_and_Technology",
    "supergpqa_Poromechanics_and_Reservoir_Physics",
    "supergpqa_Pathogen_Biology",
    "supergpqa_Power_Systems_and_Automation",
    "supergpqa_Epidemiology_and_Health_Statistics",
    "supergpqa_Drama_and_Opera_Studies",
    "supergpqa_Environmental_Engineering",
    "supergpqa_Polymer_Chemistry_and_Physics",
    "supergpqa_Digital_Surveying_and_Remote_Sensing_Applications",
    "supergpqa_Atmospheric_Physics_and_Atmospheric_Environment",
    "supergpqa_Education_Economics,_Management_and_Social_Security",
    "supergpqa_Probability_and_Statistics",
    "supergpqa_Geometry_and_Topology",
    "supergpqa_Linguistics_and_Applied_Linguistics",
    "supergpqa_Astronomical_Observation_and_Technology",
    "supergpqa_Forensic_Medicine",
    "supergpqa_Fine_Arts",
    "supergpqa_Paleontology_and_Stratigraphy",
    "supergpqa_Management_Science_and_Engineering",
    "supergpqa_Logic",
    "supergpqa_Agricultural_Mechanization_Engineering",
    "supergpqa_Traditional_Chinese_Medicine_Theory",
    "supergpqa_Obstetrics_and_Gynecology",
    "supergpqa_Ship_Mechanics_and_Design_Principles",
    "supergpqa_Statistical_Mechanics",
    "supergpqa_Combinatorial_Mathematics",
    "supergpqa_Mass_Transport_and_Separation_Process_in_Chemical_Engineering",
    "supergpqa_Economic_Statistics",
    "supergpqa_Operations_Research_and_Cybernetics",
    "supergpqa_Formal_Languages",
    "supergpqa_Oil_and_Gas_Field_Development_and_Storage_&_Transportation_Engineering",
    "supergpqa_Environmental_and_Resource_Protection",
    "supergpqa_Structural_Geology",
    "supergpqa_Semiconductor_Physics",
    "supergpqa_Social_and_Folklore_Studies",
    "supergpqa_Music_History,_Education,_and_Technology",
    "supergpqa_Radiation_Protection_and_Nuclear_Technology_Applications",
    "supergpqa_Pathology_and_Pathophysiology",
    "supergpqa_Textile_Chemistry_and_Dyeing_Engineering",
    "supergpqa_Military_Command_and_Information_Systems",
    "supergpqa_Forest_Engineering",
    "supergpqa_Graph_Theory",
    "supergpqa_Radiation_Medicine",
    "supergpqa_Geological_Resources_and_Geological_Engineering",
    "supergpqa_Historical_Geography",
    "supergpqa_Cosmology",
    "supergpqa_Pharmaceutics",
    "supergpqa_National_and_Defense_Economics",
    "supergpqa_Imaging_and_Nuclear_Medicine",
    "supergpqa_Stellar_and_Interstellar_Evolution"
],
    summary_groups=sum([v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)
