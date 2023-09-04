import importlib.util

# Define the module name (with hyphen)
module_name = "102-magic_calculation"

# Use importlib to create a module object from the file
module_spec = importlib.util.spec_from_file_location(module_name, module_name + ".py")
magic_calculation_module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(magic_calculation_module)

# Call the function from the dynamically imported module
result = magic_calculation_module.magic_calculation(3, 5)

# Print the result
print("Result:", result)

