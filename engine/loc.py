class LocationService(object):
    __DEFAULT_COLLECTION_NAME = 'fmark_locations'
    collection = None

    def __init__(self, mdb, collection_name=None):
        '''Initializes the service with given mongodb database
        and, optionally a locations collection name'''
        self.collection = (str(collection_name) if collection_name
                else self.__DEFAULT_COLLECTION_NAME)

    def get_location_by_id(self, _id):
        '''Returns the location dict by its id in the database'''
        return self.collection.find_one(_id)
