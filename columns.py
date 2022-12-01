from antihistamine.meta.foods import GROUPS
ATHENA_COLUMN = "Athena ID"


NAME_COLUMN = 'Name'
WEIGHT_COLUMN = 'f_weight'
AGE_COLUMN = 'age'

META_COLUMNS = [
    NAME_COLUMN,
    WEIGHT_COLUMN,
    AGE_COLUMN
]

FLAG_COLUMN_SCORES = "__scores"
FLAG_COLUMN_TESTS = "__tests"
FLAG_COLUMN_ENDOTYPE = "__endotype"
FLAG_COLUMN_FDS = "__fds"
FLAG_COLUMN_FDV = "__fdv"


FLAG_COLUMNS = [
    FLAG_COLUMN_SCORES,
    FLAG_COLUMN_TESTS,
    FLAG_COLUMN_ENDOTYPE,
    FLAG_COLUMN_FDS,
    FLAG_COLUMN_FDV
]

ENDOTYPE_COLUMN = "Endotype"

TESTS_COLUMNS = [
    "almond_ige",
    "coconut_ige",
    "peanut_ige",
    "pecan_ige",
    "sesame_ige",
    "hazelnut_ige",
    "cashew_ige",
    "brazilnut_ige",
    "pine_nut_ige",
    "walnut_ige",
    "pistachio_ige",
    "macadamia_ige",
    "sweet_chestnut_ige",
    "pumpkin_ige",
    "sunflower_ige",
    "poppy_ige",
    "mustard_ige",
    "linseed_ige_flax",
    "chickpea_ige",
    "lentil_ige",
    "black_beans_ige",
    "pinto_beans_ige",
    "kidney_beans_ige",
    "navy_beans_ige",
    "rape_seed_ige",
    "lima_beans_ige",
    "soy_ige",
    "green_pea_ige",
    "cow_milk_ige",
    "boiled_cow_milk_ige",
    "goat_milk_ige",
    "sheep_milk_ige",
    "mare_milk_ige",
    "beef_ige",
    "egg_white_ige",
    "egg_yolk_ige",
    "chicken_ige",
    "wheat_ige",
    "barley_ige",
    "rye_ige",
    "buckwheat_ige",
    "white_rice_ige",
    "oat_ige",
    "peach_ige",
    "pineapple",
    "apple_ige",
    "mango",
    "avocado",
    "banana",
    "kiwi_ige",
    "celery_ige",
    "cod_ige",
    "lobster_ige",
    "shrimp_ige",
    "crab_ige",
    "salmon_ige",
    "catfish_ige",
    "scallop_ige",
    "clam_ige",
    "tuna_ige",
    "halibut_ige",
    "red_snapper",
    "tilapia_ige",
    "oyster_ige",
    "turkey_ige",
    "cultivated_wheat_ige",
    "potato_ige",
    "tomato_ige",
    "common_millet_ige",
    "quinoa_ige",
    "corn_ige",
    "cockroach_ige",
    "white_mulberry_ige",
    "johnson_grass_ige",
    "mouse_urine_protein_ige",
    "dermatophagoides_pteronyssinus_ige",
    "dermatophagoides_farinae_ige",
    "penicillium_chrysogenum_ige",
    "cladosporium_herbarum_ige",
    "aspergillus_fumigatus_ige",
    "alternaria_alernata_ige",
    "alder_tree_ige",
    "red_cedar_ige",
    "olive_tree_ige",
    "walnut_tree_ige",
    "cottonwood_ige",
    "common_ragweed_ige",
    "mugwort_ige",
    "russian_thistle_ige",
    "common_pigweed_ige",
    "cat_dander_ige",
    "dog_dander_ige",
    "oak_tree_ige",
    "elm_tree_ige",
    "bermuda_grass_ige",
    "timothy_grass_ige",
    "mucor_racemosus_ige",
    "candida_albicans_ige",
    "mountain_juniper_ige",
    "peanut_spt",
    "walnut_spt",
    "almond_spt",
    "brazilnut_spt",
    "cashew_spt",
    "hazelnut_spt",
    "coconut_spt",
    "pecan_spt",
    "green_pea_spt",
    "pine_nut_spt",
    "macadamia_spt",
    "pistachio_spt",
    "sesame_spt",
    "chickpea_spt",
    "lentil_spt",
    "pumpkin_spt",
    "sunflower_spt",
    "mustard_spt",
    "soy_spt",
    "positive_control",
    "negative_control",
    "mango_spt",
    "banana_spt",
    "avocado_spt",
    "pineapple_spt",
    "cow_milk_spt",
    "boiled_cow_milk_spt",
    "goat_milk_spt",
    "boiled_goat_milk_spt",
    "beef_spt",
    "egg_white_spt",
    "egg_yolk_spt",
    "chicken_spt",
    "wheat_spt",
    "barley_spt",
    "rye_spt",
    "oat_spt",
    "white_rice_spt",
    "buckwheat_spt",
    "poppy_spt",
    "chia_spt",
    "linseed_spt_flax",
    "black_beans_spt",
    "pinto_beans_spt",
    "navy_beans_spt",
    "lima_beans_spt",
    "kidney_beans_spt",
    "cod_spt",
    "lobster_spt",
    "shrimp_spt",
    "crab_spt",
    "salmon_spt",
    "catfish_spt",
    "scallop_spt",
    "clam_spt",
    "tuna_spt",
    "strawberry_spt",
    "pru_p_1_ige",
    "pru_p_3_ige",
    "pru_p_4_ige",
    "rmald_1_ige",
    "rmal_d_3_ige",
    "act_d_8_ige",
    "api_g_1_01_ige",
    "ber_e_1_ige",
    "cor_a_1_ige",
    "cor_a_8_ige",
    "rcor_a_9_ige",
    "ncor_a_14_ige",
    "ana_o_3_ige",
    "jug_r_1_ige",
    "jug_r_3_ige",
    "gly_m_4_ige",
    "ngly_m_5_ige",
    "ngly_m_6_ige",
    "r_tri_a_14_ige",
    "tri_a_19_ige",
    "pen_a_1_ige",
    "gad_c_1_ige",
    "cyp_c_1_ige",
    "gal_d_1_ige",
    "gal_d_2_ige",
    "gal_d_3_ige",
    "bos_d_4_ige",
    "bos_d_5_ige",
    "bos_d_8_ige",
    "cyn_d_1_ige",
    "phl_p_1_ige",
    "phl_p_2_ige",
    "phl_p_6_ige",
    "phl_p_7_ige",
    "phl_p_12_ige",
    "phl_p_5b_ige",
    "amb_a_1_ige",
    "art_v_1_ige",
    "art_v_3_ige",
    "bet_v_1_ige",
    "bet_v_2_ige",
    "bet_v_4_ige",
    "bet_v_6_ige",
    "ole_e_1_ige",
    "ole_e_7_ige",
    "role_e9_ige",
    "alt_a_1_ige",
    "asp_0_21_ige",
    "can_f_1_ige",
    "can_f_2_ige",
    "can_f_3_ige",
    "can_f_5_ige",
    "fel_d_1_ige",
    "fel_d_2_ige",
    "fel_d_4_cat_ige",
    "equ_c_1_ige",
    "der_p_1_ige",
    "der_p_2_ige",
    "der_p_10_ige",
    "arah_1",
    "arah_2",
    "arah_3",
    "arah_8",
    "arah_9",
    "peanut_igg4",
    "egg_white_igg4",
    "sesame_igg4",
    "almond_igg4",
    "hazelnut_igg4",
    "pistachio_igg4",
    "cashew_igg4",
    "pecan_igg4",
    "milk_igg4",
    "walnut_igg4",
    "egg_yolk_igg4",
    "uib",
    "cyt",
    "ige",
    "eos",
    "igg",
    "igg_subclass1",
    "igg_subclass2",
    "igg_subclass3",
    "igg_subclass4",
    "igg_total"
]

