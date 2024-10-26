from flask import Flask, request, jsonify, send_from_directory
from rule_engine import create_rule, combine_rules, evaluate_rule
from database import create_table, create_connection
import json

app = Flask(__name__)
create_connection()
create_table()

@app.route('/create_rule', methods=['POST'])
def create_rule_route():
    data = request.get_json()
    rule_input = data.get('rule')

    try:
        ast = create_rule(rule_input)
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO rules (rule_string) VALUES (%s)", (rule_input,))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({'message': 'Rule added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/modify_rule', methods=['PUT'])
def modify_rule_route():
    data = request.get_json()
    rule_index = data.get('index')
    new_rule = data.get('rule')
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT rule_string FROM rules")
    rules = cursor.fetchall()
    cursor.close()
    connection.close()

    try:
        rules_list = [rule[0] for rule in rules]
        if 0 <= rule_index < len(rules_list):
            rules_list[rule_index] = new_rule
            
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE rules SET rule_string = %s WHERE rule_string = %s", (new_rule, rules_list[rule_index]))
            connection.commit()
            cursor.close()
            connection.close()

            return jsonify({'message': 'Rule modified successfully!'}), 200
        else:
            return jsonify({'error': 'Invalid rule index!'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/evaluate_rules', methods=['POST'])
def evaluate_rules_route():
    data = request.get_json()
    rules = data.get('rules')
    data_input = data.get('data')

    try:
        combined_ast = combine_rules(rules)
        result = evaluate_rule(combined_ast, data_input)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


if __name__ == "__main__":
    app.run(debug=True)
