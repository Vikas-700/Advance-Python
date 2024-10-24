# Quistion 1
models_2019={"Model S","Model X","Model 3","Model Y"}
models_2023={"Model 3","Model Y","Model Z","Model A"}
print("The models that were produced in both years")
print(models_2019.union(models_2023))
print()
print("The models that are unique to each year.")
print(models_2019.symmetric_difference(models_2023))
print()

# Quistion 2
factory_A_parts={"engine","brake","gearbox","seat","headlight"}
factory_B_parts={"seat","dashboard","gearbox","wheel","headlight"}
print("Find the parts common to both Factories.")
print(factory_A_parts.intersection(factory_B_parts))
print()
print("List the parts produced only in Factory A not and in Factory B")
print(list(factory_A_parts.difference(factory_B_parts)))


print()

# 3
current_models = {"Sedan", "SUV", "Truck", "Hatchback"} 
discontinued_models = {"Coupe", "Convertible", "Truck", "Hatchback"} 
print(" Find the models that are still in production.")
print(current_models-discontinued_models)
print()
print("Find the models that were discontinued.")
print(current_models.intersection(discontinued_models))
print()

#4
warehouse_parts = {"engine", "brake", "tire", "radiator", "mirror"} 
restocked_parts = {"tire", "brake", "radiator", "windshield"} 
print("Identify which parts are in the warehouse but not currently being restocked.")
print(warehouse_parts-restocked_parts)
print()
print("Find the parts that are restocked and already in the warehouse.")
print(warehouse_parts.intersection(restocked_parts))
print()

#5
customer_1_features = {"leather seats", "sunroof", "premium sound", "GPS"} 
customer_2_features = {"premium sound", "sunroof", "automatic parking", "heated seats"}
print("Find the features both customers selected.")
print(customer_1_features.intersection(customer_2_features)) 
print()
print("List the features that are unique to each customer")
print(customer_1_features.symmetric_difference(customer_2_features))