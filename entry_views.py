import sys
print sys.getdefaultencoding()
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restplus import Api, Resource, Namespace, fields
from flask import request, jsonify
from datetime import datetime


from entry_models import journalEntry

app = Flask(__name__)

api = Api(app, version='1.0', title='My Journal', description= 'My Online Journal')

# data structure to store entry offers
entries = {}

entry = api.model('entry offer', {
    'title': fields.String(description='title of journal entry'),
    'body': fields.String(description='body of journal entry')
    
})



@api.route('/api/v1/entries')
class Entries(Resource):

    @api.doc(responses={'message': 'journal entry added successfully.',
                        201: 'Created', 400: 'BAD FORMAT'})
    @api.expect(entry)
    def post(self):
        """Create an entry."""
        data = request.get_json()
        # Check whether there is data
        if any(data):
            # save entry to data structure
            
            try:
                # set id for the entry offer
                journal_entry = journalEntry(data)
                entry_id = len(entries) + 1
                entries[(entry_id)] = journal_entry.getDict()
                response = {'message': 'journal entry added successfully.',
                            'entry id': entry_id}
                return response, 201
            except Exception as e:
                return {'message': 'use correct format for date and time.'}, 400
        else:
            return {'message': 'make sure you provide all required fields.'}, 400

    @api.doc('list of entries', responses={200: 'OK'})
    def get(self):
        """Fetch all entries."""
        return (entries)

#api.add_resource(entries, '/entries')

@api.route('/api/v1/entries/<string:entry_id>')
class SingleEntry(Resource):

    @api.doc('Fetch a single entry',
             params={'entry_id': 'Id for a single entry'},
             responses={200: 'OK', 404: 'NOT FOUND'})
    def get(self, entry_id):
        """Fetch a single entry."""
        try:
            entry = entries[int(entry_id)]
            entry['id'] = int(entry_id)
            return jsonify(entry)
        except Exception as e:
            return {'message': 'entry does not exist'}, 404

    
    def update(self, entry_id):
        ''' Modify an entry '''




'''
if __name__=='__main__':
    app.run(debug=True)
'''