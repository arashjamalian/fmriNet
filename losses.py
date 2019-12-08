from tensorflow.keras import backend as K

def custom_weighted_loss(yTrue, yPred, weights):
    loss = yTrue * K.log(yPred) * weights
    loss = -K.sum(loss, -1)
    return loss

def weighted_crossentropy_loss(weights):
  kWeights = K.variable(weights)
  def cLoss(yTrue, yPred):
    return custom_weighted_loss(yTrue, yPred, kWeights)
  return cLoss


