# -*- coding: utf-8 -*-
__author__ = 'shn7798'

from FlaskZhihu.constants import *


class CollectionOperationMixin(object):
    def add_collection_comment(self, collection, comment):
        comment.user = self
        collection.comments.appen(comment)

    def add_collection_answer(self, collection, answer):
        collection.answers.append(answer)

    def follow_collection(self, collection):
        op = self.op_on_collection(collection, edit=True)
        op.follow = FOLLOW_ON

    def unfollow_collection(self, collection):
        op = self.op_on_collection(collection, edit=True)
        op.follow = FOLLOW_OFF