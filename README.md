# Rule Engine with AST

## Overview

This is a simple 3-tier rule engine application developed using Flask, Python, and MySQL. The application allows users to determine eligibility based on various attributes such as age, department, income, and spending using conditional rules represented by an Abstract Syntax Tree (AST). It supports dynamic creation, combination, and modification of rules.

## Objectives

- **Develop a rule engine** that evaluates user eligibility based on specified attributes.
- **Utilize an Abstract Syntax Tree (AST)** to represent conditional rules.
- **Provide a simple UI**, API, and backend data for rule management.

## Data Structure

The application uses the following data structure to represent the AST:

- **Node**
  - `type`: A string indicating the node type ("operator" for AND/OR, "operand" for conditions).
  - `left`: A reference to another Node (left child).
  - `right`: A reference to another Node (right child for operators).
  - `value`: An optional value for operand nodes (e.g., number for comparisons).

## Sample Rules

- `rule1`: `"((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"`
- `rule2`: `"((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"`

## Database

The application uses MySQL to store rules and metadata. The schema for the rules table is as follows:

```sql
CREATE TABLE IF NOT EXISTS rules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rule_string TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


