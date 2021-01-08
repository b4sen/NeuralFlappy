# This is an AI playing flappy bird implemented in PyTorch

## TODO:

- [ ] Add distance to top and bottom edge to the network -> 7 input nodes instead of 5?
- [x] Implement learning algorithm -> Adjust random weights by a number sampled from some distribution
- [x] Spawn more birds and try to save the best agent's `state_dict`
- [x] Improve physics -> add linearity to the change of velocity
- [ ] Display number of alive agents and generation number
- [ ] Add option to load trained model and let it play


## Description

This is a very simple FlappyBird clone implemented in PyGame which uses a basic feedforward network and trained using a genetic algorithm.
The mutation is very barbaric and the save functionality is not so elegant.

I used Dan Shiffmans video to implement the GA.
