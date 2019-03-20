from nn_1 import SnakeNN

class Snake:
    if __name__ == "__main__":
        nn = SnakeNN()
        nn_model = nn.model()
        nn_model.load(nn.filename)
        nn.visualise_game(nn_model)
