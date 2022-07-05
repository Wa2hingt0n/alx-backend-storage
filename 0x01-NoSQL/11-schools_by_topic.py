#!/usr/bin/env python3
""" Defines a function 'schools_by_topic' """


def schools_by_topic(mongo_collection, topic):
    """ Returns a list of schools having a specific topic """
    top = {"topics": {"$elemMatch": {"$eq": topic}}}
    return [document for document in mongo_collection.find(top)]
