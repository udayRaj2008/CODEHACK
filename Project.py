# PROBLEM STATEMENT:  Climate Change and Variability in adaptive agriculture and food security

# SOLUTION:A tool that helps farmers integrate agroforestry practices into their land use plans. The system should recommend suitable tree species and placement to improve soil fertility, provide shade, and sequester carbon.

import random

# Sample data: Tree species and their attributes
tree_species = {
    "Acacia": {"soil_improvement": 0.8, "shade_provision": 0.7, "carbon_sequestration": 0.9},
    "Eucalyptus": {"soil_improvement": 0.6, "shade_provision": 0.5, "carbon_sequestration": 0.8},
    "Fruit Tree": {"soil_improvement": 0.7, "shade_provision": 0.8, "carbon_sequestration": 0.7},
    "Pine": {"soil_improvement": 0.5, "shade_provision": 0.4, "carbon_sequestration": 0.6},
}

def recommend_agroforestry_practices(land_area, soil_condition):
    recommended_trees = []
    for species, attributes in tree_species.items():
        suitability_score = (attributes["soil_improvement"] + attributes["shade_provision"] + attributes["carbon_sequestration"]) / 3
        recommended_trees.append((species, suitability_score))
    
    recommended_trees.sort(key=lambda x: x[1], reverse=True)
    return recommended_trees

# User-specific data
user_land_area = 10  # in acres
user_soil_condition = "Well-drained"

# Recommend agroforestry practices
recommended_trees = recommend_agroforestry_practices(user_land_area, user_soil_condition)

# Display recommended trees
print("Recommended Agroforestry Practices:")
for species, score in recommended_trees:
    print(f"{species}: Suitability Score = {score:.2f}")
