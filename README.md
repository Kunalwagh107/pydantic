# Pydantic Examples Project

A collection of examples demonstrating Pydantic's data validation and settings management capabilities in Python.

## Overview

This project contains various examples showcasing different features of Pydantic, including:
- Basic type validation
- Required and optional fields
- Custom data validation
- Field validators
- Model validators
- Computed fields
- Nested models
- Serialization

## Examples

### 1. Basic Problem with Python Types
[1_problem_with_python.py](1_problem_with_python.py) demonstrates why we need better type validation in Python.

### 2. Basic Pydantic Usage
[2_pydantic.py](2_pydantic.py) shows the basic usage of Pydantic models with simple type validation.

### 3. Detailed Pydantic Model
[3_detailed_pydantic_model.py](3_detailed_pydantic_model.py) shows complex validations using:
- Lists
- Dictionaries
- Multiple data types

### 4. Required and Optional Fields
[4_required_and_optional_field.py](4_required_and_optional_field.py) demonstrates how to define:
- Required fields
- Optional fields using `Optional` type hint

### 5. Data Validation Series
1. [5_data_validation_pydantic.py](5_data_validation_pydantic.py) - Custom data types (`EmailStr`, `AnyUrl`)
2. [5.1_data_validation_pydantic.py](5.1_data_validation_pydantic.py) - Using `Field` for validation
3. [5.2_field_validator.py](5.2_field_validator.py) - Field-level validation
4. [5.3_fv_modal_validator.py](5.3_fv_modal_validator.py) - Model-level validation

### 6. Computed Fields
[6_computed_field.py](6_computed_field.py) shows how to create computed fields using `@computed_field` decorator.

### 7. Nested Models
[7_nested_field.py](7_nested_field.py) demonstrates how to nest Pydantic models within each other.

### 8. Serialization
[8_serialization.py](8_serialization.py) shows how to:
- Convert models to dictionaries
- Convert models to JSON
- Include/exclude fields during serialization

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
