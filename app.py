from flask import Flask, jsonify, request

app = Flask(__name__)

items_db = {}
next_item_id = 0

def get_new_id():
    global next_item_id
    next_item_id += 1
    return next_item_id

@app.route('/')
def hello_world():
    return 'Hello, World! Your API is running.'

@app.route('/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'POST':
        # create a new item
        item_data = request.get_json()
        if not item_data or 'name' not in item_data:
            return jsonify({'error': 'Missing item data or name'}), 400 # Bad request

        new_id = get_new_id()
        new_item = {
            'id': new_id,
            'name': item_data['name'],
            'description': item_data.get('description', '')
        }
        items_db[str(new_id)] = new_item
        return jsonify(new_item), 201 # Return the new item and 201 Created status
    else: # GET request
        return jsonify(items_db)

@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_item(item_id):
    item_id_str = str(item_id)
    if item_id_str not in items_db:
        return jsonify({'error': 'Item not found'}), 404

    if request.method == 'GET':
        return jsonify(items_db[item_id_str])

    elif request.method == 'PUT':
        update_data = request.get_json()
        if not update_data:
            return jsonify({'error': 'Missing update data'}), 400

        item = items_db[item_id_str]
        item['name'] = update_data.get('name', item['name'])
        item['description'] = update_data.get('description', item['description'])
        items_db[item_id_str] = item
        return jsonify(item)

    elif request.method == 'DELETE':
        del items_db[item_id_str]
        return jsonify({'message': 'Item deleted'})

@app.route('/testing/reset', methods=['POST'])
def reset_for_testing():
    global items_db, next_item_id
    items_db = {}
    next_item_id = 0
    return jsonify({"message": "Database reset"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
