# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:47:01 2021

@author: mikko.nuutinen

"""




def select_variables(df,variable_set,impution_type,target):

    
    variables_m0 = []
    
   
##-------------------------------------
    
    if (variable_set == 'scales'):
        print ('Scale value data')
        variables_m0 = [ 
            'pre_m0_extraversion_TIPI',
            'pre_m0_aggreableness_TIPI',
            'pre_m0_conscientiousness_TIPI',
            'pre_m0_emot_stab_TIPI',
            'pre_m0_openess_TIPI',
            'pre_m0_optimism_LOT',
            'pre_m0_comprehensibility_SOC',
            'pre_m0_manageability_SOC',
            'pre_m0_meaningfulness_SOC',
            'pre_m0_total_coherence_SOC',
            'pre_m0_Forward_PACT',
            'pre_m0_Trauma_PACT',
            'pre_m0_Flexibility_PACT',
            'pre_m0RI5rev',
            'pre_m0_self_blame_CERQ',
            'pre_m0_other_blame_CERQ',
            'pre_m0_rumination_CERQ',
            'pre_m0_catastrophizing_CERQ',
            'pre_m0_perspective_CERQ',
            'pre_m0_pos_refus_CERQ',
            'pre_m0_pos_reapp_CERQ',
            'pre_m0_acceptance_CERQ',
            'pre_m0_planning_CERQ',
            'pre_m0_negative_overall_CERQ',
            'pre_m0_positive_overall_CERQ',
            'pre_m0_mindfulness_MAAS',
            'pre_m0_resilience_CDRISC',
            'pre_m0_coping_with_cancer_CBI',
            'pre_m0_Global_QLQ30',
            'pre_m0_Phys_Fun_QLQ30',
            'pre_m0_Role_Fun_QLQ30',
            'pre_m0_Emot_Fun_QLQ30',
            'pre_m0_Cogn_Fun_QLQ30',
            'pre_m0_Soc_Fun_QLQ30',
            'pre_m0_Fatigue_QLQ30',
            'pre_m0_Nausea_QLQ30',
            'pre_m0_Pain_QLQ30',
            'pre_m0_Dyspnoea_QLQ30',
            'pre_m0_Insomnia_QLQ30',
            'pre_m0_Apetite_QLQ30',
            'pre_m0_Constipation_QLQ30',
            'pre_m0_Diarrhoea_QLQ30',
            'pre_m0_Financial_QLQ30',
            'pre_m0_Body_Image_BR23',
            'pre_m0_Side_Effects_BR23',
            'pre_m0_Breast_Symptoms_BR23',
            'pre_m0_Arm_Symptoms_BR23',
            'pre_m0_Upset_Hair_Image_BR23',
            'pre_m0_Future_Persp_Image_BR23',
            'pre_m0_Sex_Funct_BR23',
            'pre_m0_Sex_Enjoy_BR23',
            'pre_m0_fear_of_recur_FCRI',
            'pre_m0_anxiety_HADS',
            'pre_m0_depression_HADS',
            'pre_m0_mental_health_total_HADS',
            'pre_m0_negative_affect_PANAS',
            'pre_m0_positive_affect_PANAS',
            'pre_m0_anxiety_HADSgroups1.2',
            'pre_m0_depression_HADSgroups1.2',
            'pre_m0_MentalH_HADSgroups1.14'
            ]

        vars_m6 = [
        target]

        if (impution_type == 'median'):
            for a in range(len(variables_m0)):
                median = df[variables_m0[a]].median()
                for k in range(len(df)):
                    if (str(df[variables_m0[a]][k]) == 'nan'):
                        df[variables_m0[a]][k] = median
                    
        df_sel = df[variables_m0 + vars_m6]


##-------------------------------------

    if (variable_set == 'sode'):
        print ('Sociodemographics and lifestyle data')
        variables_m0 = [
            'sode_age',
            'sode_education_1',
            'sode_education_2',
            'sode_number_of_children',
            'sode_children_yes',
            'sode_marital_status',
            'sode_alone',
            'sode_employed',
            'sode_net_monthly_income',
            'sode_sick_leave_days',
            'sode_ever_smoked',
            'sode_smoking_how_many',
            'sode_frequency_wine_or_beer',
            'sode_weight',
            'sode_height',
            'sode_bmi',
            'sode_obese',
            'sode_exercise',
                ]

        vars_m6 = [
        target]

        if (impution_type == 'median'):
            for a in range(len(variables_m0)):
                median = df[variables_m0[a]].median()
                for k in range(len(df)):
                    if (str(df[variables_m0[a]][k]) == 'nan'):
                        df[variables_m0[a]][k] = median
        
        df_sel = df[variables_m0 + vars_m6]
    

##-------------------------------------
        
        
    if (variable_set == 'all_raw_m0'):
        print ('All M0 raw data')
        
        variables_m0 = [
                'M0_br23_1',
                'M0_br23_2',
                'M0_br23_3',
                'M0_br23_4',
                'M0_br23_5',
                'M0_br23_6',
                'M0_br23_7',
                'M0_br23_8',
                'M0_br23_9',
                'M0_br23_10',
                'M0_br23_11',
                'M0_br23_12',
                'M0_br23_13',
                'M0_br23_14',
                'M0_br23_15',
                'M0_br23_16',
                'M0_br23_17',
                'M0_br23_18',
                'M0_br23_19',
                'M0_br23_20',
                'M0_br23_21',
                'M0_br23_22',
                'M0_br23_23',
                'M0_c30_1',
                'M0_c30_2',
                'M0_c30_3',
                'M0_c30_4',
                'M0_c30_5',
                'M0_c30_6',
                'M0_c30_7',
                'M0_c30_8',
                'M0_c30_9',
                'M0_c30_10',
                'M0_c30_11',
                'M0_c30_12',
                'M0_c30_13',
                'M0_c30_14',
                'M0_c30_15',
                'M0_c30_16',
                'M0_c30_17',
                'M0_c30_18',
                'M0_c30_19',
                'M0_c30_20',
                'M0_c30_21',
                'M0_c30_22',
                'M0_c30_23',
                'M0_c30_24',
                'M0_c30_25',
                'M0_c30_26',
                'M0_c30_27',
                'M0_c30_28',
                'M0_c30_29',
                'M0_c30_30',
                'M0_hads1',
                'M0_hads2',
                'M0_hads3',
                'M0_hads4',
                'M0_hads5',
                'M0_hads6',
                'M0_hads7',
                'M0_hads8',
                'M0_hads9',
                'M0_hads10',
                'M0_hads11',
                'M0_hads12',
                'M0_hads13',
                'M0_hads14',
                'M0_nccn_distress_thermometer',
                'M0_general_se_1_item',
                'M0_panas1',
                'M0_panas2',
                'M0_panas3',
                'M0_panas4',
                'M0_panas5',
                'M0_panas6',
                'M0_panas7',
                'M0_panas8',
                'M0_panas9',
                'M0_panas10',
                'M0_cd1',
                'M0_cd2',
                'M0_cd3',
                'M0_cd4',
                'M0_cd5',
                'M0_cd6',
                'M0_cd7',
                'M0_cd8',
                'M0_cd9',
                'M0_cd10',
                'M0_tipi1',
                'M0_tipi2',
                'M0_tipi3',
                'M0_tipi4',
                'M0_tipi5',
                'M0_tipi6',
                'M0_tipi7',
                'M0_tipi8',
                'M0_tipi9',
                'M0_tipi10',
                'M0_lot1',
                'M0_lot2',
                'M0_lot3',
                'M0_lot4',
                'M0_lot5',
                'M0_lot6',
                'M0_lot7',
                'M0_lot8',
                'M0_lot9',
                'M0_lot10',
                'M0_soc1',
                'M0_soc2',
                'M0_soc3',
                'M0_soc4',
                'M0_soc5',
                'M0_soc6',
                'M0_soc7',
                'M0_soc8',
                'M0_soc9',
                'M0_soc10',
                'M0_soc11',
                'M0_soc12',
                'M0_soc13',
                'M0_pact1',
                'M0_pact2',
                'M0_pact3',
                'M0_pact4',
                'M0_pact5',
                'M0_pact6',
                'M0_pact7',
                'M0_pact8',
                'M0_pact9',
                'M0_pact10',
                'M0_pact11',
                'M0_pact12',
                'M0_pact13',
                'M0_pact14',
                'M0_pact15',
                'M0_pact16',
                'M0_pact17',
                'M0_pact18',
                'M0_pact19',
                'M0_pact20',
                'M0_cerq1',
                'M0_cerq2',
                'M0_cerq3',
                'M0_cerq4',
                'M0_cerq5',
                'M0_cerq6',
                'M0_cerq7',
                'M0_cerq8',
                'M0_cerq9',
                'M0_cerq10',
                'M0_cerq11',
                'M0_cerq12',
                'M0_cerq13',
                'M0_cerq14',
                'M0_cerq15',
                'M0_cerq16',
                'M0_cerq17',
                'M0_cerq18',
                'M0_maas1',
                'M0_maas2',
                'M0_maas3',
                'M0_maas4',
                'M0_maas5',
                'M0_maas6',
                'M0_maas7',
                'M0_maas8',
                'M0_maas9',
                'M0_maas10',
                'M0_maas11',
                'M0_maas12',
                'M0_maas13',
                'M0_maas14',
                'M0_maas15',
                'M0_perceived_suppport_1_item',
                'M0_cbi1',
                'M0_cbi2',
                'M0_cbi3',
                'M0_cbi4',
                'M0_cbi5',
                'M0_cbi6',
                'M0_cbi7',
                'M0_cbi8',
                'M0_cbi9',
                'M0_cbi10',
                'M0_cbi11',
                'M0_cbi12',
                'M0_fcri1',
                'M0_fcri2',
                'M0_fcri3',
                'M0_fcri4',
                'M0_fcri5',
                'M0_fcri6',
                'M0_fcri7',
                'M0_fcri8',
                'M0_fcri9'
            ]
        
        vars_m6 = [
        target]

        if (impution_type == 'median'):
            for a in range(len(variables_m0)):
                median = df[variables_m0[a]].median()
                for k in range(len(df)):
                    if (str(df[variables_m0[a]][k]) == 'nan'):
                        df[variables_m0[a]][k] = median
        
        if (impution_type == 'knn'):
            from sklearn.impute import KNNImputer
            imp = KNNImputer(n_neighbors=2, weights="uniform")
            imp.fit(df[variables_m0])
            df[variables_m0] = imp.transform(df[variables_m0])
        
        df_sel = df[variables_m0 + vars_m6]
        
        
            ##-------------------------------------
    if (variable_set == 'medical'):
        print ('Medical and treatment')
        variables_m0 = [ 
        'labs_baseline_alt',
        'labs_baseline_creatinine',
        'labs_baseline_er',
        'labs_baseline_erclass',
        'labs_baseline_prclass',
        'labs_baseline_her2class',
        'labs_baseline_ki67class',
        'labs_Luminal_A',
        'labs_Luminal_B',
        'labs_Triple_negative',
        'labs_HER2_enriched',
        'labs_HER2Positive',
        'labs_positive_genetic_testing',
        'labs_family_history',
        'labs_baseline_hb',
        'labs_baseline_her2',
        'labs_baseline_histological_type',
        'labs_baseline_hscrp',
        'labs_baseline_ki67',
        'labs_molecular_classification',
        'labs_baseline_leukocytes',
        'labs_baseline_neutrofiles',
        'labs_baseline_thrombocytes',
        'labs_baseline_pn',
        'labs_baseline_pr',
        'labs_baseline_pt',
        'labs_baseline_serumbilirubin',

        'treat_side_effect_other',
        'treat_side_effect_osteoporosis',
        'treat_side_effect_neutropenic_fever',
        #'treat_side_effect_heart_failure',
        #'treat_side_effect_coronary_sdr',
        'treat_side_effect_asymptomatic_decrease_of_lvef',

        'medical_radiotherapy',
        'medical_positive_genetic_testing',
        'medical_menopausal_status_pretreatment_pre_M0',
        'medical_menopausal_status_pretreatment_post_M0',
        'medical_family_history',
        'medical_endocrine',
        'medical_chemo',
        'medical_cancer_stage',
        'medical_cancer_grade',
        'medical_baseline_pt',
        'medical_baseline_hormone_replacement_pre_treatment',
        'medical_baseline_hb',
        'medical_baseline_chronic_illness',
        'medical_antiher',
        'medical_M0_psychotropics',
        'medical_M0_performancestatus',
        
        'medical_cancer_stage',
        'medical_cancer_grade',
        'medical_chemo',
        'medical_radiotherapy',
        'medical_endocrine',
        'medical_antiher'
        
        # OBS! select disease only when n>20
        'diseases_preexisting_illnesses',
        'diseases_baseline_chronic_illness',
        'diseases_preexisting_metabolicillness',	
        'diseases_chronic_hypertension',
        'diseases_preexisting_mentalillness',	
        'diseases_chronic_hypothyreosis',
        'diseases_chronic_asthma',
        'diseases_chronic_diabetes',
        'diseases_Hypercholesterolemia'
       # 'diseases_dysthymia',
       # 'diseases_Anxiety',
       # 'diseases_Panic',
       # 'diseases_Migraine',
       # 'diseases_chronic_depression',
       # 'diseases_Fibromyalgia',
       # 'diseases_INSOMNIA',
       # 'diseases_polycystic_ovary_syndrome',
       # 'diseases_chronic_copd',
       # 'diseases_chronic_hypertension',
       # 'diseases_chronic_asthma',
       # 'diseases_chronic_cardiac_disease',
       # 'diseases_chronic_diabetes',
       # 'diseases_chronic_hypothyreosis',
       # 'diseases_chronic_arthrosis',
       # 'diseases_iron_deficiency_anemia',
       # 'diseases_obesity',
       # 'diseases_Hypercholesterolemia',
       # 'diseases_aortic_regurgitation',
       # 'diseases_MDS',
       # 'diseases_IBS',
       # 'diseases_arythmia',
       # 'diseases_Fibrillatio_atriorum_paroxysmalis',
       # 'diseases_cholelithiasis',
       # 'diseases_seronegative_spondyloarthropathy',
       # 'diseases_Hyperthyroidism',
       # 'diseases_venous_insufficiency',
       # 'diseases_poliomyelitis_sequelae',
       # 'diseases_Tremor',
       # 'diseases_essentielli_trombisytosis',
       # 'diseases_Autoimmune_hepatitis',
       # 'diseases_colitis_collagenosa',
       # 'diseases_mitral_valve_regurgitation',
       # 'diseases_Dyslipidemia',
       # 'diseases_emphysema',
       # 'diseases_degenerative_articular_disease',
       # 'diseases_Cholesterol',
       # 'diseases_HASHIMOTO_THYROIDE_DISEASE',
       # 'diseases_sarcoidosis',
       # 'diseases_IgA_nephropathy',
       # 'diseases_hyperlipidemia',
       # 'diseases_Glaucoma',
       # 'diseases_Back_pain',
       # 'diseases_dysthyroidism',
       # 'diseases_AF',
       # 'diseases_Rheumatic_disease',
       # 'diseases_Osteopenia',
       # 'diseases_colitis_ulcerosa',
       # 'diseases_Endometriosis',
       # 'diseases_Dermatomyositis',
       # 'diseases_Osteoporosis',
       # 'diseases_eosinophilic_oesophagitis',
       # 'diseases_polymyalgia_rheumatica',
       # 'diseases_APCresistance',
       # 'diseases_fasialNervePalsy',
       # 'diseases_anemia',
       # 'diseases_Bronchiectasis',
       # 'diseases_celiac',
       # 'diseases_hepatitis',
       # 'diseases_spinalStenosis',
       # 'diseases_hodgin_in_the_past',
       # 'diseases_SCC',
       # 'mental_health_chronic_depression',
       # 'diseases_baseline_chronic_illness',
       # 'diseases_preexisting_illnesses',
       # 'diseases_preexisting_mentalillness'
       # 'diseases_preexisting_metabolicillness'
            ]

        vars_m6 = [
        target]

        df_sel = df[variables_m0 + vars_m6]





##-------------------------------------        
        
    if (variable_set == 'selected_10'):
        print ('Selected 10 from different sets')
        
        variables_m0 = [
                # Raw
                'M0_c30_29',
                'M0_c30_30',
                'M0_nccn_distress_thermometer',
                'M0_panas5',
                'M0_panas2',
                'M0_panas3',
                'M0_panas7',
                'M0_c30_21',
                'M0_c30_25',
                'M0_c30_19',
                # Scales
                'pre_m0_Global_QLQ30',
                'pre_m0_negative_affect_PANAS',
                'pre_m0_mental_health_total_HADS',
                'pre_m0_depression_HADS',
                'pre_m0_Cogn_Fun_QLQ30',
                'pre_m0_anxiety_HADS',
                'pre_m0_Emot_Fun_QLQ30',
                'pre_m0_coping_with_cancer_CBI',
                'pre_m0_Diarrhoea_QLQ30',
                'pre_m0_Pain_QLQ30',
                # Sode
                'sode_net_monthly_income',
                'sode_age',
                'sode_education_1',
                'sode_exercise',
                'sode_net_monthly_income',
                'sode_number_of_children',
                'sode_employed',
                'sode_sick_leave_days',
                'sode_education_2',
                'sode_bmi',
                # Medical and treatment
                'medical_cancer_stage',
                'medical_cancer_grade',
                'medical_chemo',
                'mental_health_preexisting_mentalillness',
                'mental_health_chronic_depression',
                'labs_baseline_ki67',
                'labs_baseline_hb',
                'labs_family_history',
                'labs_Triple_negative',
                'labs_baseline_creatinine',
            ]
        
        vars_m6 = [
        target]

        
        df_sel = df[variables_m0 + vars_m6]


    
    df_sel_y = df_sel[[
                target
                ]]
    
    df_sel.drop(list(df_sel_y.columns), axis=1, inplace=True) 

    return df_sel, df_sel_y