SCORING_COLUMNS = [
    'Sesame',
    'Beans',
    'Chickpea',
    'Pea',
    'Lentils',
    'Almond',
    'Peanut',
    'Hazelnut',
    'Soy',
    'Buffalo milk',
    'Beef',
    'Mare milk',
    'Camel milk',
    'Cow milk',
    'Goat milk',
    'Quinoa',
    'Corn',
    'Rye',
    'Rice',
    'Oat',
    'Buckwheat',
    'Barley',
    'Wheat',
    'Dark tuna',
    'Tuna',
    'Carp',
    'Red fish',
    'White fish',
    'Oyster',
    'Clam',
    'Scallop',
    'Crab',
    'Shrimp',
    'Lobster',
    'Mollusk',
    'Shellfish',
    'Turkey',
    'Chicken',
    'Egg yolk',
    'Egg white',
    'Mustard',
    'Chia',
    'Poppy',
    'Flax',
    'Sunflower',
    'Pumpkin',
    'Macadamia',
    'Pistachio',
    'Cashew',
    'Coconut',
    'Chestnut',
    'Pine nut',
    'Brazil nut',
    'Pecan',
    'Walnut'
]

NAME_ADDON_DOSE_REQ = ' dosing required'
NAME_ADDON_CHALLENGE_AMOUNT = ' challenge amount'
NAME_ADDON_DOSE_CAPPED = ' dose capped'
NAME_ADDON_DOSE_MICRO = ' dose micro'
NAME_ADDON_DOSE_VISITS = ' dose visits'
NAME_ADDON_DOSE_VECTOR = ' dose vector'
NAME_ADDON_FOOD_SPAN = ' span'
NAME_ADDON_GROUP_SPAN = ' span'


