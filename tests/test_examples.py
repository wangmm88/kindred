import sys

import kindred
from kindred.CandidateBuilder import CandidateBuilder
from kindred.Vectorizer import Vectorizer
from kindred.Parser import Parser
from kindred.RelationClassifier import RelationClassifier
from kindred.Evaluator import Evaluator

from kindred.datageneration import generateData,generateTestData

def _bionlpst_bb3():
	assert False
	trainData = kindred.bionlpst.load('2016-BB3-event-train')
	devData = kindred.bionlpst.load('2016-BB3-event-dev')
	
	devData_TextAndEntities = [ d.getTextAndEntities() for d in devData ]
	devData_Relations = [ d.getRelations() for d in devData ]

	classifier = RelationClassifier(useBuilder=True)
	classifier.train(trainData)

	predictedRelations = classifier.predict(devData) #devData_TextAndEntities)

	evaluator = Evaluator()
	f1score = evaluator.evaluate(devData_Relations, predictedRelations, metric='f1score')
	print("f1score:",f1score)
	assert f1score > 0.5

def _bionlpst_seedev():
	assert False
	trainData = kindred.bionlpst.load('2016-SeeDev-binary-train')
	devData = kindred.bionlpst.load('2016-SeeDev-binary-dev')
	
	devData_TextAndEntities = [ d.getTextAndEntities() for d in devData ]
	devData_Relations = [ d.getRelations() for d in devData ]

	classifier = RelationClassifier()
	classifier.train(trainData)

	predictedRelations = classifier.predict(devData) #devData_TextAndEntities)

	evaluator = Evaluator()
	f1score = evaluator.evaluate(devData_Relations, predictedRelations, metric='f1score')
	print("f1score:",f1score)
	assert f1score > 0.33

def _pubannotation():
	trainData = kindred.PubAnnotationData('2016-SeeDev-binary-training')
	model = kindred.train(trainData)
	text = 'A SeeDev related text goes here'
	predictedRelations = model.predict(text)
	assert len(predicted_relations) == 1

def _pubtator():
	assert False
	
def _unicodeCheck():
	assert False
	
def _naryRelations():
	assert False
	
if __name__ == '__main__':
	test_bionlpst_bb3()
	#test_bionlpst_seedev()