DOSE_REQ_COLUMNS = [sc + NAME_ADDON_DOSE_REQ for sc in SCORING_COLUMNS]
DOSE_CAPPED_COLUMNS = [sc + NAME_ADDON_DOSE_CAPPED for sc in SCORING_COLUMNS]
DOSE_MICRO_COLUMNS = [sc + NAME_ADDON_DOSE_MICRO for sc in SCORING_COLUMNS]
DOSE_VECTOR_COLUMNS = [sc + NAME_ADDON_DOSE_VECTOR for sc in SCORING_COLUMNS]
FOOD_SPAN_COLUMNS = [sc + NAME_ADDON_FOOD_SPAN for sc in SCORING_COLUMNS]
GROUP_SPAN_COLUMNS = [g + NAME_ADDON_FOOD_SPAN for g in GROUPS]

RECOMMENDED_FOODS_COLUMN = 'recommended_foods'
MAINTENANCE_FOODS_COLUMN = 'maintenance_foods'
TREATMENT_FOODS_COLUMN = 'treatment_foods'

LAUNCH_VISIT_GROUPS_COLUMN = 'launch_visit_groups'

FDS_META_COLUMNS = [RECOMMENDED_FOODS_COLUMN, MAINTENANCE_FOODS_COLUMN, TREATMENT_FOODS_COLUMN]

FDS_COLUMNS = DOSE_REQ_COLUMNS + DOSE_CAPPED_COLUMNS + DOSE_MICRO_COLUMNS \
              + DOSE_VECTOR_COLUMNS + FOOD_SPAN_COLUMNS \
              + GROUP_SPAN_COLUMNS + FDS_META_COLUMNS

COLUMNS = [ATHENA_COLUMN] + FLAG_COLUMNS + META_COLUMNS + [ENDOTYPE_COLUMN] + TESTS_COLUMNS + SCORING_COLUMNS\
          + DOSE_REQ_COLUMNS + DOSE_CAPPED_COLUMNS + DOSE_MICRO_COLUMNS\
          + DOSE_VECTOR_COLUMNS + FOOD_SPAN_COLUMNS + GROUP_SPAN_COLUMNS + FDS_META_COLUMNS

ENDOTYPE_PREDICTION_COLUMNS = [ATHENA_COLUMN] + META_COLUMNS + [ENDOTYPE_COLUMN] + TESTS_COLUMNS

SCORING_PREDICTION_COLUMNS = [ATHENA_COLUMN] + META_COLUMNS + [ENDOTYPE_COLUMN] + TESTS_COLUMNS + SCORING_COLUMNS

FDS_PREDICTION_COLUMNS = [ATHENA_COLUMN] + META_COLUMNS + [ENDOTYPE_COLUMN] + TESTS_COLUMNS + SCORING_COLUMNS\
                         + DOSE_REQ_COLUMNS + DOSE_CAPPED_COLUMNS + DOSE_MICRO_COLUMNS \
                         + DOSE_VECTOR_COLUMNS + FOOD_SPAN_COLUMNS\
                         + GROUP_SPAN_COLUMNS + FDS_META_COLUMNS


